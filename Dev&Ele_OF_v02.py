""" this module makes FDS and OpenSEES files script files, in thsi version any direction of structural memeber
can be chosen. There are separate python scripts for GUI and some of the functions used in the program. Those files
(gui and functions are imported in this program)
 NEW : Added a function to remove duplicate elements from Truss which were appeared due to same location
 Rev03 : Some of the functions which were making element files in different ways are removed"""

try:
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import filedialog
except ImportError:
    import Tkinter as tk
    import ttk
    import tkFileDialog as filedialog
import csv
import pandas as pd
import numpy as np
from decimal import *
from functions_OF_v02 import *
from gui_OF_v02 import *


tk.Button(general_inputs, text="Add Analysis", command=addAnalysis, width=10, height=1).grid(row=1, column=4, padx=5, pady=5)
tk.Button(OSFrame, text="Add Material", command=addMaterial, width=10, height=1).grid(row=2, column=4, padx=5, pady=5)
tk.Button(OSFrame, text="Add Constants", command=addHTConstants, width=10, height=1).grid(row=3, column=4)


def openNodesFile():  # opening the Nodes file before using it to write
    global nodesFile
    nodesFile = filedialog.askopenfilename(title="select a file", filetypes=(('All files', '*.*'),
                                                                             ('Text Files', ('*.txt', '*.dat', '*.csv'))))


tk.Button(elementFrame, text="Browse Nodes File", command=openNodesFile, width=15, height=1).grid(row=0, column=1)
tk.Label(elementFrame, width=16, text="Open Nodes File", anchor='e').grid(row=0, column=0, padx=5, pady=5)


def openElementFile():  # opening the beam-column element file before using it to write
    # noinspection PyGlobalUndefined
    global beamEleFile
    beamEleFile = filedialog.askopenfilename(
        title="select a file", filetypes=(('All files', '*.*'), ('Text Files', ('*.txt', '*.csv', '*.dat'))))


tk.Button(elementFrame, text="BC Element File", command=openElementFile, width=15, height=1).grid(row=1, column=1)
tk.Label(elementFrame, width=16, text="BC Element File", anchor='e').grid(row=1, column=0, padx=5, pady=5)


def openShellElementFile():  # opening SHELL file before using it to write
    global shellEleFile
    shellEleFile = filedialog.askopenfilename(
        title="select a file", filetypes=(('All files', '*.*'), ('Text Files', ('*.txt', '*.csv', '*.dat'))))


tk.Button(elementFrame, text="Shell Element File", command=openShellElementFile,
          width=15, height=1).grid(row=2, column=1)
tk.Label(elementFrame, width=15, text="Shell Element File", anchor='e').grid(row=2, column=0, padx=5, pady=5)


def nodesDict():  # creating dictionaries of nodes and nodes files
    global nodesFile
    createFolder('./ElementFiles')
    NODES_OUTPUT = 'ElementFiles/Nodes.csv'  # writing to make an CSV file
    NODES_OUTPUT2 = 'ElementFiles/Nodes2.csv'  # writing new files by Removing blank lines
    with open(nodesFile) as f1:
        stripped = (line.strip() for line in f1)
        lines = (line.replace("\t", " ").split() for line in stripped if line)
        csv.reader(f1, delimiter=',')
        with open(NODES_OUTPUT, 'w', newline='') as out_file:
            writer = csv.writer(out_file, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerows(lines)

    fn = open(NODES_OUTPUT2, 'w', newline='')
    nodeData = pd.read_csv(NODES_OUTPUT)
    first_column = nodeData.columns[0]
    nodeData = nodeData.drop([first_column], axis=1)
    nodeData.to_csv(fn, index=False)
    fn.close()
    '''this function reads all lines which are used to make list of all lines later to make dictionary '''

    def read_lines():
        with open(NODES_OUTPUT2) as file:
            reader = csv.reader(file)
            for row in reader:
                yield [float(jItem) for jItem in row]

    allLines = list(read_lines())
    global finalDict
    '''it makes a dictionary where first element is key and others are values '''
    finalDict = {nodes[0]: nodes[1:] for nodes in allLines}
    # convert key (node) as an integer and rounding all values to significant figures using ROUND (round) command

    global nodesDictionary
    nodesDictionary = {int(k): (float(X), float(Y), float(Z)) for k, (X, Y, Z) in finalDict.items()}


d1_button = tk.Button(elementFrame, text="Nodes Creation", command=nodesDict, width=15, height=1)
d1_button.grid(row=0, column=3, padx=10, pady=10)
tk.Label(elementFrame, width=15, text="Generate Nodes File", anchor='e').grid(row=0, column=2, padx=5, pady=5)


def bcElementDict():
    global beamEleFile
    createFolder('./ElementFiles')
    ELEMENT_OUTPUT = 'ElementFiles/Element.csv'
    ELEMENT_OUTPUT2 = 'ElementFiles/Element2.csv'
    with open(beamEleFile) as elementFile:
        strippedEle = (ele.strip() for ele in elementFile)
        elements = (ele.replace(" ", ",").split() for ele in strippedEle if
                    ele)  # be noted that elimination is "tab" here
        csv.reader(elementFile, delimiter=',')
        with open(ELEMENT_OUTPUT, 'w', newline='') as outFile:
            writer = csv.writer(outFile, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerows(elements)

    beamColData = pd.read_csv(ELEMENT_OUTPUT)
    c1 = beamColData.columns[0]
    c2 = beamColData.columns[1]
    c6 = beamColData.columns[5]
    c7 = beamColData.columns[6]
    c8 = beamColData.columns[7]
    c9 = beamColData.columns[8]
    c10 = beamColData.columns[9]

    fn2 = open(ELEMENT_OUTPUT2, 'w', newline='')
    beamColData = beamColData.drop([c1, c2, c6, c7, c8, c9, c10], axis=1)
    beamColData.to_csv(fn2, index=False)
    fn2.close()

    def read_lines2():
        with open(ELEMENT_OUTPUT2) as file2:
            reader2 = csv.reader(file2)
            for row3 in reader2:
                yield [int(float(k)) for k in row3]

    elementSet = list(read_lines2())
    global bcEleDictionary
    # making elements as dictionary where elements are keys and corresponding nodes are values
    bcEleDictionary = {elekey[0]: elekey[1:] for elekey in elementSet}


tk.Button(elementFrame, text="BC Elements ", command=bcElementDict, width=15, height=1).grid(row=1, column=3)
tk.Label(elementFrame, width=15, text="BC Element File", anchor='e').grid(row=1, column=2, padx=5, pady=5)


def shellElementDict():
    global shellEleFile
    createFolder('./ElementFiles')
    SHELL_ELEMENT_OUTPUT = 'ElementFiles/Element3.csv'
    SHELL_ELEMENT_OUTPUT2 = 'ElementFiles/Element4.csv'
    with open(shellEleFile) as elementFile:
        strippedEle = (ele.strip() for ele in elementFile)
        elements = (ele.replace("\t", " ").split() for ele in strippedEle if
                    ele)  # be noted that elimination is space here
        csv.reader(elementFile, delimiter=',')
        with open(SHELL_ELEMENT_OUTPUT, 'w', newline='') as outFile:
            writer = csv.writer(outFile, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerows(elements)

    shellData = pd.read_csv(SHELL_ELEMENT_OUTPUT)
    cS1 = shellData.columns[0]
    cS2 = shellData.columns[1]
    cS3 = shellData.columns[7]
    fnSE = open(SHELL_ELEMENT_OUTPUT2, 'w', newline='')
    shellData = shellData.drop([cS1, cS2, cS3], axis=1)
    shellData.to_csv(fnSE, index=False)
    fnSE.close()

    def read_lines2():
        with open(SHELL_ELEMENT_OUTPUT2) as file3:
            reader2 = csv.reader(file3)
            for row3 in reader2:
                yield [int(float(jSE)) for jSE in row3]

    elementSet2 = list(read_lines2())
    # noinspection PyGlobalUndefined
    global shellEleDictionary
    shellEleDictionary = {elekey[0]: elekey[1:] for elekey in elementSet2}


tk.Button(elementFrame, text="Shell Element File", command=shellElementDict, width=15, height=1).grid(row=2, column=3)
tk.Label(elementFrame, width=15, text="Create Shell Elements", anchor='e').grid(row=2, column=2, padx=5, pady=5)


def nodes1():
    matchingNodes = [key for key, (X, Y, Z) in nodesDictionary.items()
                     if (float(x_BeamLL.get()) <= X <= float(x_BeamUL.get())+0.00001) and
                     (float(y_BeamLL.get()) <= Y <= float(y_BeamUL.get())) and
                     (columnBegin <= Z <= columnBegin + float(incZ_Beam.get()))]
    return matchingNodes


def nodes2():    # increment X
    matchingNodes = [key for key, (X, Y, Z) in nodesDictionary.items()
                     if (beginXBeam <= X <= beginXBeam + float(incX_Beam.get())+0.00001) and    # 0.00001 is added to avoid decimal error
                     (float(y_BeamLL.get()) <= Y <= float(y_BeamUL.get())) and
                     (float(z_BeamLL.get()) <= Z <= float(z_BeamUL.get()))]
    return matchingNodes


def nodes3():   # increment Y
    matchingNodes = [key for key, (X, Y, Z) in nodesDictionary.items()
                     if a1 <= X <= a2 and
                     (beginYBeam <= Y <= beginYBeam + float(incY_Beam.get())+0.00001) and
                     zL1 <= Z <= zL2]
    return matchingNodes


def outputData():
    global iEle
    global jEle
    global entBeam
    global columnBegin, lowerZ, upperZ, lowerX, upperX, lowerY, upperY
    global beginXBeam, beginYBeam
    '''This part of the code makes devices for FDS using the above functions "fdsFileMaker"'''

    if incrementDirectionBEAM.get() == "Z":
        i = float(z_BeamLL.get())
        m = float(z_LenBeam.get())
        var = round(float(incZ_Beam.get()), 2)
        if units.get() == "m":
            fdsFileMaker(i, m, var, float(x_BeamLL.get()), float(y_BeamLL.get()), ior_Beam.get())

        if units.get() == "mm":
            fdsFileMaker(i, m, var, float(x_BeamLL.get())/1000,  float(y_BeamLL.get())/1000, ior_Beam.get())

    if incrementDirectionBEAM.get() == "X":
        initialY_Beam = float(y_BeamLL.get())
        initialX_Beam = float(x_BeamLL.get())
        BeamLengthX = float(x_LenBeam.get())
        incrementX_Beam = round(float(incX_Beam.get()), 2)
        if units.get() == "m":
            fdsFileMaker(initialX_Beam, BeamLengthX, incrementX_Beam, initialY_Beam,
                         float(z_BeamLL.get()), ior_Beam.get())
        if units.get() == "mm":
            fdsFileMaker(initialX_Beam, BeamLengthX, incrementX_Beam, initialY_Beam/1000,
                         float(z_BeamLL.get())/1000, ior_Beam.get())

    if incrementDirectionBEAM.get() == "Y":
        initialX_Beam = float(x_BeamLL.get())
        initialY_Beam = float(y_BeamLL.get())
        incrementY_Beam = float(incY_Beam.get())
        BeamLengthY = round(float(y_LenBeam.get()), 0)
        if units.get() == "m":
            fdsFileMaker(initialY_Beam, BeamLengthY, incrementY_Beam, initialX_Beam,
                         float(z_BeamLL.get()), ior_Beam.get())
        if units.get() == "mm":
            fdsFileMaker(initialY_Beam, BeamLengthY, incrementY_Beam, initialX_Beam/1000,
                         float(z_BeamLL.get())/1000, ior_Beam.get())


    #########################################-----functions for OpenSEES files

    if incrementDirectionBEAM.get() == "Z":
        global entCol
        initialZ = float(z_BeamLL.get())
        heightColumn = float(z_LenBeam.get())
        increment_Z = float(incZ_Beam.get())
        with open(osFile, 'a') as f3:
            f3.writelines("\n#This is Column {0}\n\n".format(entCol))
        if selectEntity.get() == "Isection":
            iEntity(initialZ, heightColumn, increment_Z, float(cX_iSec.get()), float(cY_iSec.get()),
                    float(flangeWidth.get()), float(beamHeight.get()), float(webThickness.get()),
                    float(flangeThickness.get()))
            mesh(initialZ, heightColumn, increment_Z, int(pChange.get()), float(meshFlangeWidth.get()),
                 float(meshFlangeThickness.get()), float(meshWebThickness.get()), float(meshWebHeight.get()),
                 int(modelMatTag.get()))

        if selectEntity.get() == "Block":
            blockEntity(initialZ, heightColumn, increment_Z, float(cX_Block.get()), float(cY_Block.get()),
                        float(widthBlock.get()), float(depthBlock.get()))
            meshBLK(initialZ, heightColumn, increment_Z, modelMatTag.get(), pChange.get(),
                    float(meshWidBlock.get()), float(meshDepthBlock.get()))

        if selectNodeSet.get() == "Faces":
            nodeSETFaces(initialZ, heightColumn, increment_Z, Nodeset.get())
        if selectNodeSet.get() == "Node Points":
            if selectEntity.get() == "Isection":
                nodeSETLoc(initialZ, heightColumn, increment_Z, float(beamHeight.get()))
            if selectEntity.get() == "Block":
                nodeSETLoc(initialZ, heightColumn, increment_Z, float(depthBlock.get()))

        fireModel(initialZ, heightColumn, increment_Z, fireModelType.get())
        heatFlux(initialZ, heightColumn, increment_Z, hfFaces.get(), modelHT_Tag.get())
        htRecorder(initialZ, heightColumn, increment_Z)
        entCol += 1

    if incrementDirectionBEAM.get() == "X":
        beginX_BEAM = float(x_BeamLL.get())
        lengthBEAM = float(x_LenBeam.get())
        incrementXBeam = round(float(incX_Beam.get()), 3)
        with open(osFile, 'a') as f3:
            f3.writelines("\n#This is Beam {0}\n\n".format(entBeam))
        if selectEntity.get() == "Isection":
            iEntity(beginX_BEAM, lengthBEAM, incrementXBeam, float(cX_iSec.get()), float(cY_iSec.get()),
                    float(flangeWidth.get()), float(beamHeight.get()), float(webThickness.get()),
                    float(flangeThickness.get()))
            mesh(beginX_BEAM, lengthBEAM, incrementXBeam, int(pChange.get()), float(meshFlangeWidth.get()),
                 float(meshFlangeThickness.get()), float(meshWebThickness.get()), float(meshWebHeight.get()),
                 int(modelMatTag.get()))

        if selectEntity.get() == "Block":
            blockEntity(beginX_BEAM, lengthBEAM, incrementXBeam, float(cX_Block.get()), float(cY_Block.get()),
                        float(widthBlock.get()), float(depthBlock.get()))
            meshBLK(beginX_BEAM, lengthBEAM, incrementXBeam, modelMatTag.get(), pChange.get(),
                    float(meshWidBlock.get()), float(meshDepthBlock.get()))

        if selectNodeSet.get() == "Faces":
            nodeSETFaces(beginX_BEAM, lengthBEAM, incrementXBeam, Nodeset.get())
        if selectNodeSet.get() == "Node Points":
            if selectEntity.get() == "Isection":
                nodeSETLoc(beginX_BEAM, lengthBEAM, incrementXBeam, float(beamHeight.get()))
            if selectEntity.get() == "Block":
                nodeSETLoc(beginX_BEAM, lengthBEAM, incrementXBeam, float(depthBlock.get()))

        fireModel(beginX_BEAM, lengthBEAM, incrementXBeam, fireModelType.get())
        heatFlux(beginX_BEAM, lengthBEAM, incrementXBeam, hfFaces.get(), modelHT_Tag.get())
        htRecorder(beginX_BEAM, lengthBEAM, incrementXBeam)
        entBeam += 1

    if incrementDirectionBEAM.get() == "Y":
        beginY_BEAM = float(y_BeamLL.get())
        incrementY_BEAM = float(incY_Beam.get())
        widthBEAM = float(y_LenBeam.get())
        with open(osFile, 'a') as f3:
            f3.writelines("\n#This is Beam {0}\n\n".format(entBeam))
        if selectEntity.get() == "Isection":
            iEntity(beginY_BEAM, widthBEAM, incrementY_BEAM, float(cX_iSec.get()), float(cY_iSec.get()),
                    float(flangeWidth.get()), float(beamHeight.get()), float(webThickness.get()),
                    float(flangeThickness.get()))
            mesh(beginY_BEAM, widthBEAM, incrementY_BEAM, int(pChange.get()), float(meshFlangeWidth.get()),
                 float(meshFlangeThickness.get()), float(meshWebThickness.get()), float(meshWebHeight.get()),
                 int(modelMatTag.get()))

        if selectEntity.get() == "Block":
            blockEntity(beginY_BEAM, widthBEAM, incrementY_BEAM, float(cX_Block.get()), float(cY_Block.get()),
                        float(widthBlock.get()), float(depthBlock.get()))
            meshBLK(beginY_BEAM, widthBEAM, incrementY_BEAM, modelMatTag.get(), pChange.get(),
                    float(meshWidBlock.get()), float(meshDepthBlock.get()))

        if selectNodeSet.get() == "Faces":
            nodeSETFaces(beginY_BEAM, widthBEAM, incrementY_BEAM, Nodeset.get())
        if selectNodeSet.get() == "Node Points":
            if selectEntity.get() == "Isection":
                nodeSETLoc(beginY_BEAM, widthBEAM, incrementY_BEAM, float(beamHeight.get()))
            if selectEntity.get() == "Block":
                nodeSETLoc(beginY_BEAM, widthBEAM, incrementY_BEAM, float(depthBlock.get()))

        fireModel(beginY_BEAM, widthBEAM, incrementY_BEAM, fireModelType.get())
        heatFlux(beginY_BEAM, widthBEAM, incrementY_BEAM, hfFaces.get(), modelHT_Tag.get())
        htRecorder(beginY_BEAM, widthBEAM, incrementY_BEAM)
        entBeam += 1

    global jEle, ELEMENT_SET_COL, ELEMENT_SET2, ELEMENT_SET_BEAM, ELEMENT_SET_Truss
    global onlySlabEle, onlySlabEle, onlyBeamEle, onlyTrussEle

    def eleDictionaryBC(getClass):
        global elementListBC
        setX = getClass  # calling functions(methods) from the class
        fullSet = set(setX)
        elementListBC = [key for key, value in bcEleDictionary.items()
                         if set(value).issubset(fullSet)]

    def eleDictionaryShell(getClass):  # this method generate the element list which is copied in ele_set_gen method
        global elementListShell
        setX = getClass  # calling functions(methods) from the class
        fullSet = set(setX)  # all nodes are changed into a set
        elementListShell = [key for key, value in shellEleDictionary.items()
                            if set(value).issubset(fullSet)]

    def ele_set_genBeamThermal(counter):
        with open(ELEMENT_SET2, 'a', newline='') as EleSet2:
            EleSet2.write("\n\n#This is ElementSet{0}\n".format(counter))
            for iItem in range(0, len(elementListBC), 1):  # step by threes.
                f = str(elementListBC[iItem:iItem + 1])[1:-1]  # it removes the square brackets
                EleSet2.write('\n eleLoad -ele {0} -type -beamThermal -source "temp{1}.dat" {2}'
                              .format(f, counter, sectionBC.get()))

    def ele_set_genShellThermal(counter):  # one line for each element
        with open(ELEMENT_SET2, 'a', newline='') as EleSet2:
            EleSet2.write("\n\n#This is ElementSet{0}\n".format(counter))
            for iItem in range(0, len(elementListShell), 1):  # step by threes.
                f = str(elementListShell[iItem:iItem + 1])[1:-1]  # it removes the square brackets
                EleSet2.write('\n eleLoad -ele {0} -type -shellThermal -source "temp{1}.dat" {2}'
                              .format(f, counter, sectionShell.get()))

    if incrementDirectionBEAM.get() == "Z":
        columnBegin = float(z_BeamLL.get())
        while columnBegin < float(z_LenBeam.get()):
            lowerZ = columnBegin
            upperZ = columnBegin + float(incZ_Beam.get())
            if elementType.get() == "BeamColumn":
                eleDictionaryBC(nodes1())
                ele_set_genBeamThermal(iEle)
            if elementType.get() == "Shell":
                eleDictionaryShell(nodes1())
                ele_set_genShellThermal(iEle)
            columnBegin += (float(incZ_Beam.get())+0.000001)
            Var5 = Decimal(columnBegin)
            Var6 = Decimal(Var5.quantize(Decimal('.001'), rounding=ROUND_HALF_EVEN))
            columnBegin = float(Var6)
            iEle += 1

    if incrementDirectionBEAM.get() == "X":
        beginXBeam = float(x_BeamLL.get())
        while beginXBeam <= float(x_LenBeam.get()):
            if elementType.get() == "BeamColumn":
                eleDictionaryBC(nodes2())
                ele_set_genBeamThermal(iEle)
            if elementType.get() == "Shell":
                eleDictionaryShell(nodes2())
                ele_set_genShellThermal(iEle)
            beginXBeam += (float(incX_Beam.get())+0.000001)
            Var = Decimal(beginXBeam)
            Var2 = Decimal(Var.quantize(Decimal('.001'), rounding=ROUND_HALF_EVEN))
            beginXBeam = float(Var2)
            #print(beginXBeam)
            jEle += 1
            iEle += 1

    if incrementDirectionBEAM.get() == "Y":
        global a1, a2, zL1, zL2
        beginYBeam = 0  # float(y_BeamLL.get())
        a1 = float(x_BeamLL.get())
        a2 = float(x_BeamUL.get())
        zL1 = float(z_BeamLL.get())
        zL2 = float(z_BeamUL.get())
        while beginYBeam < float(y_LenBeam.get()):
            if elementType.get() == "BeamColumn":
                eleDictionaryBC(nodes3())
                ele_set_genBeamThermal(iEle)
            if elementType.get() == "Shell":
                eleDictionaryShell(nodes3())
                ele_set_genShellThermal(iEle)
            beginYBeam += (float(incY_Beam.get())+0.000001)
            Var3 = Decimal(beginYBeam)
            Var4 = Decimal(Var3.quantize(Decimal('.001'), rounding=ROUND_HALF_EVEN))
            beginYBeam = float(Var4)
            jEle += 1
            iEle += 1


tk.Button(savingFrame, text="Save File", command=outputData, width=15, height=1).grid(row=0, column=0, padx=5, pady=5)

tk.Button(savingFrame, text="Save HT File", command=savingHTFile, width=10, height=1).grid(row=0, column=3)

window2.mainloop()

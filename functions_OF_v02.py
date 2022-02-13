"""Many functions are written in the Python script including the files names used in the program
Rev02: Many unnecessary file names are removed"""

try:
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import filedialog
except ImportError:
    import Tkinter as tk
    import ttk
    import tkFileDialog as filedialog

from decimal import *
from gui_OF_v02 import *


def createFolder(directory):  # creating folders in the directory
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating Directory.' + directory)


def addAnalysis():
    with open(osFile, 'a') as fileOS:
        fileOS.writelines("\nwipe;\n\n")
        if dimAnalysis.get() == "2D":
            fileOS.writelines("HeatTransfer 2D;\n\n")
        else:
            fileOS.writelines("HeatTransfer 3D;\n\n")


def addMaterial():  # adding materials
    with open(osFile, 'a') as fileOS:
        fileOS.writelines("HTMaterial {0} {1};\n\n".format(selectMat.get(), matTag.get()))


def addHTConstants():  # adding constants for convection and radiation
    with open(osFile, 'a') as fileOS:
        fileOS.writelines("HTConstants {0} {1};\n\n".format(htConstTag.get(), htConstants.get()))


fdsFile = 'fds.txt'  # file containing all FDS devices
fds_AST = 'fds_ast.txt'  # file containing FDS AST devices
fds_HF = 'ElementFiles/fds_hf.txt'  # file containing FDS heat flux devices
fds_HTC = 'ElementFiles/fds_htc.txt'  # file containing FDS HTC devices
fds_gas = 'ElementFiles/fds_gas.txt'  # file containing FDS HTC devices
osFile = 'OpenSees.txt'  # script file for OpenSEES HT
ELEMENT_SET2 = 'Elementset2.txt'  # element file containing boundary file names
Final_EleSET2 = 'Final_EleSet.txt'   # makes final file containing updated files

'''These are the increment counter for devices and entities'''
j = 1  # counter for FDS devices
j1 = 1  # counter for entities
j2 = 1  # counter for mesh
j3 = 1  # counter for node set
jNS = 1  # counter for new node set
j4 = 1  # counter for fire model
j5 = 1  # counter for heat flux
j6 = 1  # counter for recorder
j7 = 1  # counter for nodeset when User defined location is chosen
entCol = 1  # counter for entity of Z
entBeam = 1  # counter for entity of X
entTruss = 1  # counter for entity of  Y
iEle = 1  # counter for the BC elements
jEle = 1  # counter for shell elements, so used for slabs in OpenSEES

'''These functions are to make the devices for FDS script file'''


def fdsFileMaker(begin, final, increment, Cord1, Cord2, IOR):
    global j
    if incrementDirectionBEAM.get() == "Z":
        while begin < final:
            if units.get() == "m":
                devcLocCol = begin + round((float(incZ_Beam.get()) / 2), 2)
                with open(fds_AST, 'a') as f1:
                    f1.writelines("\n&DEVC ID = 'AST{0}', QUANTITY='ADIABATIC SURFACE TEMPERATURE', XYZ={1},{2},{3}, "
                                  "IOR={4}/".format(j, Cord1, Cord2, devcLocCol, IOR))
                with open(fds_HF, 'a') as f1:
                    f1.writelines("\n&DEVC ID = 'HF{0}', QUANTITY='GAUGE HEAT FLUX', XYZ={1},{2},{3}, "
                                  "IOR={4}/".format(j, Cord1, Cord2, devcLocCol, IOR))
                with open(fds_HTC, 'a') as f1:
                    f1.writelines("\n&DEVC ID = 'HTC{0}', QUANTITY='HEAT TRANSFER COEFFICIENT', XYZ={1},{2},{3}, "
                                  "IOR={4}/".format(j, Cord1, Cord2, devcLocCol, IOR))
                with open(fds_gas, 'a') as f1:
                    f1.writelines("\n&DEVC ID = 'GAS{0}', QUANTITY='TEMPERATURE', "
                                  "XYZ={1},{2},{3}/".format(j, Cord1, Cord2, devcLocCol))

            if units.get() == "mm":
                devcLocCol = begin/1000 + round((float(incZ_Beam.get()) / 2000), 2)
                with open(fds_AST, 'a') as f1:
                    f1.writelines("\n&DEVC ID = 'AST{0}', QUANTITY='ADIABATIC SURFACE TEMPERATURE', XYZ={1},{2},{3}, "
                                  "IOR={4}/".format(j, Cord1, Cord2, devcLocCol, IOR))
                with open(fds_HF, 'a') as f1:
                    f1.writelines("\n&DEVC ID = 'HF{0}', QUANTITY='GAUGE HEAT FLUX', XYZ={1},{2},{3}, "
                                  "IOR={4}/".format(j, Cord1, Cord2, devcLocCol, IOR))
                with open(fds_HTC, 'a') as f1:
                    f1.writelines("\n&DEVC ID = 'HTC{0}', QUANTITY='HEAT TRANSFER COEFFICIENT', XYZ={1},{2},{3}, "
                                  "IOR={4}/".format(j, Cord1, Cord2, devcLocCol, IOR))
                with open(fds_gas, 'a') as f1:
                    f1.writelines("\n&DEVC ID = 'GAS{0}', QUANTITY='TEMPERATURE', "
                                  "XYZ={1},{2},{3}/".format(j, Cord1, Cord2, devcLocCol))
            j += 1
            begin += increment
            begin = round(float(begin), 2)

    if incrementDirectionBEAM.get() == "X":
        while begin < final:
            if units.get() == "m":
                devcLocTruss = begin + round((float(incX_Beam.get()) / 2),)
                with open(fds_AST, 'a') as f1:
                    f1.writelines("\n&DEVC ID = 'AST{0}', QUANTITY='ADIABATIC SURFACE TEMPERATURE', {1},{2},{3}, "
                                  "IOR={4}/".format(j, devcLocTruss, Cord1, Cord2, IOR))
                with open(fds_HF, 'a') as f1:
                    f1.writelines("\n&DEVC ID = 'HF{0}', QUANTITY='GAUGE HEAT FLUX', {1},{2},{3}, "
                                  "IOR={4}/".format(j, devcLocTruss, Cord1, Cord2, IOR))
                with open(fds_HTC, 'a') as f1:
                    f1.writelines("\n&DEVC ID = 'HTC{0}', QUANTITY='HEAT TRANSFER COEFFICIENT', {1},{2},{3}, "
                                  "IOR={4}/".format(j, devcLocTruss, Cord1, Cord2, IOR))
                with open(fds_gas, 'a') as f1:
                    f1.writelines("\n&DEVC ID = 'GAS{0}', QUANTITY='TEMPERATURE', "
                                  "{1},{2},{3}/".format(j, devcLocTruss, Cord1, Cord2))
            if units.get() == "mm":
                devcLocTruss = begin/1000 + round((float(incX_Beam.get()) / 2000), 2)
                with open(fds_AST, 'a') as f1:
                    f1.writelines("\n&DEVC ID = 'AST{0}', QUANTITY='ADIABATIC SURFACE TEMPERATURE', {1},{2},{3}, "
                                  "IOR={4}/".format(j, devcLocTruss, Cord1, Cord2, IOR))
                with open(fds_HF, 'a') as f1:
                    f1.writelines("\n&DEVC ID = 'HF{0}', QUANTITY='GAUGE HEAT FLUX', {1},{2},{3}, "
                                  "IOR={4}/".format(j, devcLocTruss, Cord1, Cord2, IOR))
                with open(fds_HTC, 'a') as f1:
                    f1.writelines("\n&DEVC ID = 'HTC{0}', QUANTITY='HEAT TRANSFER COEFFICIENT', {1},{2},{3}, "
                                  "IOR={4}/".format(j, devcLocTruss, Cord1, Cord2, IOR))
                with open(fds_gas, 'a') as f1:
                    f1.writelines("\n&DEVC ID = 'GAS{0}', QUANTITY='TEMPERATURE', "
                                  "{1},{2},{3}/".format(j, devcLocTruss, Cord1, Cord2))
            j += 1
            begin += increment
            begin = round(float(begin), 2)

    if incrementDirectionBEAM.get() == "Y":
        while begin < final:
            if units.get() == "m":
                devcLocTrussY = begin + round((float(incY_Beam.get()) / 2), 2)
                with open(fds_AST, 'a') as f1:
                    f1.writelines("\n&DEVC ID = 'AST{0}', QUANTITY='ADIABATIC SURFACE TEMPERATURE', {1},{2},{3}, "
                                  "IOR={4}/".format(j, Cord1, devcLocTrussY, Cord2, IOR))
                with open(fds_HF, 'a') as f1:
                    f1.writelines("\n&DEVC ID = 'HF{0}', QUANTITY='GAUGE HEAT FLUX', {1},{2},{3},  "
                                  "IOR={4}/".format(j, Cord1, devcLocTrussY, Cord2, IOR))
                with open(fds_HTC, 'a') as f1:
                    f1.writelines("\n&DEVC ID = 'HTC{0}', QUANTITY='HEAT TRANSFER COEFFICIENT', {1},{2},{3}, "
                                  "IOR={4}/".format(j, Cord1, devcLocTrussY, Cord2, IOR))
                with open(fds_gas, 'a') as f1:
                    f1.writelines("\n&DEVC ID = 'GAS{0}', QUANTITY='TEMPERATURE', "
                                  "{1},{2},{3}/".format(j, Cord1, devcLocTrussY, Cord2))
            if units.get() == "mm":
                devcLocTrussY = begin/1000 + round((float(incY_Beam.get()) / 2000), 2)
                with open(fds_AST, 'a') as f1:
                    f1.writelines("\n&DEVC ID = 'AST{0}', QUANTITY='ADIABATIC SURFACE TEMPERATURE', {1},{2},{3}, "
                                  "IOR={4}/".format(j, Cord1, devcLocTrussY, Cord2, IOR))
                with open(fds_HF, 'a') as f1:
                    f1.writelines("\n&DEVC ID = 'HF{0}', QUANTITY='GAUGE HEAT FLUX', {1},{2},{3},  "
                                  "IOR={4}/".format(j, Cord1, devcLocTrussY, Cord2, IOR))
                with open(fds_HTC, 'a') as f1:
                    f1.writelines("\n&DEVC ID = 'HTC{0}', QUANTITY='HEAT TRANSFER COEFFICIENT', {1},{2},{3}, "
                                  "IOR={4}/".format(j, Cord1, devcLocTrussY, Cord2, IOR))
                with open(fds_gas, 'a') as f1:
                    f1.writelines("\n&DEVC ID = 'GAS{0}', QUANTITY='TEMPERATURE', "
                                  "{1},{2},{3}/".format(j, Cord1, devcLocTrussY, Cord2))
            j += 1
            begin += increment
            begin = round(float(begin), 2)

##############################---Functions for entities

def iEntity(intValue, maxL, increment, centroidX, centroidY, flangeWid, flangeHeight, webThick, flangeThick):
    global j1
    while intValue < maxL:  # entities
        with open(osFile, 'a') as fileOS:
            fileOS.writelines("HTEntity \t Isection \t {0}   \t {1} \t {2} \t {3} \t {4} \t {5} "
                              "\t {6};\n".format(j1, centroidX, centroidY, flangeWid, flangeHeight, webThick,
                                                 flangeThick))
            j1 += 1
            intValue += increment
    with open(osFile, 'a') as fileOS:
        fileOS.writelines("\n")


def mesh(intValue2, maxL2, increment2, phaseChange, meshFlangeW, meshFlangeT, meshWebT, meshWidth, materialTag):
    global j2
    while intValue2 < maxL2:  # creating mesh
        with open(osFile, 'a') as fileOS:
            fileOS.writelines("HTMesh \t {0}  \t {0}  \t {6} \t -phaseChange \t {1} \t -MeshCtrls \t {2} \t {3} \t "
                              "{4} \t {5}\n".format(j2, phaseChange, meshFlangeW, meshFlangeT, meshWebT,
                                                    meshWidth, materialTag))
            j2 += 1
            intValue2 += increment2
    with open(osFile, 'a') as fileOS:
        fileOS.writelines("\nHTMeshAll;\n\n")


def nodeSETFaces(intValue3, maxL3, increment3, faces):
    global j3
    while intValue3 < maxL3:  # creating Node Set
        with open(osFile, 'a') as fileOS:
            fileOS.writelines("HTNodeSet \t {0}  \t -Entity \t {0}  \t -face \t {1}\n".format(j3, faces))
        j3 += 1
        intValue3 += increment3

    with open(osFile, 'a') as fileOS:
        fileOS.writelines("\n")


def nodeSETLoc(intValue3, maxL3, increment3, entityDepth):
    global j3
    global j7, jNS
    while intValue3 < maxL3:  # creating Node Set
        with open(osFile, 'a') as fileOS:
            webH = round(float(beamHeight.get()) - 2*float(flangeThickness.get()), 4)
            div1 = round((webH/4), 4)
            div2 = round(3*(webH/8), 4)
            div3 = round((webH/4), 4)
            div4 = round((webH/8), 4)
            if deptLocation.get() == "2":
                fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {2} \t -Locx 0.0  \t"
                                  " -Locy -{1}\n".format(j3, entityDepth/2, j7))
                j3 += 1
                fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {2} \t -Locx 0.0  \t"
                                  " -Locy {1}\n".format(j3, entityDepth/2, j7))
                j3 += 1
                fileOS.writelines("HTNodeSet \t {0} \t -NodeSet {1} {2}\n".format(j3, j3-2, j3-1))

            if selectEntity.get() == "Isection":
                if deptLocation.get() == "5":
                    fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {2} \t -Locx 0.0  \t"
                                      " -Locy -{1}\n".format(j3, entityDepth/2, j7))
                    j3 += 1
                    fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {2} \t -Locx 0.0  \t"
                                      " -Locy -{1}\n".format(j3, div1, j7))
                    j3 += 1
                    fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {1} \t -Locx 0.0  \t -Locy 0.0\n".format(j3, j7))
                    j3 += 1
                    fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {2} \t -Locx 0.0  \t"
                                      " -Locy {1}\n".format(j3, div1, j7))
                    j3 += 1
                    fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {2} \t -Locx 0.0  \t"
                                      " -Locy {1}\n".format(j3, entityDepth/2, j7))

                    j3 += 1
                    fileOS.writelines("HTNodeSet \t {0} \t -NodeSet {1} {2} {3} {4} "
                                      "{5}\n".format(j3, j3-5, j3-4, j3-3, j3-2, j3-1))

                if deptLocation.get() == "9":
                    fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {2} \t -Locx 0.0  \t"
                                      " -Locy -{1}\n".format(j3, entityDepth/2, j7))
                    j3 += 1
                    fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {2} \t -Locx 0.0  \t"
                                      " -Locy -{1}\n".format(j3, div2, j7))
                    j3 += 1
                    fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {2} \t -Locx 0.0  \t"
                                      " -Locy -{1}\n".format(j3, div3, j7))
                    j3 += 1
                    fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {2} \t -Locx 0.0  \t"
                                      " -Locy -{1}\n".format(j3, div4, j7))
                    j3 += 1
                    fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {1} \t -Locx 0.0  \t -Locy 0.0\n".format(j3, j7))
                    j3 += 1
                    fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {2} \t -Locx 0.0  \t"
                                      " -Locy {1}\n".format(j3, div4, j7))
                    j3 += 1
                    fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {2} \t -Locx 0.0  \t"
                                      " -Locy {1}\n".format(j3, div3, j7))
                    j3 += 1
                    fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {2} \t -Locx 0.0  \t"
                                      " -Locy {1}\n".format(j3, div2, j7))
                    j3 += 1
                    fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {2} \t -Locx 0.0  \t "
                                      "-Locy {1}\n".format(j3, entityDepth/2, j7))
                    j3 += 1
                    fileOS.writelines("HTNodeSet \t {0} \t -NodeSet {1} {2} {3} {4} {5} {6} {7} {8} "
                                      "{9}\n".format(j3, j3-9, j3-8, j3-7, j6-6, j3-5, j3-4, j3-3, j3-2, j3-1))

            if selectEntity.get() == "Block":
                if deptLocation.get() == "5":
                    fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {2} \t -Locx 0.0  \t"
                                      " -Locy -{1}\n".format(j3, round(entityDepth/2, 3), j7))
                    j3 += 1
                    fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {2} \t -Locx 0.0  \t"
                                      " -Locy -{1}\n".format(j3, round(entityDepth/4, 3), j7))
                    j3 += 1
                    fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {1} \t -Locx 0.0  \t -Locy 0.0\n".format(j3, j7))
                    j3 += 1
                    fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {2} \t -Locx 0.0  \t"
                                      " -Locy {1}\n".format(j3, round(entityDepth/4, 3), j7))
                    j3 += 1
                    fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {2} \t -Locx 0.0  \t"
                                      " -Locy {1}\n".format(j3, round(entityDepth/2, 3), j7))
                    j3 += 1
                    fileOS.writelines("HTNodeSet \t {0} \t -NodeSet {1} {2} {3} {4} "
                                      "{5}\n".format(j3, j3-5, j3-4, j3-3, j3-2, j3-1))

            if deptLocation.get() == "9":
                fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {2} \t -Locx 0.0  \t"
                                  " -Locy -{1}\n".format(j3, round(entityDepth/2, 3), j7))
                j3 += 1
                fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {2} \t -Locx 0.0  \t"
                                  " -Locy -{1}\n".format(j3, round(3*entityDepth/8, 3), j7))
                j3 += 1
                fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {2} \t -Locx 0.0  \t"
                                  " -Locy -{1}\n".format(j3, round(entityDepth/4, 3), j7))
                j3 += 1
                fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {2} \t -Locx 0.0  \t"
                                  " -Locy -{1}\n".format(j3, round(entityDepth/8, 3), j7))
                j3 += 1
                fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {1} \t -Locx 0.0  \t -Locy 0.0\n".format(j3, j7))
                j3 += 1
                fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {2} \t -Locx 0.0  \t"
                                  " -Locy {1}\n".format(j3, round(entityDepth/8, 3), j7))
                j3 += 1
                fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {2} \t -Locx 0.0  \t"
                                  " -Locy {1}\n".format(j3, round(entityDepth/4, 3), j7))
                j3 += 1
                fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {2} \t -Locx 0.0  \t"
                                  " -Locy {1}\n".format(j3, round(3*entityDepth/8), j7))
                j3 += 1
                fileOS.writelines("HTNodeSet \t {0} \t -HTEntity {2} \t -Locx 0.0  \t "
                                  "-Locy {1}\n".format(j3, round(entityDepth/2, 3), j7))

                j3 += 1
                fileOS.writelines("HTNodeSet \t {0} \t -NodeSet {1} {2} {3} {4} {5} {6} {7} {8} "
                                  "{9}\n".format(j3, j3-9, j3-8, j3-7, j3-6, j3-5, j3-4, j3-3, j3-2, j3-1))

            j3 += 1
        j7 += 1
        intValue3 += increment3


    with open(osFile, 'a') as fileOS:
        fileOS.writelines("\n")


def fireModel(intValue4, maxL4, increment4, fireType):
    global j4
    while intValue4 < maxL4:  # creating Fire Model
        with open(osFile, 'a') as fileOS:
            fileOS.writelines(
                "FireModel \t UserDefined \t {0}  \t -file \t AST{0}.dat -type {1};\n".format(j4, fireType))
            j4 += 1
            intValue4 += increment4
    with open(osFile, 'a') as fileOS:
        fileOS.writelines("\n")


def heatFlux(intValue5, maxL5, increment5, HFfaces, HTConstants):
    global j5
    while intValue5 < maxL5:  # creating Heat Flux  ### check this part carefully in OpenSEES File
        with open(osFile, 'a') as fileOS:
            fileOS.writelines("HTPattern \t fire \t {0}  \t model \t {0}  {{\nHeatFluxBC \t -HTEntity \t {0}"
                              "  \t -face {1} \t -type \t ConvecAndRad \t -HTConstants {2};\n}}\n"
                              .format(j5, HFfaces, HTConstants))
            j5 += 1
            intValue5 += increment5
    with open(osFile, 'a') as fileOS:
        fileOS.writelines("\n")


def htRecorder(intValue6, maxL6, increment6):
    global j6, jNS
    while intValue6 < maxL6:  # creating recorder
        with open(osFile, 'a') as fileOS:
            if selectNodeSet.get() == "Faces":
                fileOS.writelines("HTRecorder \t -file \t temp{0}.dat  \t -NodeSet \t {0};\n".format(j6))
            if selectNodeSet.get() == "Node Points":
                if deptLocation.get() == "2":
                    jNS = jNS + 2
                    fileOS.writelines("HTRecorder \t -file \t temp{0}.dat  \t -NodeSet \t {1};\n".format(j6, jNS))
                if deptLocation.get() == "5":
                    jNS = jNS + 5
                    fileOS.writelines("HTRecorder \t -file \t temp{0}.dat  \t -NodeSet \t {1};\n".format(j6, jNS))
                if deptLocation.get() == "9":
                    jNS = jNS + 9
                    fileOS.writelines("HTRecorder \t -file \t temp{0}.dat  \t -NodeSet \t {1};\n".format(j6, jNS))
        j6 += 1
        jNS += 1
        intValue6 += increment6


''' Below functions is for block entity, the Tag number will continue with '''


def blockEntity(intValue7, maxL7, increment7, blkCentroidX, blkCentroidY, widthBLK, depthBLK):
    global j1
    while intValue7 < maxL7:  # entities
        with open(osFile, 'a') as fileOS:
            fileOS.writelines("HTEntity \t Block \t {0}   \t {1} \t {2} \t {3} "
                              "\t {4};\n".format(j1, blkCentroidX, blkCentroidY, widthBLK, depthBLK))
            j1 += 1
            intValue7 += increment7
    with open(osFile, 'a') as fileOS:
        fileOS.writelines("\n")


def meshBLK(intValue8, maxL8, increment8, material2, phaseChange2, meshWBLK, meshDepth):
    global j2
    while intValue8 < maxL8:  # creating mesh
        with open(osFile, 'a') as fileOS:
            fileOS.writelines("HTMesh \t {0}  \t {0}  \t {1} \t -phaseChange \t {2} \t -MeshCtrls \t {3} \t {4};\n"
                              .format(j2, material2, phaseChange2, meshWBLK, meshDepth))
            j2 += 1
            intValue8 += increment8
    with open(osFile, 'a') as fileOS:
        fileOS.writelines("\nHTMeshAll;\n\n")

######################--- Defining HT Analysis

def savingHTFile():  # it allows the user to proceed the chooses module
    with open(osFile, 'a') as fileOS:
        fileOS.writelines("\nSetInitialT {};\n".format(initialTemp.get()))
        fileOS.writelines("\nHTAnalysis HeatTransfer TempIncr 0.1 1000 2 Newton\n")
        fileOS.writelines("HTAnalyze {0} {1};\n".format(simTime.get(), simTimeStep.get()))
        fileOS.writelines("wipe;\n\n")

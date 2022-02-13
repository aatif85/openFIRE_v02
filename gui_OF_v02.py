"""Rev03: In this revision tabs are added """

try:
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import filedialog
except ImportError:
    import Tkinter as tk
    import ttk
    import tkFileDialog as filedialog
import os
from PIL import ImageTk, Image


def location():  # Directory Location
    get = filedialog.askdirectory()
    os.chdir(get)


window2 = tk.Tk()    # main Window
window2.title("Devices, Entities & Element Sets")
window2.geometry("780x580")

# this is the notebook for making tabs
dvc_Ele_notebook = ttk.Notebook(window2)
dvc_Ele_notebook.pack()

# adding tabs
general = tk.Frame(dvc_Ele_notebook, width=500, height=500, bg="light grey")
OpenSEES = tk.Frame(dvc_Ele_notebook, width=500, height=500, bg="light grey")
Entities = tk.Frame(dvc_Ele_notebook, width=400, height=400, bg="light grey")

general.pack(fill="both", expand=1)
OpenSEES.pack(fill="both", expand=1)
Entities.pack(fill="both", expand=0.8)

dvc_Ele_notebook.add(general, text="General")
dvc_Ele_notebook.add(OpenSEES, text="OpenSEES")
dvc_Ele_notebook.add(Entities, text="Entities")

# this is a frame for the entries of files and options for the user to chose the devices
general_inputs = tk.LabelFrame(general, text="Basic Inputs", padx=5, pady=5)
general_inputs.grid(row=0, column=0, sticky="nsew")

tk.Button(general_inputs, text="Directory", command=location, width=10, height=1).grid(row=0, column=1, padx=10, pady=10)
tk.Label(general_inputs, width=15, text="Get Working Directory", anchor='e').grid(row=0, column=0, padx=5, pady=5)

entityType = ["Isection", "Block", "Brick"]
selectEntity = tk.StringVar()  # it was clickedEnt
selectEntity.set(entityType[0])  # use variables as list
EntityDrop = tk.OptionMenu(general_inputs, selectEntity, *entityType)
EntityDrop.config(width=5)
EntityDrop.grid(row=1, column=1, padx=5, pady=5)
tk.Label(general_inputs, width=15, text="Section Entity", anchor='e').grid(row=1, column=0, padx=5, pady=5)

units = tk.StringVar()
units.set("m")
unitsOption = tk.OptionMenu(general_inputs, units, "m", "mm")
unitsOption.config(width=5)
unitsOption.grid(row=0, column=3, padx=5, pady=5)
tk.Label(general_inputs, width=10, text="Units", anchor='e').grid(row=0, column=2, padx=5, pady=5)

dimAnalysis = tk.StringVar()  # to chose if entities to be created
dimAnalysis.set("2D")
dimOption = tk.OptionMenu(general_inputs, dimAnalysis, "2D", "3D")
dimOption.config(width=5)
dimOption.grid(row=1, column=3, padx=5, pady=5)
tk.Label(general_inputs, width=15, text="HT Analysis", anchor='e').grid(row=1, column=2, padx=5, pady=5)

# OpenSees entries

OSFrame = tk.LabelFrame(OpenSEES, text="OpenSEES Inputs", padx=5, pady=5)   # it was OSFrame
OSFrame.grid(row=0, column=0, sticky="nsew")

materialSelect = ["CarbonSteelEC3", "ConcreteEC2"]
selectMat = tk.StringVar()
selectMat.set(materialSelect[1])  # use variables as list
matDrop = tk.OptionMenu(OSFrame, selectMat, *materialSelect)
matDrop.config(width=10)
matDrop.grid(row=2, column=1, padx=5, pady=5)
tk.Label(OSFrame, width=10, text="Material", anchor='e').grid(row=2, column=0, padx=5, pady=5)

matTag = tk.Entry(OSFrame, width=5)
matTag.grid(row=2, column=3)
matTag.insert(tk.END, "1")
tk.Label(OSFrame, width=10, text="Material Tag", anchor='e').grid(row=2, column=2)

htConstants = tk.Entry(OSFrame, width=10)
htConstants.grid(row=3, column=1)
htConstants.insert(tk.END, "25 293.15 0.85 0.85")
tk.Label(OSFrame, width=10, text="HT Constants", anchor='e').grid(row=3, column=0)

htConstTag = tk.Entry(OSFrame, width=5)
htConstTag.grid(row=3, column=3)
htConstTag.insert(tk.END, "2")
tk.Label(OSFrame, width=10, text="HT Const. Tag", anchor='e').grid(row=3, column=2)

pChange = tk.Entry(OSFrame, width=10)
pChange.grid(row=4, column=1)
pChange.insert(tk.END, "0")
tk.Label(OSFrame, width=10, text="Phase Change", anchor='e').grid(row=4, column=0)

fireModelType = tk.Entry(OSFrame, width=5)   # it was fModel
fireModelType.grid(row=4, column=3)
fireModelType.insert(tk.END, "1")
tk.Label(OSFrame, width=10, text="Fire Model", anchor='e').grid(row=4, column=2)

hfFaces = tk.Entry(OSFrame, width=10)    # it was hffaces
hfFaces.grid(row=5, column=1)
hfFaces.insert(tk.END, "1 5 7 9")
tk.Label(OSFrame, width=12, text="Heat Flux (Face)", anchor='e').grid(row=5, column=0)

modelHT_Tag = tk.Entry(OSFrame, width=10)   # it was htConst
modelHT_Tag.grid(row=6, column=1)
modelHT_Tag.insert(tk.END, "1")
tk.Label(OSFrame, width=16, text="Model HT Const. Tag", anchor='e').grid(row=6, column=0)

modelMatTag = tk.Entry(OSFrame, width=5)  # it was matT
modelMatTag.grid(row=5, column=3)
modelMatTag.insert(tk.END, "1")
tk.Label(OSFrame, width=15, text="Section Material Tag", anchor='e').grid(row=5, column=2)

nodeSetType = ["Faces", "Node Points"]
selectNodeSet = tk.StringVar()                 # this was clickedNS
selectNodeSet.set(nodeSetType[0])  # use variables as list
NS_Drop = tk.OptionMenu(OSFrame, selectNodeSet, *nodeSetType)
NS_Drop.config(width=5)
NS_Drop.grid(row=6, column=3, padx=5, pady=5)
tk.Label(OSFrame, width=15, text="Node Sets Location", anchor='e').grid(row=6, column=2, padx=5, pady=5)

Nodeset = tk.Entry(OSFrame, width=10)   # it was fNodeset
Nodeset.grid(row=7, column=1)
Nodeset.insert(tk.END, "1 4 5")
tk.Label(OSFrame, width=15, text="Node Sets Faces", anchor='e').grid(row=7, column=0, padx=5, pady=5)

locDepth = ["2", "5", "9"]
deptLocation = tk.StringVar()                 # this was clickedNS
deptLocation.set(locDepth[1])  # use variables as list
loc_Drop = tk.OptionMenu(OSFrame, deptLocation, *locDepth)
loc_Drop.config(width=5)
loc_Drop.grid(row=7, column=3, padx=5, pady=5)
tk.Label(OSFrame, width=15, text="Number of Points", anchor='e').grid(row=7, column=2, padx=3, pady=5)

initialTemp = tk.Entry(OSFrame, width=5)
initialTemp.grid(row=8, column=1)
initialTemp.insert(tk.END, "293.15")
tk.Label(OSFrame, width=15, text="Initial Temperature", anchor='e').grid(row=8, column=0)

simTime = tk.Entry(OSFrame, width=5)
simTime.grid(row=8, column=3)
simTime.insert(tk.END, "200")
tk.Label(OSFrame, width=12, text="Simulation Time", anchor='e').grid(row=8, column=2)

simTimeStep = tk.Entry(OSFrame, width=5)
simTimeStep.grid(row=9, column=1)
simTimeStep.insert(tk.END, "15")
tk.Label(OSFrame, width=10, text="Time Step", anchor='e').grid(row=9, column=0)

#####################################------Entries for Structural Components-----#############################

beamFrame = tk.LabelFrame(general, text="Structural Components", padx=5, pady=5)
beamFrame.grid(row=1, column=0, sticky="nsew")

directionLengthBEAM = ["X", "Y", "Z"]
incrementDirectionBEAM = tk.StringVar()  # it was clickedEnt
incrementDirectionBEAM.set(directionLengthBEAM[0])  # use variables as list
incrementBeamDrop = tk.OptionMenu(beamFrame, incrementDirectionBEAM, *directionLengthBEAM)
incrementBeamDrop.config(width=5)
incrementBeamDrop.grid(row=0, column=1, padx=5, pady=5)
tk.Label(beamFrame, width=15, text="Initial Inc. Dir.", anchor='e').grid(row=0, column=0)

elementTypes = ["BeamColumn", "Shell"]
elementType = tk.StringVar()  # it was clickedEnt
elementType.set(elementTypes[1])  # use variables as list
elementTypeDrop = tk.OptionMenu(beamFrame, elementType, *elementTypes)
elementTypeDrop.config(width=5)
elementTypeDrop.grid(row=0, column=3, padx=5, pady=5)
tk.Label(beamFrame, width=15, text="Element Types.", anchor='e').grid(row=0, column=2)

ior_Beam = tk.Entry(beamFrame, width=5)
ior_Beam.grid(row=0, column=5)
ior_Beam.insert(tk.END, "-3")
tk.Label(beamFrame, width=15, text="Orientation", anchor='e').grid(row=0, column=4)

x_BeamLL = tk.Entry(beamFrame, width=5)
x_BeamLL.grid(row=1, column=1)
x_BeamLL.insert(tk.END, "0")
tk.Label(beamFrame, width=15, text="Lower Limit of X", anchor='e').grid(row=1, column=0)

x_BeamUL = tk.Entry(beamFrame, width=5)
x_BeamUL.grid(row=1, column=3)
x_BeamUL.insert(tk.END, "0")
tk.Label(beamFrame, width=15, text="Upper Limit of X", anchor='e').grid(row=1, column=2)

x_LenBeam = tk.Entry(beamFrame, width=5)
x_LenBeam.grid(row=1, column=5)
x_LenBeam.insert(tk.END, "36.5")
tk.Label(beamFrame, width=15, text="Length in X", anchor='e').grid(row=1, column=4)

y_BeamLL = tk.Entry(beamFrame, width=5)
y_BeamLL.grid(row=2, column=1)
y_BeamLL.insert(tk.END, "2.3")
tk.Label(beamFrame, width=15, text="Lower Limit of Y", anchor='e').grid(row=2, column=0)

y_BeamUL = tk.Entry(beamFrame, width=5)
y_BeamUL.grid(row=2, column=3)
y_BeamUL.insert(tk.END, "3.7")
tk.Label(beamFrame, width=15, text="Upper Limit of Y", anchor='e').grid(row=2, column=2)

y_LenBeam = tk.Entry(beamFrame, width=5)
y_LenBeam.grid(row=2, column=5)
y_LenBeam.insert(tk.END, "0")
tk.Label(beamFrame, width=15, text="Length in Y", anchor='e').grid(row=2, column=4)

z_BeamLL = tk.Entry(beamFrame, width=5)
z_BeamLL.grid(row=3, column=1)
z_BeamLL.insert(tk.END, "-1")
tk.Label(beamFrame, width=15, text="Lower Limit of Z", anchor='e').grid(row=3, column=0)

z_BeamUL = tk.Entry(beamFrame, width=5)
z_BeamUL.grid(row=3, column=3)
z_BeamUL.insert(tk.END, "1")
tk.Label(beamFrame, width=15, text="Upper Limit of Z", anchor='e').grid(row=3, column=2)

z_LenBeam = tk.Entry(beamFrame, width=5)
z_LenBeam.grid(row=3, column=5)
z_LenBeam.insert(tk.END, "0")
tk.Label(beamFrame, width=15, text="Length in Z", anchor='e').grid(row=3, column=4)

incX_Beam = tk.Entry(beamFrame, width=5)
incX_Beam.grid(row=4, column=1)
incX_Beam.insert(tk.END, "1.55")
tk.Label(beamFrame, width=15, text="Increment in X", anchor='e').grid(row=4, column=0)

incY_Beam = tk.Entry(beamFrame, width=5)
incY_Beam.grid(row=4, column=3)
incY_Beam.insert(tk.END, "2500")
tk.Label(beamFrame, width=15, text="Increment in Y", anchor='e').grid(row=4, column=2)

incZ_Beam = tk.Entry(beamFrame, width=5)
incZ_Beam.grid(row=4, column=5)
incZ_Beam.insert(tk.END, "0")
tk.Label(beamFrame, width=15, text="Increment in Z", anchor='e').grid(row=4, column=4)


#####################--- frames and Entries for Element Sets

elementFrame = tk.LabelFrame(general, text="Element Sets", padx=5, pady=5)
elementFrame.grid(row=3, column=0, sticky="nsew")

sectionBC = tk.Entry(elementFrame, width=10)
sectionBC.grid(row=3, column=1)
sectionBC.insert(tk.END, "$c1 $c2 $c3")
tk.Label(elementFrame, width=15, text="Section BC", anchor='e').grid(row=3, column=0)

sectionShell = tk.Entry(elementFrame, width=10)
sectionShell.grid(row=3, column=3)
sectionShell.insert(tk.END, "$s1 $s2 $s3")
tk.Label(elementFrame, width=15, text="Section Shell", anchor='e').grid(row=3, column=2)

################################################------OpenSEES File Entries-------#####################################
##### I section Entries

iSectionFrame = tk.LabelFrame(Entities, text="I Section Entities", padx=5, pady=5)
iSectionFrame.grid(row=1, column=0, sticky="nsew")

iSectionImageFrame = tk.LabelFrame(Entities,text="I Section", padx=5, pady=5)
iSectionImageFrame.grid(row=1, column=1, sticky="nsew")
iSection_image = Image.open("isection.png")
resize_iSection_image = iSection_image.resize((300, 220))
iSection_img = ImageTk.PhotoImage(resize_iSection_image)
tk.Label(iSectionImageFrame, image=iSection_img).grid(row=0, column=0)

blockImageFrame = tk.LabelFrame(Entities, text="Block", padx=5, pady=5)
blockImageFrame.grid(row=0, column=1, sticky="nsew")
block_image = Image.open("block.png")
resize_Block_image = block_image.resize((300, 150))
block_img = ImageTk.PhotoImage(resize_Block_image)
tk.Label(blockImageFrame, image=block_img).grid(row=0, column=0)

brickImageFrame = tk.LabelFrame(Entities,text="Brick", padx=5, pady=5)
brickImageFrame.grid(row=2, column=1, sticky="nsew")
brick_image = Image.open("brick.png")
resize_brick_image = brick_image.resize((300, 200))
brick_img = ImageTk.PhotoImage(resize_brick_image)
tk.Label(brickImageFrame, image=brick_img).grid(row=0, column=0)

cX_iSec = tk.Entry(iSectionFrame, width=5)
cX_iSec.grid(row=0, column=1)
cX_iSec.insert(tk.END, "0")
tk.Label(iSectionFrame, width=20, text="Centroid of X", anchor='e').grid(row=0, column=0)

cY_iSec = tk.Entry(iSectionFrame, width=5)
cY_iSec.grid(row=0, column=3)
cY_iSec.insert(tk.END, "0")
tk.Label(iSectionFrame, width=20, text="Centroid of Y", anchor='e').grid(row=0, column=2)

flangeWidth = tk.Entry(iSectionFrame, width=5)
flangeWidth.grid(row=1, column=1)
flangeWidth.insert(tk.END, "0.4")
tk.Label(iSectionFrame, width=20, text="Width of Flange", anchor='e').grid(row=1, column=0)

beamHeight = tk.Entry(iSectionFrame, width=5)
beamHeight.grid(row=1, column=3)
beamHeight.insert(tk.END, "0.4")
tk.Label(iSectionFrame, width=20, text="Height of Beam", anchor='e').grid(row=1, column=2)

webThickness = tk.Entry(iSectionFrame, width=5)
webThickness.grid(row=2, column=1)
webThickness.insert(tk.END, "0.008")
tk.Label(iSectionFrame, width=20, text="Web Thickness", anchor='e').grid(row=2, column=0)

flangeThickness = tk.Entry(iSectionFrame, width=5)
flangeThickness.grid(row=2, column=3)
flangeThickness.insert(tk.END, "0.01")
tk.Label(iSectionFrame, width=20, text="Flange Thickness", anchor='e').grid(row=2, column=2)

meshFlangeWidth = tk.Entry(iSectionFrame, width=5)
meshFlangeWidth.grid(row=3, column=1)
meshFlangeWidth.insert(tk.END, "0.04")
tk.Label(iSectionFrame, width=20, text="Mesh flange width", anchor='e').grid(row=3, column=0)

meshFlangeThickness = tk.Entry(iSectionFrame, width=5)
meshFlangeThickness.grid(row=3, column=3)
meshFlangeThickness.insert(tk.END, "0.002")
tk.Label(iSectionFrame, width=20, text="Mesh flange thickness", anchor='e').grid(row=3, column=2)

meshWebThickness = tk.Entry(iSectionFrame, width=5)
meshWebThickness.grid(row=4, column=1)
meshWebThickness.insert(tk.END, "0.002")
tk.Label(iSectionFrame, width=20, text="Mesh web thickness", anchor='e').grid(row=4, column=0)

meshWebHeight = tk.Entry(iSectionFrame, width=5)
meshWebHeight.grid(row=4, column=3)
meshWebHeight.insert(tk.END, "0.04")
tk.Label(iSectionFrame, width=20, text="Mesh web height", anchor='e').grid(row=4, column=2)

##### Block Entries

blockFrame = tk.LabelFrame(Entities, text="Block Entities", padx=5, pady=5)
blockFrame.grid(row=0, column=0, sticky="nsew")

cX_Block = tk.Entry(blockFrame, width=5)
cX_Block.grid(row=1, column=1)
cX_Block.insert(tk.END, "0")
tk.Label(blockFrame, width=20, text="Centroid of X", anchor='e').grid(row=1, column=0)

cY_Block = tk.Entry(blockFrame, width=5)
cY_Block.grid(row=1, column=3)
cY_Block.insert(tk.END, "0")
tk.Label(blockFrame, width=20, text="Centroid of Y", anchor='e').grid(row=1, column=2)

widthBlock = tk.Entry(blockFrame, width=5)
widthBlock.grid(row=2, column=1)
widthBlock.insert(tk.END, ".2")
tk.Label(blockFrame, width=20, text="Width of Block", anchor='e').grid(row=2, column=0)

depthBlock = tk.Entry(blockFrame, width=5)
depthBlock.grid(row=2, column=3)
depthBlock.insert(tk.END, ".8")
tk.Label(blockFrame, width=20, text="Depth of Block", anchor='e').grid(row=2, column=2)

meshWidBlock = tk.Entry(blockFrame, width=5)
meshWidBlock.grid(row=3, column=1)
meshWidBlock.insert(tk.END, "0.02")
tk.Label(blockFrame, width=20, text="Mesh along Width ", anchor='e').grid(row=3, column=0)

meshDepthBlock = tk.Entry(blockFrame, width=5)
meshDepthBlock.grid(row=3, column=3)
meshDepthBlock.insert(tk.END, "0.04")
tk.Label(blockFrame, width=20, text="Mesh along Depth", anchor='e').grid(row=3, column=2)


#####################--- frames and Entries Brick Entities

brickFrame = tk.LabelFrame(Entities, text="Brick Entities", padx=5, pady=5)
brickFrame.grid(row=2, column=0, sticky="nsew")

cX_Brick = tk.Entry(brickFrame, width=5)
cX_Brick.grid(row=0, column=1)
cX_Brick.insert(tk.END, "0")
tk.Label(brickFrame, width=20, text="X Origin", anchor='e').grid(row=0, column=0)

x_depth = tk.Entry(brickFrame, width=5)
x_depth.grid(row=0, column=3)
x_depth.insert(tk.END, "0")
tk.Label(brickFrame, width=20, text="X (Depth)", anchor='e').grid(row=0, column=2)

cY_Brick = tk.Entry(brickFrame, width=5)
cY_Brick.grid(row=1, column=1)
cY_Brick.insert(tk.END, "0")
tk.Label(brickFrame, width=20, text="Y Origin", anchor='e').grid(row=1, column=0)

y_Height = tk.Entry(brickFrame, width=5)
y_Height.grid(row=1, column=3)
y_Height.insert(tk.END, "0")
tk.Label(brickFrame, width=20, text="Y (Height)", anchor='e').grid(row=1, column=2)

cZ_Brick = tk.Entry(brickFrame, width=5)
cZ_Brick.grid(row=2, column=1)
cZ_Brick.insert(tk.END, "0")
tk.Label(brickFrame, width=20, text="Z Origin", anchor='e').grid(row=2, column=0)

z_Width = tk.Entry(brickFrame, width=5)
z_Width.grid(row=2, column=3)
z_Width.insert(tk.END, "0")
tk.Label(brickFrame, width=20, text="Z (Width)", anchor='e').grid(row=2, column=2)

Mesh_depth = tk.Entry(brickFrame, width=5)
Mesh_depth.grid(row=3, column=1)
Mesh_depth.insert(tk.END, "0")
tk.Label(brickFrame, width=20, text="X Mesh (Depth)", anchor='e').grid(row=3, column=0)

Mesh_Height = tk.Entry(brickFrame, width=5)
Mesh_Height.grid(row=3, column=3)
Mesh_Height.insert(tk.END, "0")
tk.Label(brickFrame, width=20, text="Y Mesh (Height)", anchor='e').grid(row=3, column=2)

Mesh_Width = tk.Entry(brickFrame, width=5)
Mesh_Width.grid(row=4, column=1)
Mesh_Width.insert(tk.END, "0")
tk.Label(brickFrame, width=20, text="Z Mesh (Width)", anchor='e').grid(row=4, column=0)


# file saving frames
savingFrame = tk.LabelFrame(general, padx=5, pady=5)
savingFrame.grid(row=4, column=0, sticky="nsew")


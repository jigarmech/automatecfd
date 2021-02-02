# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:55:00 2021

@author: jdodia
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 12:27:04 2021

@author: jdodia
"""
# =============================================================================
# importing necessary packages
# 
# =============================================================================
from tkinter import *
import shutil 
import tkinter as tk 
from tkinter import messagebox, filedialog 


root = Tk()
root.geometry("1000x500")
root.title("Simulation with OpenFOAM using icoFoam solver")
# =============================================================================
# Defining different widgets
# 
# =============================================================================


#Project name
def show_data():
    project = float(ent1.get())
    
l1 = Label(root, text = "Project name : ", bg = "#E8D579")

ent1 = Entry(root)

l1.grid(row=0, column=0, pady = 5, padx = 5)

ent1.grid(row=0, column=1,pady = 5, padx = 5, columnspan = 2)

#Project name end
#------------------------------------
#Solid model widget
def CreateWidgets(): 
    link_Label = Label(root, text ="Choose CAD file : ", 
                    bg = "#E8D579") 
    link_Label.grid(row = 1, column = 0, 
                    pady = 5, padx = 5) 
     
    root.sourceText = Entry(root, width = 50, 
                            textvariable = sourceLocation) 
    root.sourceText.grid(row = 1, column = 1, 
                        pady = 5, padx = 5, 
                        columnspan = 2) 
     
    source_browseButton = Button(root, text ="Browse", 
                                command = SourceBrowse, width = 15) 
    source_browseButton.grid(row = 1, column = 3, 
                            pady = 5, padx = 5) 
     
    destinationLabel = Label(root, text ="Project location : ", 
                            bg ="#E8D579") 
    destinationLabel.grid(row = 2, column = 0, 
                        pady = 5, padx = 5) 
     
    root.destinationText = Entry(root, width = 50, 
                                textvariable = destinationLocation) 
    root.destinationText.grid(row = 2, column = 1, 
                            pady = 5, padx = 5, 
                            columnspan = 2) 
     
    dest_browseButton = Button(root, text ="Browse", 
                            command = DestinationBrowse, width = 15) 
    dest_browseButton.grid(row = 2, column = 3, 
                        pady = 5, padx = 5) 
     
    copyButton = Button(root, text ="Mesh & Update", 
                        command = MeshUpdate, width = 15) 
    copyButton.grid(row = 4, column = 3, 
                    pady = 5, padx = 5) 
     
def SourceBrowse(): 
     
    root.files_list = list(filedialog.askopenfilenames(initialdir =" ")) 
    root.sourceText.insert('1', root.files_list) 
     
def DestinationBrowse(): 
    destinationdirectory = filedialog.askdirectory(initialdir =" ") 
    root.destinationText.insert('1', destinationdirectory) 
     
def MeshUpdate(): 
    files_list = root.files_list 
    destination_location = destinationLocation.get() 
    for f in files_list: 
        shutil.copy(f, destination_location) 
 
    messagebox.showinfo("SUCCESSFULL") 
    
root.config(background = "black") 
     
sourceLocation = StringVar() 
destinationLocation = StringVar() 
CreateWidgets() 

#Solid model widget end
#---------------------

#Mesh widget starts

Mesh = ["Coarse", "Medium", "Fine"]
text_Input=StringVar()
variable = StringVar(root)
variable.set(Mesh[0])
l5 = Label(root, text="Mesh Selection : ", bg ="#E8D579")
l5.grid(row=4)
w = OptionMenu(root, variable, *Mesh)
w.grid(row=4, column=1)

#Mesh widget ends
#----------------------------
# =============================================================================
# 
# #solver widget start
# 
# Solver = ["icoFoam", "simpleFoam", "PISO"]
# text_Input=StringVar()
# variable1 = StringVar(root)
# variable1.set(Solver[0])
# l6 = Label(root, text="Solver Selection : ", bg ="#E8D579")
# l6.grid(row=5)
# x = OptionMenu(root, variable1, *Solver)
# x.grid(row=5, column=1)
# #---------------
# #Solver widget ends
# 
# =============================================================================
# =============================================================================
# Widgets end
# =============================================================================


root.mainloop()

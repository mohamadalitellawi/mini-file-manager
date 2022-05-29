#python -m pip install comtypes

#Import needed modules
import os
import comtypes.client
from comtypes import COMError
from comtypes.client import CreateObject, GetActiveObject


'''Autocad
2018    AutoCAD.Application.22
2019    AutoCAD.Application.23
2020    AutoCAD.Application.23.1
2021    AutoCAD.Application.24
2022    AutoCAD.Application.24.1
2023    AutoCAD.Application.24.2
'''

def rename_layout_as_file_name():

    try: #Get AutoCAD running instance
        acad = GetActiveObject("AutoCAD.Application.24")
        state = True
    except(OSError,COMError): #If autocad isn't running, open it
        acad = CreateObject("AutoCAD.Application.24", dynamic=True)
        state = False

    if state: #If you have only 1 opened drawing
        doc = acad.Documents[0]
    else:
        #filepath = r"C:\Users\mali\Downloads\DTV\DTV\backup\B05-DWG-DTV-DDD-ST-SSC-0003-00.dwg" #Replace it with the actual drawing path
        #doc = acad.Documents.Open(filepath)
        print("there is no running autocad or file opened")

    try:
        for doc in acad.Application.Documents:
            file_name = doc.Name[:-4]
            for layout in doc.Layouts:
                if "Model" not in layout.Name:
                    try:
                        layout.Name = file_name
                        print(layout.Name)
                        break
                    except:
                        print("Error in renaming file", file_name)
    finally:
        acad = None


def get_layout_and_file_name_list():

    try: #Get AutoCAD running instance
        acad = GetActiveObject("AutoCAD.Application.24")
        state = True
    except(OSError,COMError): #If autocad isn't running, open it
        acad = CreateObject("AutoCAD.Application.24", dynamic=True)
        state = False

    if state: #If you have only 1 opened drawing
        doc = acad.Documents[0]
    else:
        #filepath = r"C:\Users\mali\Downloads\DTV\DTV\backup\B05-DWG-DTV-DDD-ST-SSC-0003-00.dwg" #Replace it with the actual drawing path
        #doc = acad.Documents.Open(filepath)
        print("there is no running autocad or file opened")

    try:
        for doc in acad.Application.Documents:
            file_name = doc.Name[:-4]
            print(file_name)
            for layout in doc.Layouts:
                if "Model" not in layout.Name:
                    try:
                        print("\t",layout.Name)
                        
                    except:
                        print("Error in renaming file", file_name)
    finally:
        acad = None


def main():
    try: #Get AutoCAD running instance
        acad = GetActiveObject("AutoCAD.Application.24.2")
        state = True
    except(OSError,COMError): #If autocad isn't running, open it
        acad = CreateObject("AutoCAD.Application.24.2",dynamic=True)
        state = False
    
    if state: #If you have only 1 opened drawing
        doc = acad.Documents[0]
    else:
        filepath = r"C:\Users\mali\Downloads\DTV\DTV\backup\B05-DWG-DTV-DDD-ST-SSC-0003-00.dwg" #Replace it with the actual drawing path
        doc = acad.Documents.Open(filepath)

    #Our example command is to draw a line from (0,0) to (5,5)
    command_str = '._line 0,0 5,5 ' #Notice that the last SPACE is equivalent to hiting ENTER
    #You should separate the command's arguments also with SPACE

    #Send the command to the drawing
    doc.SendCommand(command_str)

#Execution Part
if __name__ == '__main__':
    rename_layout_as_file_name()
    print('\nDone')
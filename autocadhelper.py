#pip install pyautocad
from pyautocad import Autocad, utils
from pathlib import Path
import time

def rename_layout_as_file():
    acad = Autocad()
    for doc in acad.app.Documents:
        file_name = doc.Name[:-4]
        for layout in doc.Layouts:
            if "Model" not in layout.Name:
                try:
                    layout.Name = file_name
                except:
                    print("Error in renaming file", file_name)


        # for layout_number, layout in enumerate(acad.iter_layouts()):
        #     if layout_number == 0:
        #         layout.Name = file_name
        #         print(layout_number,layout.Name)
        #         time.sleep(1)

def main():
     acad = Autocad()
     for doc in acad.app.Documents:
        print ("Drawing Name:",doc.Name)
        for layout_number, layout in enumerate(acad.iter_layouts()):
            print("\tLayout\t",layout_number,layout.Name)

if __name__ == "__main__":
    #main()
     rename_layout_as_file()
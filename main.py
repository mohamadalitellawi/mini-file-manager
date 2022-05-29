import db
import pathlib
import buisness

from autocadhelper_com import rename_layout_as_file_name , get_layout_and_file_name_list

def show_title():
    print("The Mini File Manager Program")
    print()



def show_menu():
    print("COMMAND MENU")
    print("dir - Assign Working Directory")
    print("lst - Show File List in Working Directory")
    print("rev - Change File Revision")
    print("lay - Update Autocad Layout Name as Drawing Name")
    print("laylist - Print List Of Autocad files and layouts")
    print("m - Show Menu")
    print("x = Exit Program")

def get_int(prompt, maxNum = 1000):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Invalid whole number (integer). please try again./n")
            continue
        if number < 1 or number > maxNum:
            print("That number is out of range. Please try again.\n")
        else:
            return number


def change_working_directory():
    while True:
        try:
            new_path = pathlib.Path( input("Select New Directory to work inside:\t"))
        except ValueError:
            print("Invalid Path . please try again./n")
            continue
        if not new_path.is_dir():
            print("That Path is not correct. Please try again.\n")
        else:
            return new_path.resolve()

def change_file_revision(directory):
    try:
        file_extension = input("what is the files extension to change the revision? (dwg\\pdf)\n")
        new_revision = input("enter the new revision:\n")
        buisness.change_revision(directory,file_extension,new_revision,len(new_revision))
    except:
        print("\n!Error in change_file_revision")

def print_layouts_names():
    get_layout_and_file_name_list()

def update_cad_layouts():
    rename_layout_as_file_name()

def list_all_files_in_working_directory(directory):
    try:
        file_extension = input("what is the files extension to change the revision? (dwg\\pdf)\n")
        files = buisness.get_files_of_extension(directory,file_extension)
        [print(f.resolve()) for f in files]
    except:
        print("\n!Error in Getting files from working directory")

def main():
    show_title()
    show_menu()

    wdir = pathlib.Path().cwd().resolve()


    while True:
        print(f'Current Working Directory is\t{wdir}')
        command = input("Command: ").lower()
        if command == "dir":
            wdir = change_working_directory()
        if command == "lst":
            list_all_files_in_working_directory(wdir)
        elif command == "rev":
            change_file_revision(wdir)
        elif command == "lay":
            update_cad_layouts()
        elif command == "laylist":
            print_layouts_names()
        elif command == "m":
            show_menu()
        elif command == "x":
            print("Bye!")
            break
        else:
            print("Not Valid Command. Please try again.\n")

if __name__ == "__main__":
    main()

import db
import pathlib
import buisness

def show_title():
    print("The Mini File Manager Program")
    print()



def show_menu():
    print("COMMAND MENU")
    print("dir - Assign Working Directory")
    print("rev - Change File Revision")
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


def main():
    show_title()
    show_menu()

    wdir = pathlib.Path().cwd().resolve()


    while True:
        print(f'Current Working Directory is\t{wdir}')
        command = input("Command: ").lower()
        if command == "dir":
            wdir = change_working_directory()
        elif command == "rev":
            change_file_revision(wdir)

        elif command == "x":
            print("Bye!")
            break
        else:
            print("Not Valid Command. Please try again.\n")

if __name__ == "__main__":
    main()
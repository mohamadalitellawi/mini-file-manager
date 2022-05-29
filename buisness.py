from pathlib import Path
import shutil

from pprint import pprint

def get_files_of_extension(directory:Path, extension:str) -> Path:
    ext = f'*.{extension}'
    p = directory.glob(ext)
    files = [x for x in p if x.is_file()]
    return files

def change_revision(directory:Path,extension:str, revision:str, length:int = 2):
    files = get_files_of_extension(directory,extension)
    for file in files:
        old_name = file.stem
        new_name = old_name[0:-length]
        new_name += revision
        backup_dir = directory / 'backup'

        backup_dir.mkdir(exist_ok=True)
        shutil.copy(file,backup_dir)

        new_file = file.with_stem(new_name)
        file.replace(new_file)
    print ('\nDone!')

def main():
    test_path = Path.cwd()
    # Search the directory
    p = list(test_path.glob('*.*'))
    pprint(p)
    # Search directories and subdirectories, recursively
    p = list(test_path.rglob('*.*'))
    pprint(p)

    pprint("="*20)
    files = [x for x in p if x.is_file()]
    pprint(files)

if __name__ == "__main__":
    main()
    #change_revision(Path(r'C:\Users\mali\Downloads\DTV\DTV'),'dwg','0004',length=2)
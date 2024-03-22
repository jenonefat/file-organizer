import os
import sys
import shutil
PDF_EXT = ".pdf"
IMAGE_EXT = (".png", ".jpeg", ".jpg")
PRES_EXT = ".pptx"
DOC_EXT = (".doc", ".docx", ".txt")


def create_dir(path):
    '''
    Determines whether a directory exists,
    and if not, creates new directory

    path: path for directory that will be created(if it doesn't
    already exist)

    Returns: new directory if folder did not already exist,
    nothing if already exists
    '''
    if not os.path.exists(path):
        os.mkdir(path)

def organize_dir(source):
    '''
    Organizes files within a directory by moving each file
     to an appropriate new directory.
    The target directory location for each file is determined by the file extension.
    New directory categories are 'Documents', 'Images', PDFs, and 'Presentations'.

    source(string): name of directory containing files to organize

    Returns: New subdirectories in source directory that
    contain the appropriate files
    '''
    # obtaining current working directory
    cwd = os.getcwd()
    # path for source directory
    source_path = os.path.join(cwd, source)

    # find each file name in directory tree using recursive process
    for root, dirs, files in os.walk(source_path):
        # iterate through each file name found in directory
        for file in files:
            # current file location
            file_path = os.path.join(root, file)

            # categorizing file based on its extension
            if file.endswith(PDF_EXT):
                target = "PDFs"
            elif file.endswith(IMAGE_EXT):
                target = "Images"
            elif file.endswith(PRES_EXT):
                target = "Presentations"
            elif file.endswith(DOC_EXT):
                target = "Documents"
            # if file extension does not fit into any category, ignore
            else:
                continue

            target_path = os.path.join(source_path, target)
            create_dir(target_path)

            # checks to see if file is already in new directory location;
            # prevents error message when rerunning code
            if not os.path.exists(
                    os.path.join(target_path, file)
            ):
                # moves file from current directory to new directory
                shutil.move(file_path, target_path)



if __name__ == "__main__":
    args = sys.argv

    if len(args) != 2:
        raise Exception("Pass in directory you would like to organize ONLY")

    source = args[1]
    organize_dir(source)

from _typeshed import FileDescriptorLike
import time as t
import os
import os.path
from collatzer_main import *


def optionsChecker():
    with open("options.txt", "r") as optionsFile:
        for lineNumber, optionsFileLine in enumerate(optionsFile):
            if lineNumber == 0:  # first line in the options file
                lineContent_L1 = optionsFileLine.replace("dir_save", "")
                lineContent_L1 = lineContent_L1.replace("=", "")
                lineContent_L1 = lineContent_L1.strip()

            elif lineNumber == 1:  # second line in the options file
                lineContent_L2 = optionsFileLine.replace("dir", "")
                lineContent_L2 = lineContent_L2.replace("=", "")
                # this is the folder location path for latex_outputs
                lineContent_L2 = lineContent_L2.strip()

        if lineContent_L1 == "0" and lineContent_L2 == "0":  # file location not saved
            global fileDirectoryPath
            fileDirectoryPath = str(input("latex_outputs file path \n< "))
            saveFilePath()
        else:  # file location is saved
            print("\nFile location saved (latex_outputs folder path in options.txt")
            print("The folder path is saved as:", lineContent_L2)
            correctChecker = str(input("Is this correct? [Y/n]\n< "))
            correctChecker = correctChecker.upper()
            if correctChecker == 'N':  # execute save function
                global fileDirectoryPath
                fileDirectoryPath = str(input("latex_outputs file path \n< "))
                saveFilePath()


def saveFilePath():  # function that saves the latex_outputs path to options.txt (if it is not saved yet)
    os.remove("options.txt")
    with open("options.txt", "w") as NewOptionsFile:
        NewOptionsFile.write("dir_save = 1\n")
        FilePathInOptions = "dir = " + fileDirectoryPath


def latexSaveFile(fileContent):
    fileFormat = str(input("""
File format of file?
[1 = .tex]
[2 = .txt]
< """))
    if fileFormat == "1":
        fileFormat = ".tex"
    else:
        fileFormat = ".txt"

    fileName = str(input("""
File Name?
< """))
    fullFileName = fileName + fileFormat
    with open(fullFileName, "w") as f:
        f.write(fileContent)

    for i in range(10):
        t.sleep(0.35)
        print("\nLoading...\n")
    print("Done!")

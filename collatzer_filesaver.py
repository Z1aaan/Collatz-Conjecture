import time as t
import os
import os.path as path
import json
from collatzer_main import *


def optionsChecker():
    global fileDirectoryPath
    fileDirectoryPath = str()

    with open("config.json", "r") as configFile:
        global configs
        configs = json.load(configFile)

        dirSaved = configs["dir_save"]
        dirSaveLocation = configs["dir"]

        if dirSaveLocation == "0" and dirSaved == "0":  # file location not saved
            print("""
Folder location for latex_output not saved...
options.txt
{
  "dir_save": "0",
  "dir": "0"
}
saveFilePath function loading...\n""")
            fileDirectoryPath = str(input("latex_outputs file path \n< "))
            configFile.close()
            saveFilePath()

        else:  # file location is saved
            print("\nFile location saved (latex_outputs folder path in options.txt)")
            print("The folder path is saved as:", dirSaveLocation)
            correctChecker = str(input("Is this correct? [Y/n]\n< "))
            print()
            correctChecker = correctChecker.upper()
            if correctChecker == 'N':  # execute save function
                fileDirectoryPath = str(input("latex_outputs file path \n< "))
                configFile.close()
                saveFilePath()


def saveFilePath():  # function that saves the latex_outputs path to options.txt (if it is not saved yet)
    configs["dir"] = fileDirectoryPath
    configs["dir_save"] = "1"
    with open("config.json", "w") as configFile:
        json.dump(configs, configFile)


def getFolderLocation():
    global FOLDERLOCATION
    FOLDERLOCATION = str()
    with open("config.json", "r") as configFile:
        content = configs["dir"]

    # Backslash duplicator because python doesn't recognize a single '\'
    for character in content:
        if character == "\\":
            FOLDERLOCATION += character + character
        else:
            FOLDERLOCATION += character


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

    t.sleep(2)

    optionsChecker()
    saveFilePath()
    getFolderLocation()

    print(FOLDERLOCATION)

    fullFileName = fileName + fileFormat
    completeFileName = path.join(FOLDERLOCATION, fullFileName)

    with open(completeFileName, "w") as f:
        f.write(fileContent)

    for i in range(10):
        t.sleep(0.35)
        print("\nLoading...\n")
    print("Done!")

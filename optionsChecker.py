def optionsChecker():
    global fileDirectoryPath
    fileDirectoryPath = str()
    with open("collatzer_options.txt", "r") as optionsFile:
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
            print("""
Folder location for latex_output not saved...
options.txt
{
    dir_save = 0
    dir = 0
}
saveFilePath function loading...\n""")
            fileDirectoryPath = str(input("latex_outputs file path \n< "))
            optionsFile.close()
            saveFilePath()
        else:  # file location is saved
            print("\nFile location saved (latex_outputs folder path in options.txt)")
            print("The folder path is saved as:", lineContent_L2)
            correctChecker = str(input("Is this correct? [Y/n]\n< "))
            print()
            correctChecker = correctChecker.upper()
            if correctChecker == 'N':  # execute save function
                fileDirectoryPath = str(input("latex_outputs file path \n< "))
                optionsFile.close()
                saveFilePath()

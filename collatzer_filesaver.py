import time as t


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

    for i in range(15):
        t.sleep(0.7)
        print("\nLoading...\n")
    print("Done!")
    input("Press ANY KEY to leave...")

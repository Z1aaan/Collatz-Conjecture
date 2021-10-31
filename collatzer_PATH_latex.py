from collatzer_main import *
from collatzer_filesaver import *
import time as t
import math


def collatz_latex(collatzN):
    # remember to duplicate \ because python needs two \ to print it
    latex_path = str()
    collatzN_str = str(collatzN)
    collatzN_prev = int()
    collatzN_str_prev = str()

    # start the latex docuement

    # separate the begin variables to append because we have to insert the user unput

    latexBegin_1 = """
    \\documentclass{article}
    \\usepackage[utf8]{inputenc}
    \\usepackage{amsmath}
    \\begin{document}"""

    latexBegin_input = "\n %Title \n \\section{Collatz Sequence for \(n=" + \
        collatzN_str + "\) }"

    latexBegin_2 = latexBegin_input

    latexBegin_3 = """
    %Collatz Function
    \\[
        f(n)=
        \\begin{cases}
        \\frac{n}{2}, & n \mod 2=0
        \\\\
        3n+1, &n \mod 2=1
        \end{cases} \\\\
    \\]"""

    latex_path += latexBegin_1 + latexBegin_2 + latexBegin_3

    # add the output of collatzer_main to the middle of the latex document
    latexMainStart_1 = """
    % Path for given N
    \\("""
    latexMainStart_2 = "\\textbf{Path for f(" + collatzN_str + ")}"

    latexMainStart_3 = "\\\\[3mm]"

    latex_path += latexMainStart_1 + latexMainStart_2 + latexMainStart_3

    # LATEX

    # odd
    # f(n), n=[INPUT]
    # \\
    # \Rightarrow 3(n)+1
    # \\[1mm]

    # even
    # f(n), n=1
    # \\
    # \Rightarrow \frac{n}{2}

    CollatzMain = int()
    CollatzMainPrev = int()
    STRCollatzMain = str()
    STRCollatzMainPrev = str()

    ifCond = collatzN % 2
    if ifCond == 0:
        CollatzMainPrev = collatzN
        STRCollatzMainPrev = str(CollatzMainPrev)
        CollatzMain = CollatzMainPrev / 2
        CollatzMain = math.trunc(CollatzMain)
        STRCollatzMain = str(CollatzMain)
        eq_collatzEquation = "f(n), n=" + STRCollatzMainPrev + \
            "\n \\\\ \n \\Rightarrow \\frac{" + \
            STRCollatzMainPrev + \
            "}{2} " + "\n \\\\ \n \\Rightarrow n=" + \
            STRCollatzMain + "\n \\\\[3mm] \n"
        latex_path += eq_collatzEquation
    else:
        CollatzMainPrev = collatzN
        STRCollatzMainPrev = str(CollatzMainPrev)
        CollatzMain = (3 * CollatzMainPrev) + 1
        CollatzMain = math.trunc(CollatzMain)
        STRCollatzMain = str(CollatzMain)
        eq_collatzEquation = "f(n), n=" + STRCollatzMainPrev + \
            "\n \\\\ \n \\Rightarrow 3(" + STRCollatzMainPrev + ") + 1" + \
            "\n \\\\ \n \\Rightarrow n=" + STRCollatzMain + "\n \\\\[3mm] \n"
        latex_path += eq_collatzEquation

    while True:
        if CollatzMain != 1:
            ifCond = CollatzMain % 2
            if ifCond == 0:
                CollatzMainPrev = CollatzMain
                STRCollatzMainPrev = str(CollatzMainPrev)
                CollatzMain = CollatzMainPrev / 2
                CollatzMain = math.trunc(CollatzMain)
                STRCollatzMain = str(CollatzMain)
                eq_collatzEquation = "f(n), n=" + STRCollatzMainPrev + \
                    "\n \\\\ \n \\Rightarrow \\frac{" + \
                    STRCollatzMainPrev + \
                    "}{2} " + "\n \\\\ \n \\Rightarrow n=" + \
                    STRCollatzMain + "\n \\\\[3mm] \n"
                latex_path += eq_collatzEquation
            else:
                CollatzMainPrev = CollatzMain
                STRCollatzMainPrev = str(CollatzMainPrev)
                CollatzMain = (3 * CollatzMainPrev) + 1
                CollatzMain = math.trunc(CollatzMain)
                STRCollatzMain = str(CollatzMain)
                eq_collatzEquation = "f(n), n=" + STRCollatzMainPrev + \
                    "\n \\\\ \n \\Rightarrow 3(" + STRCollatzMainPrev + ") + 1" + \
                    "\n \\\\ \n \\Rightarrow n=" + \
                    STRCollatzMain + "\n \\\\[3mm] \n"
                latex_path += eq_collatzEquation
            # print(CollatzMain, CollatzMainPrev)
            # print(latex_path)
            # input()
        else:
            break

    # end to latex docuement
    latexEnd = """
    \\section{Credits and References Shit}
    %Maybe add link to gitrepo and other shit, idk
    This is created using Collatzer (https://github.com/Z1aaan/Collatzer).
    Created By: Z1aaan
    
    README:
    A program created to visualize and simulate a user-given value for \\textit{N} 
    and see what happens when it is put under the Collatz function.
    \\end{document}"""

    latex_path += latexEnd

    print(latex_path)

    latexSaveFile(latex_path)


def collatz_latex_start(mainImport):
    choice = str(input("""
Converting the equation in LaTeX, 
may take a long time (depending on how long the equation is),
are you sure? [Y/n]
< """))
    choice = choice.upper()
    if choice == 'Y':
        print()
        print("""
PATH_latex: Working...
Converting to LaTeX... 
Hold On....""")
        for i in range(10):
            # add this so that there's like a 'loading sequence' before the latex output is displayed
            t.sleep(0.1)
            print()
        collatz_latex(mainImport)
    else:
        print("\nPATH_latex: leaving...")

from collatzer_main import *
import time as t


def collatz_latex(collatzN):
    # remember to duplicate \ because python needs two \ to print it
    latex_path = str()
    collatzN_str = str(collatzN)

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

    # f(n), n = [INPUT]
    # \\
    # \Rightarrow 3(n)+1
    # \\[1mm]
    # \vdots
    # \\[1mm]
    # f(n), n = 1
    # \\
    # \Rightarrow \frac{n}{2}

    # \)

    # collatz_function="f(" + NUM_str + ")"
    # PATH += "Path for " + collatz_function + "\n"

    # ifCondition=NUM % 2
    # if ifCondition == 0:
    #     NUM_str=str(NUM)
    #     PATH += "\n" + "n = " + NUM_str
    #     equation="\n => " + NUM_str + " / 2 \n"
    #     PATH += equation
    # else:
    #     NUM_str=str(NUM)
    #     PATH += "\n" + "n = " + NUM_str
    #     equation="\n => (3 * " + NUM_str + ") + 1 \n"
    #     PATH += equation

    # end to latex docuement
    latexEnd = """
    \\section{Credits and References Shit}
    %Maybe add link to gitrepo and other shit, idk

    \\end{document}"""

    latex_path += latexEnd

    print(latex_path)


if __name__ == "__main__":
    print("""Put messages here later""")
    for i in range(10):
        # add this so that there's like a 'loading sequence' before the latex output is displayed
        t.sleep(0.25)
        print()
    collatz_latex(3)

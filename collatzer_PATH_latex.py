from collatzer_main import *
import time as t


def collatz_latex(collatz_N):
    # remember to duplicate \ because python needs two \ to print it
    latex_path = str()
    # start the latex docuement
    latexBegin = """
    \\documentclass{article}
    \\usepackage[utf8]{inputenc}
    \\usepackage{amsmath}
    \\begin{document}

    %Title
    \\section{Collatz Sequence for \(n=[INPUT]\) }

    %Collatz Function
    \\[
        f(n)=
        \\begin{cases}
        \\frac{n}{2}, & n \mod 2=0
        \\\\
        3n+1, &n \mod 2=1
        \end{cases} \\\\
    \\]"""
    latex_path += latexBegin

    # add the output of collatzer_main to the middle of the latex document

    # end to latex docuement
    latexEnd = """
    \\section{Credits and References Shit}
    %Maybe add link to gitrepo and other shit, idk

    \\end{document}"""

    latex_path += latexBegin
    print(latex_path)


if __name__ == "__main__":
    print("""Put messages here later""")
    for i in range(10):
        # add this so that there's like a 'loading sequence' before the latex output is displayed
        t.sleep(0.25)
        print()
    collatz_latex(3)

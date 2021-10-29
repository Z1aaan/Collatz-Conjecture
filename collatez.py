"""
    Collatz's Conjecture
"""
import time as t


def collatz(NUM):
    while True:
        # stop the loop if the collatz_value = 1
        if NUM != 1:
            ifCondition = NUM % 2
            if ifCondition == 0:  # if statement 1, n mod 2 = 0 (even)
                # code 1
                NUM = NUM/2
            else:  # if statement 2, n mod 2 = 1 (odd)
                NUM = (3*NUM) + 1
        # break the loop because the collatz_value reached 1
        else:
            break


def collatzPath(NUM, PATH):  # creates the path for the user to view
    # I want PATH to look like this:
    """
    Path for f(NUM):
    n = ...
    => ...
    n = ...
    ...
    n = 1
    """

    NUM_str = str(NUM)
    collatz_function = "f(" + NUM_str + ")"
    PATH += "Path for " + collatz_function

    NUM_str = str(NUM)
    PATH += "\n" + "n = " + NUM_str
    equation = "\n" + NUM_str + " / 2 \n"
    PATH += equation

    while True:
        if NUM != 1:
            ifCondition = NUM % 2
            if ifCondition == 0:
                NUM = NUM/2
                NUM_str = str(NUM)
                PATH += "\n" + "n = " + NUM_str
                equation = "\n" + NUM_str + " / 2 \n"
                PATH += equation
            else:
                NUM = (3*NUM) + 1
                NUM_str = str(NUM)
                PATH += "\n" + "n = " + NUM_str
                equation = "(3 * " + NUM_str + ") + 1 \n"
                PATH += equation
        else:
            print(PATH)
            break

def PATH_latex(NUM):
    latexPath = str()
    latex_start = '$'
    collatz_function_latex = "f(n)=\left\{\begin{array}{ll}\frac{n}{2}, & \hspace{} n \, mod \, 2 = 0 \\3n+1, & \hspace{} n \, mod \, 2 = 1\\\end{array} \right"
    latexPath += latex_start + collatz_function_latex

    NUM_str = str(NUM)
    collatz_function = "f(" + NUM_str + ")"
    latex_start += "Path for " + collatz_function

    NUM_str = str(NUM)
    latexPath += "\\" + "n = " + NUM_str
    equation = "\\" + NUM_str + " / 2 \\"
    latexPath += equation
    
    while True:
        if NUM != 1:
            ifCondition = NUM % 2
            if ifCondition == 0:
                NUM = NUM/2
                NUM_str = str(NUM)
                latexPath += "\n" + "n = " + NUM_str
                equation = "\n" + NUM_str + " / 2 \n"
                latexPath += equation
            else:
                NUM = (3*NUM) + 1
                NUM_str = str(NUM)
                latexPath += "\n" + "n = " + NUM_str
                equation = "(3 * " + NUM_str + ") + 1 \n"
                latexPath += equation
        else:
            print(latexPath)
            break


if __name__ == "__main__":
    # create a variable to do the function on.
    sleepVar = 1
    NUM = int(input("Number to do function on: "))
    PATH = str()
    collatz(NUM)
    t.sleep(sleepVar)
    collatzPath(NUM, PATH)
    PATH_latex(NUM)
    

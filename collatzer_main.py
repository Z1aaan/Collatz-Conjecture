"""
    Collatz's Conjecture
"""
import time as t

from collatzer_PATH_latex import *


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
    PATH += "Path for " + collatz_function + "\n"

    ifCondition = NUM % 2
    if ifCondition == 0:
        NUM_str = str(NUM)
        PATH += "\n" + "n = " + NUM_str
        equation = "\n => " + NUM_str + " / 2 \n"
        PATH += equation
    else:
        NUM_str = str(NUM)
        PATH += "\n" + "n = " + NUM_str
        equation = "\n => (3 * " + NUM_str + ") + 1 \n"
        PATH += equation

    while True:
        if NUM != 1:
            ifCondition = NUM % 2
            if ifCondition == 0:
                NUM = NUM/2
                NUM_str = str(NUM)
                PATH += "\n" + "n = " + NUM_str
                equation = "\n => " + NUM_str + " / 2 \n"
                PATH += equation
            else:
                NUM = (3*NUM) + 1
                NUM_str = str(NUM)
                PATH += "\n" + "n = " + NUM_str
                equation = "\n => (3 * " + NUM_str + ") + 1 \n"
                PATH += equation
        else:
            print(PATH)
            break


if __name__ == "__main__":
    # create a variable to do the function on.
    sleepVar = 1
    print("Welcome to Collatzer\n")
    t.sleep(sleepVar)
    NUM = int(input("Number to do function on: "))
    print()
    PATH = str()
    collatz(NUM)
    print("Hold On...\n")
    t.sleep(sleepVar * 2)
    collatzPath(NUM, PATH)
    collatz_latex_start(NUM)

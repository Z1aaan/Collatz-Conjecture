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
    PATH += "Path for " + collatz_function + "\n"

    ifCondition = NUM % 2
    if ifCondition == 0:
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


if __name__ == "__main__":
    # create a variable to do the function on.
    sleepVar = 1
    NUM = int(input("Number to do function on: "))
    PATH = str()
    collatz(NUM)
    t.sleep(sleepVar)
    collatzPath(NUM, PATH)

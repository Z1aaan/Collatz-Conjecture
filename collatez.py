"""
    Collatz's Conjecture
"""


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
            print(NUM)
            break


def collatzPath(NUM, PATH):  # export in LaTeX
    NUM_str = str(NUM)
    collatz_function = "f(" + NUM_str + ")"
    PATH += "Path for" + collatz_function
    while True:
        if NUM != 1:
            ifCondition = NUM % 2
            if ifCondition == 0:
                pass

            else:
                pass
        else:
            break


if __name__ == "__main__":
    # create a variable to do the function on.
    NUM = int(input("Number to do function on: "))
    PATH = str()
    """
    I want PATH to look like this:
    Path for f(NUM):
    n = ...
    => ...
    n = ... 
    .   
    .
    .
    n = 1    
    """
    collatz(NUM)

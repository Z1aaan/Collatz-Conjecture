import random
from collatzer_main import *


def minMaxRNG():
    userMin = int(input("""
Min
< """))
    userMax = int(input("""\n
Max
< """))
    randomNumber = random.randint(userMin, userMax)
    print("\n Generated Number: ", randomNumber)


def piValRNG():
    # 3.1415926535 8979323846

    evenNumbers = (2, 4, 6, 8)

    oddNumbers = (3, 5, 7, 9)

    randomNumber = random.randint(1, 21)

    if randomNumber in evenNumbers:
        finalRandomNumber = random.randrange(3, 9, 2)
    elif randomNumber in oddNumbers:
        finalRandomNumber = random.randrange(2, 8, 2)
    else:  # if randomNumber == 1
        finalRandomNumber = random.randint(1, 9)

    print("\n Generated Number: ", finalRandomNumber)


def importCollatzer():
    pass


if __name__ == "__main__":
    print("""
Random Number Generator
Created for Collatzer.
[1] - Min - Max RNG
[2] - Pi Digits RNG""")
    while True:
        choice = int(input("\n< "))
        if choice == 1:
            minMaxRNG()
        elif choice == 2:
            piValRNG()


import sys
import time


# TYPING EFFECT
# speaking speed veriables
SLOW = 1
MEDIUM = 0.5
FAST = 0.1
NORMAL = 0


def typing(str, speed):
    for char in str:
        time.sleep(speed)
        sys.stdout.write(char)
        sys.stdout.flush()

# WELL... I need some space in my story


def space():
    print("\n")

# opening, reading the file and giving it speed, then space


def reading(txt, speed):
    with open(txt) as f:
        lines = f.readlines()
        for line in lines:
            typing(line, speed)
    space()

# Getting the recepie


def choosen_recepie(tea):

    print("For this recepies you'll need:\n")
    print("")
    print("* Tea strainer/bag\n")

    for ingredient in tea:
        print("*", ingredient)
        print("")

    print("Get water to boil, and put all the ingridiantes in a strainer. Let it steep for seven minutes. After seven minutes, get the stariner out\n")
    print("and enjoy your tea. Let it cool for a bit before you sip.\n")
    print("")

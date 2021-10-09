# Game name: The recepie
# By: Amit Nudel
# Description: Ambiance text-adventure

from os import linesep
from functions import *
from tea_recepies import *

# game disclaimer for allergy and stuff...
# ADD CALCULATIONS FOR THE TEA RECEPIE!!!


def main():

    # CALLING ORDER

    # INTRO

    reading('the_story/1_intro.txt', NORMAL)
    answer = ""
    while answer != "coat" and answer != "beanie" and answer != "umbrella" and answer != "boots":
        answer = input(
            "You look at yourself in the reflection, what is the fist thing you notice? your coat/ beanie/ umbrella/ boots\n").lower().strip()
    space()

    # FIRST_ACT
    reading('the_story/2_first_act.txt', NORMAL)
    answer = ""
    while answer != "ice cream" and answer != "soup":
        answer = input(
            "What do you prefer, eating ice cream in the winter, or soup in summer?\n").lower().strip()
    space()

    if answer == "ice cream":
        # ICE CREAM
        reading('the_story/3_ice_cream.txt', NORMAL)
        answer = ""
        while answer != "skipping" and answer != "running":
            answer = input(
                "How do you want to cross the rest of the park? by skipping or running?\n").lower().strip()
        space()
        if answer == "skipping":
            print(
                "You start to hop cheerfully, and with every hop your smile is getting bigger and bigger.")
        elif answer == "running":
            print(
                "You start running with glee, feeling the blood rushes through your veins.")
        print("You take a turn, and get out of the park back to the street, and you see the big oak tree from afar. You are getting closer.\n")
        space()

    elif answer == "soup":

        # SOUP
        reading('the_story/4_soup.txt', NORMAL)
        answer = ""
        while answer != "yes" and answer != "no":
            answer = input(
                "Do you want to put a rock on the grave? yes/no\n").lower().strip()
        if answer == "yes":
            print(
                "You look around, and find a small, round, green rock and place it on the grave.")
        elif answer == "no":
            print(
                "You look at the grave, turn from it, and contionue to walk in the cemetery.")
        print("You find the exit rather easliy this time, and go back to the street. You see the big oka tree from afar. You are getting closer.\n")

    # 5
    reading('the_story/5.txt', NORMAL)
    answer = ""
    while answer != "honey" and answer != "maple":
        answer = input(
            "Which cupacke do you choose? honey/maple\n").lower().strip()
    if answer == "honey":
        print("You grab three honey cupcakes and pay for them. Greeing at the cashier, and get out of the bakery.\n")
    elif answer == "maple":
        print("You grab three maple cupcakes and pay for them. Greeing at the cashier, and get out of the bakery.\n")

    # SECOND ACT
    reading('the_story/6_second_act.txt', NORMAL)

   # THIRD ACT
    line_check = 0
    with open('the_story/7_third_act.txt') as f:
        lines = f.readlines()
        for line in lines:
            line_check += 1
            if line_check == 6 or line_check == 8:
                typing(line, MEDIUM)
            else:
                typing(line, NORMAL)
    space()

    answer = ""
    thoughts = ["fear", "anxious", "ambivalent",
                "curiosity", "calm", "wtf"]

    while not answer in thoughts:
        answer = input(
            "You look at the Pourer. What is your first thought? fear/anxious/ambivalent/curiosity/calm/WTF\n").lower().strip()
    if answer in thoughts:
        typing(f"{answer}? intersting, but expected...hehe", MEDIUM)
    space()
    # POURER QUETSTIONS

    print("They look at you, eyes glimming with anticipation.\n")

    answer = ""
    feeling = ["confused", "happy", "relaxed",
               "restless", "amused", "tired like a cub"]

    while not answer in feeling:
        typing("How do you feel at the moment? confused/happy/relaxed/restless/amused/tired like a cub. ", MEDIUM)
        answer = input(
            "The Pourer asks while their eyes fixed on you\n").lower().strip()

    if answer in feeling:
        typing(f"{answer}? alright", SLOW)
    answer = ""
    strength = ["mind", "heart", "stomach",
                "focus", "will", "knitting ability"]
    space()

    while not answer in strength:
        answer = input(typing(
            "What do you feel you need to strengthen? your mind/heart/stomach/focus/will/knitting ability\n", FAST)).lower().strip()

    if answer in strength:
        typing(f"{answer}? mm that's relatable", FAST)
    space()
    # GIVING THE RECEPIE
    # choosen_recepie(RECEPIE NAME HERE)

    sys.exit()


if __name__ == "__main__":
    main()

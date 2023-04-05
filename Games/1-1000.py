from random import randint

againq = True

while True:
    namesq = input("Do you want to play with names? (y or n)\n:")

    if namesq.lower() == "y":
        qname = True
        break
    if namesq.lower() == "n":
        qname = False
        break

while againq is True:
    rannum = randint(0, 1001)

    if qname is True:
        name1 = input("What is the name of player 1?\n:")
        name2 = input("What is the name of player 2?\n:")
        names = True
        print(
            f"Lets go {name1.capitalize()} and {name2.capitalize()}. Get ready to start the game.\n"
        )

    else:
        names = False
        print("Lets go player 1 and player 2. Get ready to start the game.\n")

    while names is True:
        while True:
            quess1 = int(
                input(f"{name1.capitalize()}, pick a number from 1 to 1000.\n:")
            )

            if quess1 > 1000:
                print("Invalid Answer!")
            else:
                break

        while True:
            quess2 = int(
                input(f"{name2.capitalize()}, pick a number from 1 to 1000.\n:")
            )

            if quess2 > 1000:
                print("Invalid Answer!")
            else:
                break

        ans1 = abs(rannum - quess1)
        ans2 = abs(rannum - quess2)

        if ans1 < ans2:
            print(
                f"\n{name1.capitalize()} won!\nThe number was {rannum}.\n{name1.capitalize()} was {ans1} away and {name2.capitalize()} was {ans2} away."
            )

        if ans2 < ans1:
            print(
                f"\n{name2.capitalize()} won!\nThe number was {rannum}.\n{name1.capitalize()} was {ans1} away and {name2.capitalize()} was {ans2} away."
            )

        again = input("Do you want to play again? (y or n)\n:")

        if again == "y":
            nameq = input("Do you want to play with names? (y or n)\n:")

            if nameq == "y":
                names = True
                againq = True
                break

            if nameq == "n":
                names = False
                againq = True

        if again == "n":
            againq = False
            break

    while names is False and againq is True:
        rannum = randint(0, 1001)

        while True:
            quess1 = int(input("Player 1, pick a number from 1 to 1000.\n:"))

            if quess1 > 1000:
                print("Invalid Answer!")
            else:
                break

        while True:
            quess2 = int(input("Player 2, pick a number from 1 to 1000.\n:"))

            if quess2 > 1000:
                print("Invalid Answer!")
            else:
                break

        ans1 = abs(rannum - quess1)
        ans2 = abs(rannum - quess2)

        if ans1 < ans2:
            print(
                f"\nPlayer 1 Won!\nThe number was {rannum}.\nPlayer 1 was {ans1} away and Player 2 was {ans2} away."
            )

        if ans2 < ans1:
            print(
                f"\nPlayer 2 Won!\nThe number was {rannum}.\nPlayer 1 was {ans1} away and Player 2 was {ans2} away."
            )

        again = input("Do you want to play again? (y or n)\n:")

        if again == "y":
            nameq = input("Do you want to play with names? (y or n)\n:")

            if nameq == "y":
                names = True
                qname = True
                againq = True
                break

            if nameq == "n":
                names = False
                againq = True
                break

        if again == "n":
            againq = False
            break

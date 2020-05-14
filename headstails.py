from random import randint

qheads = False
qtails = False
again = True
heads = False
tails = False
stop = False

while again == True:

    print("Thank you for playing! Hope you enjoy the game.")

    rannum = randint(1, 3)

    while True:

        ques = input("Do you want heads or tails?\n:")
        newques = ques.lower()

        if newques == 'heads':
            qheads = True
            break
        if newques == 'tails':
            qtails = True
            break
        if newques == 'end':
            print("Your operation has been stopped!")
            stop = True
            break

    if stop == True:
        break

    if rannum == 1:
        heads = True
    if rannum == 2:
        tails = True

    if heads == True and qheads == True:
        print("You won! It was heads!")

    if heads == False and qheads == True:
        print("You lost! It was tails!")

    if tails == True and qtails == True:
        print("You won! It was tails!")

    if tails == False and qtails == True:
        print("You lost! It was tails!")

    while True:

        againq = input(
            "Thank you for playing! Do you want to play again? (y or n)\n:")

        if againq.lower() == 'y':
            again = True
            break
        if againq.lower() == 'n':
            again = False
            break

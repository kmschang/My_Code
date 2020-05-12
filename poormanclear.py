quesagain = True
game = True

def poor_clear():
    print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


def again():
    while True:
        qagain = input ("Do you want to play again? (y or n)\n:")
        if qagain.lower() == 'y':
            quesagain = True
            break
        if qagain.lower() == 'n':
            quesagain = False
            break
        break




while quesagain == True:

    poor_clear()

    while True:

        ques = input("Do you want to play a game? (y or n)\n:")

        if ques.lower() == 'y':
            game = True
            break

        if ques.lower() == 'n':
            game = False
            break

    if game == True:

        print ("Sorry. There is no game actually. LOL")

    elif game == False:

        print ("You won. There wasn't even a game.")

    again()

    if quesagain == False:
        break
    

slogin = False

while slogin is False:
    tname = False
    tmail = False
    tpass = False

    print(
        "If you are new, type 'm' to make a new login, if you just make a login, type 'l' to login.\nIf you want to leave just type end."
    )
    question = input("Do you want to login (l) or make a login (m)?\n:")
    nques = question.lower()

    if nques == "m":
        while True:
            name = input("what is your name?\n:")
            capname = name.capitalize()

            if name == "end":
                print("Your operaion has been ended.")
                break

            while True:
                yn = input(f"Are you sure you want {name} as your name? (y or n)?\n:")

                if yn == "y":
                    tname = True
                    bk = True
                    break

                if yn.lower() == "end":
                    print("Your operaion has been ended.")
                    break

                else:
                    print("Yes (y) or No (n) please.")
                    bk = False
                    break

            if bk is True:
                break

        while tname is True:
            email = input(f"{capname}, what is your email?\n:")

            if email == "end":
                print("Your operaion has been ended.")
                break

            while True:
                yn = input(f"Are you sure you want {email} as your email? (y or n)?\n:")

                if yn == "y":
                    tmail = True
                    bk = True
                    break

                if yn.lower() == "end":
                    print("Your operaion has been ended.")
                    break

                else:
                    print("Yes (y) or No (n) please.")
                    bk = False
                    break

            if bk is True:
                break

        while tmail is True:
            password = input(f"{capname}, what password do you want for {email}?\n:")

            if password == "end":
                print("Your operaion has been ended.")
                break

            while True:
                yn = input(
                    f"Are you sure you want {password} as your password? (y or n)?\n:"
                )

                if yn == "y":
                    tpass = True
                    bk = True
                    break

                if yn.lower() == "end":
                    print("Your operaion has been ended.")
                    break

                else:
                    print("Yes (y) or No (n) please.")
                    bk = False
                    break

            if bk is True:
                break

    if nques == "l":
        tpass = True
        cornam = False
        login = False
        admin = False

        while tpass is True:
            inname = input("What is you name?\n:")

            if inname.lower() == "admin":
                cornam = True
                admin = True
                break

            if inname.lower() == name.lower():
                print(f"Hello {capname}")
                cornam = True
                break

            if inname.lower() == "end":
                print("Your operation has been ended.\n")
                break

            else:
                print("You are not in our system. Please Try again.\n")

        while cornam is True:
            if admin is True:
                break

            inmail = input(f"What is your email {capname}?\n:")

            if inmail.lower() == "end":
                print("Your operation has been ended.\n")
                break

            if inmail.lower() == email.lower():
                while True:
                    inpass = input(f"What is your password {capname}?\n:")

                    if inpass.lower() == "end":
                        print("Your operation has been ended.\n")
                        break

                    if inpass == password:
                        print(f"Welcome {capname}!")
                        login = True
                        break

                    else:
                        print("Incorrect password! Please try again.")

                break

            else:
                print("Incorrect e-mail! Please try again.")

        if login is True:
            print("This is where you put your secret.")
            slogin = True

        break

    if nques == "end":
        break

whatgame = int(
    input("What game do you want to play?\nHead or Tails (1) or 1 - 1000 (2)\n:")
)

if whatgame == 1:
    from random import randint

    print(
        "Game Rule: \nIf you want heads, type heads.\nIf you want tails, type tails.\nIf you want to leave, type end.\n"
    )

    while True:
        while True:
            answer = input("Heads or Tails? ")
            lower = answer.lower()

            if lower == "heads":
                newanswer = "heads"
                break

            elif lower == "tails":
                newanswer = "tails"
                break

            elif answer == "end":
                newanswer = "end"
                break

            else:
                print("Try again please?")

        number = randint(0, 101)
        key = number % 2

        if newanswer == "end":
            print("Your game has been stopped!")
            break

        elif key == 1 and newanswer == "heads":
            print("It was Heads. You Won!")

        elif key == 1 and newanswer != "heads":
            print("It was Heads. You Lost!")

        elif key == 0 and newanswer == "tails":
            print("It was tails. You Won!")

        elif key == 0 and newanswer != "tails":
            print("It was tails. You Lost!")

        else:
            print("There was an error. Please Restart.")

        gameend = input("Do you want to play again? (y or n)")

        if gameend == "n":
            break

if whatgame == 2:
    from random import randint

    endans = False

    print(
        "Each Player has to type their own number. If you want to leave the game just type 666.\n"
    )

    while True:
        while True:
            answer1 = int(input("Player 1.\nWhat is your number?"))

            if answer1 == 666:
                endans = True
                break

            elif answer1 <= 1000:
                break

            elif answer1 > 1000:
                print("Please try again!")

        while endans is not True:
            answer2 = int(input("Player 2.\nWhat is your number?"))

            if answer2 == 666:
                endans = True
                break

            elif answer2 <= 1000:
                break

            elif answer2 > 1000:
                print("Please try again!\n")

        if endans is True:
            break

        answerr = randint(0, 1001)

        player1 = abs(answerr - answer1)
        player2 = abs(answerr - answer2)

        if player1 > player2:
            print(
                f"Player 2 Wins!\nThe Number was {answerr}.\nPlayer 1 was {player1} away and player 2 was {player2} away.\n"
            )
        if player2 > player1:
            print(
                f"Player 1 Wins!\nThe number was {answerr}.\nPlayer 1 was {player1} away and player 2 was {player2} away.\n"
            )
        if player1 == player2:
            print("What are the odds. It was a draw.\n")

        gameend = input("Do you want to play again? (y or n)")

        if gameend == "n":
            break

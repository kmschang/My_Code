from random import randint


def get_name():
    return str(input("What is your name?\n:")).capitalize()


def welcome_screen(name):
    print(f"Welcome {name}")
    print("You are playing: How close to a random number 1 -100!")


def guess():
    while True:
        try:
            question = int(input("\nPick a number 1-100\n:"))
        except:
            print("Please only input integers. Thank you.")
            question = "Try again."
        else:
            if 0 < question < 101:
                return question
            else:
                print('Please only input integers 1-100. Thank you.')


def random_number():
    comp_num = int(randint(0, 100))
    return comp_num

def again():

    while True:
        try:
            yorn = int(input("\nDo you want to play again? (1 = yes or 0 = no)\n:"))
        except:
            print("Please only input 1 for yes or 0 for no. Thank you.")
        else:
            if yorn == 1:
                return True
            elif yorn == 0:
                return False
            else:
                print("Please only input 0 or 1.")


def ending_message(computer,player,name):
    diff = player - computer
    print(f"\nComputer: {computer}, {name}: {player}")
    print(f"The difference was {diff}!")


def game():
    name = get_name()

    welcome_screen(name)

    while True:

        player_guess = guess()
        computer_guess = random_number()

        ending_message(computer_guess,player_guess,name)

        if not again():
            break


game()


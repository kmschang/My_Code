from random import randint


def get_name():
    return str(input("What is your name?\n:")).capitalize()


def welcome_screen(name):
    print(f"Welcome {name}")
    print("You are playing: How close to a random number 1 -100!")


def guess():
    while True:
        try:
            question = int(input("Pick a number 1-100\n:"))
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


def game():
    name = get_name()

    welcome_screen(name)

    player_guess = guess()
    computer_guess = random_number()

    diff = abs(player_guess - computer_guess)
    print(f"Computer: {computer_guess}, {name}: {player_guess}")
    print(f"The difference between the numbers was {diff}!")


game()


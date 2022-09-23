from random import randint

"This is a test"


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


name = str(input("What is your name?\n:"))
name = name.capitalize()

while True:

    player_output = int(input("Choose a number 1-100\n:"))

    count = 0

    while True:

        computer_output = randint(1, 100)

        print(f"Computer: {computer_output}, Player: {player_output}")
        print(f"Difference:\u001b[31;1m {player_output - computer_output}\n\u001b[31;0m")

        if player_output - computer_output == 0:
            print(f"\u001b[32;5mTook {count} times to be equal.\u001b[31;0m")
            with open("playground_outputs.txt", "a") as myfile:
                myfile.write(f"\n{name}: {count} ({player_output})")
            break
        else:
            count += 1

    if not again():
        break

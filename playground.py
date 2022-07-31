from random import randint

while True:

    player_output = int(input("Choose a number 1-10\n:"))

    count = 0

    while True:

        computer_output = randint(1, 10)

        print(f"Computer: {computer_output}, Player: {player_output}")
        print(f"Difference:\u001b[31;1m {player_output - computer_output}\n\u001b[31;0m")

        if player_output - computer_output == 0:
            print(f"\u001b[32;5mTook {count} times to be equal.\u001b[31;0m")
            break
        else:
            count += 1

    break

from random import randint


## If you want to make it winnable, change first_move() on line 374 to 'random' instead of 'notrandom'

## Loading screen on/off line 342


def coltonum(x, y):
    return (x * 3) + y


def display_board():
    for col in range(3):
        for row in range(3):
            print(board[col][row], end="")
            if row != 2:
                print("\u001b[31;0m | ", end="")
            if row == 2 and col != 2:
                print("\u001b[31;0m\n---------\n", end="")
            if col == 2 and row == 2:
                print("\n")


def check_for_win(letter):
    letter = letter.upper()
    count2 = 0
    count3 = 0
    for x in range(3):
        count = 0
        for y in range(3):
            if board[x][y] == letter:
                count += 1
        if count == 3:
            print(f"{letter} won!")
            return True
    for x in range(3):
        count = 0
        for y in range(3):
            if board[y][x] == letter:
                count += 1
        if count == 3:
            print(f"{letter} won!")
            return True
    for x in range(3):
        if board[x][x] == letter:
            count2 += 1
        if count2 == 3:
            print(f"{letter} won!")
            return True
    for x in range(3):
        if board[x][2 - x] == letter:
            count3 += 1
        if count3 == 3:
            print(f"{letter} won!")
            return True


def numtocol(num):
    num -= 1
    return [num // 3, num % 3]


def first_move(string):
    if string == "random":
        rand1 = randint(0, 2)
        rand2 = randint(0, 2)
        rand3 = randint(0, 2)
        while rand2 == rand3:
            rand3 = randint(0, 2)

        if board[rand1][rand2] != " ":
            if board[rand2][rand1] != " ":
                board[rand2][rand3] = computer
            else:
                board[rand2][rand1] = computer
        else:
            board[rand1][rand2] = computer
    else:
        if board[1][1] != " ":
            board[2][2] = computer
        else:
            board[1][1] = computer


def computer_turn():
    playercount = 0
    done = False
    comcount = 0
    for x in range(3):
        for y in range(3):
            if board[x][y] == player:
                playercount += 1
            if board[x][y] == computer:
                comcount += 1
    if comcount == playercount - 1:
        for x in range(3):
            for y in range(3):
                if board[x][y] == " ":
                    board[x][y] = computer
                    done = True
                    break
                if done is True:
                    break
            if done is True:
                break
    else:
        pass


def computer_going_to_win():
    placed = False
    for x in range(3):
        count = 0
        for y in range(3):
            if board[x][y] == computer:
                count += 1
        if count == 2 and board[x][y] == " ":
            placed = True
            board[x][y] = computer
        if count == 2 and board[x][y - 1] == " ":
            placed = True
            board[x][y - 1] = computer
        if count == 2 and board[x][y - 2] == " ":
            placed = True
            board[x][y - 2] = computer
        if placed is True:
            break
    if placed is True:
        return True
    if placed is False:
        count = 0
        for x in range(3):
            count = 0
            for y in range(3):
                if board[y][x] == computer:
                    count += 1
            if count == 2 and board[y][x] == " ":
                placed = True
                board[y][x] = computer
            if count == 2 and board[y - 1][x] == " ":
                placed = True
                board[y - 1][x] = computer
            if count == 2 and board[y - 2][x] == " ":
                placed = True
                board[y - 2][x] = computer
            if placed is True:
                return True
    if placed is True:
        return True
    if placed is False:
        count = 0
        for x in range(3):
            if board[x][x] == computer:
                count += 1
        if count == 2 and board[x][x] == " ":
            placed = True
            board[x][x] = computer
        if count == 2 and board[x - 1][x - 1] == " ":
            placed = True
            board[x - 1][x - 1] = computer
        if count == 2 and board[x - 2][x - 2] == " ":
            placed = True
            board[x - 2][x - 2] = computer
    if placed is True:
        return True
    if placed is False:
        count = 0
        for x in range(3):
            if board[x][2 - x] == computer:
                count += 1
        if count == 2 and board[x][2 - x] == " ":
            placed = True
            board[x][2 - x] = computer
        if count == 2 and board[abs(x - 1)][2 - (abs(x - 1))] == " ":
            placed = True
            board[abs(x - 1)][2 - (abs(x - 1))] = computer
        if count == 2 and board[abs(x - 2)][2 - (abs(x - 2))] == " ":
            placed = True
            board[abs(x - 2)][2 - (abs(x - 2))] = computer
    if placed is True:
        return True
    if placed is False:
        return False


def computer_going_to_block():
    placed = False
    count = 0
    for x in range(3):
        count = 0
        for y in range(3):
            if board[x][y] == player:
                count += 1
        if count == 2 and board[x][y] == " ":
            placed = True
            board[x][y] = computer
        if count == 2 and board[x][y - 1] == " ":
            placed = True
            board[x][y - 1] = computer
        if count == 2 and board[x][y - 2] == " ":
            placed = True
            board[x][y - 2] = computer
        if placed is True:
            break
    if placed is True:
        return True
    if placed is False:
        count = 0
        for x in range(3):
            count = 0
            for y in range(3):
                if board[y][x] == player:
                    count += 1
            if count == 2 and board[y][x] == " ":
                placed = True
                board[y][x] = computer
            if count == 2 and board[y - 1][x] == " ":
                placed = True
                board[y - 1][x] = computer
            if count == 2 and board[y - 2][x] == " ":
                placed = True
                board[y - 2][x] = computer
            if placed is True:
                return True
    if placed is True:
        return True
    if placed is False:
        count = 0
        for x in range(3):
            if board[x][x] == player:
                count += 1
        if count == 2 and board[x][x] == " ":
            placed = True
            board[x][x] = computer
        if count == 2 and board[x - 1][x - 1] == " ":
            placed = True
            board[x - 1][x - 1] = computer
        if count == 2 and board[x - 2][x - 2] == " ":
            placed = True
            board[x - 2][x - 2] = computer
    if placed is True:
        return True
    if placed is False:
        count = 0
        for x in range(3):
            if board[x][2 - x] == player:
                count += 1
        if count == 2 and board[x][2 - x] == " ":
            placed = True
            board[x][2 - x] = computer
        if count == 2 and board[abs(x - 1)][2 - (abs(x - 1))] == " ":
            placed = True
            board[abs(x - 1)][2 - (abs(x - 1))] = computer
        if count == 2 and board[abs(x - 2)][2 - (abs(x - 2))] == " ":
            placed = True
            board[abs(x - 2)][2 - (abs(x - 2))] = computer
    if placed is False:
        return False


def turns():
    while True:
        while True:
            turn = input(f"Where would you like to place your {player}? (1-9)?\n:")
            if turn.isdigit() is True:
                if 0 < int(turn) < 10:
                    turn = int(turn)
                    break

        turn -= 1
        col = turn // 3
        row = turn % 3
        if board[col][row] == " ":
            board[col][row] = player
            break


def check_turn():
    playercount = 0
    comcount = 0
    for x in range(3):
        for y in range(3):
            if board[x][y] == player:
                playercount += 1
            if board[x][y] == computer:
                comcount += 1
    if comcount == playercount:
        return True
    else:
        return False


def poor_man_clear():
    print("\n" * 100)


def print_title():
    print(r"___       ___   ___   _   ___   ___   _    __ ")
    print(r" |    |   |      |   |-|  |      |   | |  |__ ")
    print(r" |    |   |__    |   | |  |__    |   |_|  |__ ")
    print("\n" * 2)


def clear_board():
    for x in range(3):
        for y in range(3):
            board[x][y] = " "


def thank_you():
    print(r"___        _                     _      ")
    print(r" |   |_|  |_|  |\ |  |/    \_/  | |  | |")
    print(r" |   | |  | |  | \|  |\     |   |_|  |_|")
    print("\n")


def o_won():
    display_board()
    print(r" _                 _       ")
    print(r"| | ___ \  /\  /  | |  |\ |")
    print(r"|_|      \/  \/   |_|  | \|")
    print("\n")


def x_won():
    display_board()
    print(r"                    _       ")
    print(r"\ /  ___ \  /\  /  | |  |\ |")
    print(r"/ \       \/  \/   |_|  | \|")
    print("\n")


def tie():
    print(r"___       ___")
    print(r" |    |   |__")
    print(r" |    |   |__")
    print("\n")


def loading():
    import sys
    import time

    print("Loading Game. Please Wait!")
    for i in range(0, 100):
        time.sleep(0.03)
        width = (i + 1) / 4
        bar = "[" + "#" * int(width) + " " * (25 - int(width)) + "]"
        sys.stdout.write("\u001b[1000D" + bar)
        sys.stdout.flush()
    print("\n")


def loading_screen():
    poor_man_clear()
    print_title()
    print("\n" * 2)
    loading()


board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

play_again = True

## loading_screen()

while play_again:
    poor_man_clear()
    play_again = False
    clear_board()
    poor_man_clear()
    print_title()
    board = [
        ["\u001b[31;1m1", "\u001b[31;1m2", "\u001b[31;1m3"],
        ["\u001b[31;1m4", "\u001b[31;1m5", "\u001b[31;1m6"],
        ["\u001b[31;1m7", "\u001b[31;1m8", "\u001b[31;1m9"],
    ]
    display_board()

    while True:
        xoro = input("\u001b[31;0mDo you want 'x' or 'o'?\n:")
        if xoro.lower() == "x":
            player = "X"
            computer = "O"
            break
        if xoro.lower() == "o":
            player = "O"
            computer = "X"
            break

    clear_board()
    poor_man_clear()
    print_title()
    display_board()
    # play 1
    turns()
    print_title()
    display_board()
    # play 2
    first_move("random")
    poor_man_clear()
    print_title()
    display_board()
    # play 3
    turns()
    print_title()
    display_board()
    # play4
    computer_going_to_win()
    computer_going_to_block()
    computer_turn()
    poor_man_clear()
    print_title()
    display_board()
    # play 5
    turns()
    print_title()
    display_board()
    if check_for_win("X") is True:
        poor_man_clear()
        x_won()
        thank_you()
        while True:
            again = input("Do you want to play again? (y or n)?\n:")
            if again.lower() == "y":
                play_again = True
                break
            if again.lower() == "n":
                play_again = False
                poor_man_clear()
                break
    else:
        if check_for_win("O") is True:
            poor_man_clear()
            o_won()
            thank_you()
            while True:
                again = input("Do you want to play again? (y or n)?\n:")
                if again.lower() == "y":
                    play_again = True
                    break
                if again.lower() == "n":
                    play_again = False
                    poor_man_clear()
                    break
        else:
            # play 6
            computer_going_to_win()
            if check_turn() is False:
                computer_going_to_block()
            if check_turn() is False:
                computer_turn()
            poor_man_clear()
            print_title()
            display_board()
            if check_for_win("X") is True:
                poor_man_clear()
                x_won()
                thank_you()
                while True:
                    again = input("Do you want to play again? (y or n)?\n:")
                    if again.lower() == "y":
                        play_again = True
                        break
                    if again.lower() == "n":
                        play_again = False
                        poor_man_clear()
                        break
            else:
                if check_for_win("O") is True:
                    poor_man_clear()
                    o_won()
                    thank_you()
                    while True:
                        again = input("Do you want to play again? (y or n)?\n:")
                        if again.lower() == "y":
                            play_again = True
                            break
                        if again.lower() == "n":
                            play_again = False
                            poor_man_clear()
                            break
                else:
                    # play 7
                    turns()
                    print_title()
                    display_board()
                    if check_for_win("X") is True:
                        poor_man_clear()
                        x_won()
                        thank_you()
                        while True:
                            again = input("Do you want to play again? (y or n)?\n:")
                            if again.lower() == "y":
                                play_again = True
                                break
                            if again.lower() == "n":
                                play_again = False
                                poor_man_clear()
                                break
                    else:
                        if check_for_win("O") is True:
                            poor_man_clear()
                            o_won()
                            thank_you()
                            while True:
                                again = input("Do you want to play again? (y or n)?\n:")
                                if again.lower() == "y":
                                    play_again = True
                                    break
                                if again.lower() == "n":
                                    play_again = False
                                    poor_man_clear()
                                    break
                        else:
                            # play 8
                            computer_going_to_win()
                            if check_turn() is False:
                                computer_going_to_block()
                            if check_turn() is False:
                                computer_turn()
                            poor_man_clear()
                            print_title()
                            display_board()
                            if check_for_win("X") is True:
                                poor_man_clear()
                                x_won()
                                thank_you()
                                while True:
                                    again = input(
                                        "Do you want to play again? (y or n)?\n:"
                                    )
                                    if again.lower() == "y":
                                        play_again = True
                                        break
                                    if again.lower() == "n":
                                        play_again = False
                                        poor_man_clear()
                                        break
                            else:
                                if check_for_win("O") is True:
                                    poor_man_clear()
                                    o_won()
                                    thank_you()
                                    while True:
                                        again = input(
                                            "Do you want to play again? (y or n)?\n:"
                                        )
                                        if again.lower() == "y":
                                            play_again = True
                                            break
                                        if again.lower() == "n":
                                            play_again = False
                                            poor_man_clear()
                                            break
                                else:
                                    # play 9
                                    turns()
                                    poor_man_clear()
                                    print_title()
                                    display_board()
                                    if check_for_win("X") is True:
                                        poor_man_clear()
                                        x_won()
                                        thank_you()
                                    if check_for_win("O") is True:
                                        poor_man_clear()
                                        o_won()
                                        thank_you()
                                    else:
                                        poor_man_clear()
                                        display_board()
                                        print("\n")
                                        tie()
                                        thank_you()
                                        while True:
                                            again = input(
                                                "Do you want to play again? (y or n)?\n:"
                                            )
                                            if again.lower() == "y":
                                                play_again = True
                                                break
                                            if again.lower() == "n":
                                                play_again = False
                                                poor_man_clear()
                                                break

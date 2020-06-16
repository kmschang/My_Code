from random import randint
def coltonum(x,y):
    return (x*3) + y

def display_board():
    for col in range(3):
        for row in range(3):
            print(board[col][row], end='')
            if row != 2:
                print(' | ', end='')
        print('\n')

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
            print (f"{letter} won!")
            return True
    for x in range(3):
        count = 0
        for y in range(3):
            if board[y][x] == letter:
                count += 1
        if count == 3:
            print (f"{letter} won!")
            return True
    for x in range(3):
        if board[x][x] == letter:
            count2 += 1
        if count2 == 3:
            print(f"{letter} won!")
            return True
    for x in range(3):
        if board[x][2-x] == letter:
            count3 += 1
        if count3 == 3:
            print(f"{letter} won!")
            return True

def numtocol(num):
    num -= 1
    return([num//3,num % 3])

def first_move():
    if board[1][1] != ' ':
        board[2][0] = computer
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
                if board[x][y] == ' ':
                    board[x][y] = computer
                    done = True
                    break
                if done == True:
                    break
            if done == True:
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
        if count == 2 and board[x][y] == ' ':
            placed = True
            board[x][y] = computer
        if count == 2 and board[x][y-1] == ' ':
            placed = True
            board[x][y-1] = computer
        if count == 2 and board[x][y-2] == ' ':
            placed = True
            board[x][y-2] = computer
        if placed == True:
            break
    if placed == True:
        return True
    if placed == False:
        count = 0
        for x in range(3):
            count = 0
            for y in range(3):
                if board[y][x] == computer:
                    count += 1
            if count == 2 and board[y][x] == ' ':
                placed = True
                board[y][x] = computer
            if count == 2 and board[y-1][x] == ' ':
                placed = True
                board[y-1][x] = computer
            if count == 2 and board[y-2][x] == ' ':
                placed = True
                board[y-2][x] = computer
            if placed == True:
                return True
    if placed == False:
        count = 0
        for x in range(3):
            if board[x][x] == computer:
                count += 1
        if count == 2 and board[x][x] == ' ':
            board[x][x] = computer
        if count == 2 and board [x-1][x-1] == ' ':
            board[x-1][x-1] = computer
        if count == 2 and board[x-2][x-2] == ' ':
            board[x-2][x-2] = computer
    if placed == False:
        return False

def computer_going_to_block():
    placed = False
    count = 0
    for x in range(3):
        count = 0
        for y in range(3):
            if board[x][y] == player:
                count += 1
        if count == 2 and board[x][y] == ' ':
            placed = True
            board[x][y] = computer
        if count == 2 and board[x][y-1] == ' ':
            placed = True
            board[x][y-1] = computer
        if count == 2 and board[x][y-2] == ' ':
            placed = True
            board[x][y-2] = computer
        if placed == True:
            break
    if placed == True:
        return True
    if placed == False:
        count = 0
        for x in range(3):
            count = 0
            for y in range(3):
                if board[y][x] == player:
                    count += 1
            if count == 2 and board[y][x] == ' ':
                placed = True
                board[y][x] = computer
            if count == 2 and board[y-1][x] == ' ':
                placed = True
                board[y-1][x] = computer
            if count == 2 and board[y-2][x] == ' ':
                placed = True
                board[y-2][x] = computer
            if placed == True:
                return True
    if placed == False:
        count = 0
        for x in range(3):
            if board[x][x] == player:
                count += 1
        if count == 2 and board[x][x] == ' ':
            board[x][x] = computer
        if count == 2 and board[x-1][x-1] == ' ':
            board[x-1][x-1] = computer
        if count == 2 and board[x-2][x-2] == ' ':
            board[x-2][x-2] = computer
    if placed == False:
        return False

def turns():
    while True:
        while True:
            turn = input(f"Where would you like to place your {player}? (1-9)?\n:")
            if turn.isdigit() == True:
                turn = int(turn)
                break

        turn -= 1
        col = turn//3
        row = turn % 3
        if board[col][row] == ' ':
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
    print('\n'*100)

def print_title():
    print('___''  ''   ''  ''___''   ''___''  '' _ ''  ''___''   ''___''  '' _ ''  '' __ ')
    print(' | ''  '' | ''  ''|  ''   '' | ''  ''|-|''  ''|  ''   '' | ''  ''| |''  ''|__ ')
    print(' | ''  '' | ''  ''|__''   '' | ''  ''| |''  ''|__''   '' | ''  ''|_|''  ''|__ ')
    print("\n"*2)

def clear_board():
    for x in range(3):
        for y in range(3):
            board[x][y] = ' '

board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

play_again = True

while play_again == True:
    clear_board()
    poor_man_clear()
    print_title()
    display_board()

    while True:
        xoro = input("Do you want 'x' or 'o'?\n:")
        if xoro.lower() == 'x':
            player = 'X'
            computer = 'O'
            break
        if xoro.lower() == 'o':
            player = 'O'
            computer = 'X'
            break

    poor_man_clear()
    print_title()
    display_board()
    #play 1
    turns()
    print_title()
    display_board()
    #play 2
    first_move()
    poor_man_clear()
    print_title()
    display_board()
    #play 3
    turns()
    print_title()
    display_board()
    #play4
    computer_going_to_win()
    computer_going_to_block()
    computer_turn()
    poor_man_clear()
    print_title()
    display_board()
    #play 5
    turns()
    print_title()
    display_board()
    if check_for_win('X') == True:
        again = input("Do you want to play again? (y or n)?\n:")
    else:
        if check_for_win('O') == True:
            again = input("Do you want to play again? (y or n)?\n:")
        else:
            #play 6
            computer_going_to_win()
            if check_turn() == False:
                computer_going_to_block()
            if check_turn() == False:
                computer_turn()
            poor_man_clear()
            print_title()
            display_board()
            if check_for_win('X') == True:
                again = input("Do you want to play again? (y or n)?\n:")
            else:
                if check_for_win('O') == True:
                    again = input("Do you want to play again? (y or n)?\n:")
                else:
                    #play 7
                    turns()
                    print_title()
                    display_board()
                    if check_for_win('X') == True:
                        again = input("Do you want to play again? (y or n)?\n:")
                    else:
                        if check_for_win('O') == True:
                            again = input(
                                "Do you want to play again? (y or n)?\n:")
                        else:
                            #play 8
                            computer_going_to_win()
                            if check_turn() == False:
                                computer_going_to_block()
                            if check_turn() == False:
                                computer_turn()
                            poor_man_clear()
                            print_title()
                            display_board()
                            if check_for_win('X') == True:
                                again = input(
                                    "Do you want to play again? (y or n)?\n:")
                            else:
                                if check_for_win('O') == True:
                                    again = input(
                                        "Do you want to play again? (y or n)?\n:")
                                else:
                                    #play 9
                                    turns()
                                    poor_man_clear()
                                    print_title()
                                    display_board()
                                    check_for_win('X')
                                    check_for_win('O')
                                    again = input(
                                        "Do you want to play again? (y or n)?\n:")

    if again.lower() == 'y':
        play_again = True
    if again.lower() == 'n':
        play_again = False

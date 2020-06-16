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
    for x in range(3):
        count = 0
        for y in range(3):
            if board[y][x] == letter:
                count += 1
        if count == 3:
            print (f"{letter} won!")
    for x in range(3):
        if board[x][x] == letter:
            count2 += 1
        if count2 == 3:
            print(f"{letter} won!")
    for x in range(3):
        if board[x][2-x] == letter:
            count3 += 1
        if count3 == 3:
            print(f"{letter} won!")

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
        return False

def computer_goint_to_block():
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
        return False

def turns():
    turn = int(input(f"Where would you like to place your {player}? (1-9)?\n:"))

    turn -= 1
    col = turn//3
    row = turn % 3
    board[col][row] = player

board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

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

display_board()
turns()
display_board()
first_move()
display_board()
turns()
display_board()
computer_going_to_win()
computer_goint_to_block()
computer_turn()
display_board()
turns()
display_board()
check_for_win('X')
check_for_win('O')
computer_going_to_win()
computer_goint_to_block()
computer_turn()
display_board()
check_for_win('X')
check_for_win('O')

from random import randint

while True:
    xoro = input("Do you want to be 'x' or 'o'?\n:")
    if xoro.lower() == 'x' or xoro.lower() == 'o':
        letter = xoro.upper()
        break

if letter.lower() == 'x':
    comletter = 'O'
if letter.lower() == 'o':
    comletter = 'X'

def space(num):
    print('\n'*num)

def display_board(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9])

board = ['#',' '," ",' ',' ',' ',' ',' ',' ',' ']

display_board(board)

while True:

    turn1 = int(input(f"Where do you want to place {letter} (1-9)?\n:"))

    if turn1 == 1:
        board[1] = letter
        break
    if turn1 == 2:
        board[2] = letter
        break
    if turn1 == 3:
        board[3] = letter
        break
    if turn1 == 4:
        board[4] = letter
        break
    if turn1 == 5:
        board[5] = letter
        break
    if turn1 == 6:
        board[6] = letter
        break
    if turn1 == 7:
        board[7] = letter
        break
    if turn1 == 8:
        board[8] = letter
        break
    if turn1 == 9:
        board[9] = letter
        break

space(1)
display_board(board)
space(1)

while True:
    computer1 = randint(1,9)
    if computer1 == turn1:
        computer1 = randint(1,9)
        break


board[computer1] = comletter

space(1)
display_board(board)
space(1)

while True:

    turn2 = int(input(f"Where do you want your second {letter}?\n:"))

    if turn2 == 1:
        board[1] = letter
        break
    if turn2 == 2:
        board[2] = letter
        break
    if turn2 == 3:
        board[3] = letter
        break
    if turn2 == 4:
        board[4] = letter
        break
    if turn2 == 5:
        board[5] = letter
        break
    if turn2 == 6:
        board[6] = letter
        break
    if turn2 == 7:
        board[7] = letter
        break
    if turn2 == 8:
        board[8] = letter
        break
    if turn2 == 9:
        board[9] = letter
        break

space(1)
display_board(board)
space(1)

if board[1] == letter and board[2] == letter:
    board[3] = comletter
if board[1] == letter and board[3] == letter:
    board[2] = comletter
if board[1] == letter and board[4] == letter:
    board[7] = comletter
if board[1] == letter and board[7] == letter:
    board[4] = comletter
if board[1] == letter and board[5] == letter:
    board[9] = comletter
if board[1] == letter and board[9] == letter:
    board[5] = comletter
if board[2] == letter and board[3] == letter:
    board[1] = comletter
if board[2] == letter and board[5] == letter:
    board[8] = comletter
if board[2] == letter and board[8] == letter:
    board[5] = comletter
if board[3] == letter and board[6] == letter:
    board[9] = comletter
if board[3] == letter and board[9] == letter:
    board[6] = comletter
if board[3] == letter and board[5] == letter:
    board[7] = comletter
if board[3] == letter and board[7] == letter:
    board[5] = comletter
if board[4] == letter and board[5] == letter:
    board[6] = comletter
if board[5] == letter and board[6] == letter:
    board[4] = comletter
if board[4] == letter and board[6] == letter:
    board[5] = comletter
if board[7] == letter and board[5] == letter:
    board[3] = comletter
if board[9] == letter and board[5] == letter:
    board[1] = comletter
if board[7] == letter and board[8] == letter:
    board[9] = comletter
if board[7] == letter and board[9] == letter:
    board[8] = comletter
if board[8] == letter and board[9] == letter:
    board[7] = comletter



space(1)
display_board(board)
space(1)

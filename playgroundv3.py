board = [['X', 'X', 'X'],[' ', ' ', ' '], [' ', ' ', ' ']]


def display_board():
    for col in range(3):
        for row in range(3):
            print(board[col][row], end='')
            if row != 2:
                print('\u001b[31;0m | ', end='')
            if row == 2 and col != 2:
                print('\u001b[31;0m\n---------\n', end='')
            if col == 2 and row == 2:
                print('\n')


def color_win(letter):
    letter = letter.upper()
    if board[0][0] == letter:
        zerozero = True
    else:
        zerozero = False
    if board[0][1] == letter:
        zeroone = True
    else:
        zeroone = False
    if board[0][2] == letter:
        zerotwo = True
    else:
        zerotwo = False
    if board[1][0] == letter:
        onezero = True
    else:
        onezero = False
    if board[1][1] == letter:
        oneone = True
    else:
        oneone = False
    if board[1][2] == letter:
        onetwo = True
    else:
        onetwo = False
    if board[2][0] == letter:
        twozero = True
    else:
        twozero = False
    if board[2][1] == letter:
        twoone = True
    else:
        twoone = False
    if board[2][2] == letter:
        twotwo = True
    else:
        twotwo = False

    if zerozero == True and zeroone == True and zerotwo == True:
        board[0][0] = '\u001b[32;1m' + letter
        board[0][1] = '\u001b[32;1m' + letter
        board[0][2] = '\u001b[32;1m' + letter
    if onezero == True and oneone == True and onetwo == True:
        board[1][0] = '\u001b[32;1m' + letter
        board[1][1] = '\u001b[32;1m' + letter
        board[1][2] = '\u001b[32;1m' + letter
    if twozero == True and twoone == True and twotwo == True:
        board[2][0] = '\u001b[32;1m' + letter
        board[2][1] = '\u001b[32;1m' + letter
        board[2][2] = '\u001b[32;1m' + letter
    if zerozero == True and onezero == True and twozero == True:
        board[0][0] = '\u001b[32;1m' + letter
        board[1][0] = '\u001b[32;1m' + letter
        board[2][0] = '\u001b[32;1m' + letter
    if zeroone == True and oneone == True and twoone == True:
        board[0][1] = '\u001b[32;1m' + letter
        board[1][1] = '\u001b[32;1m' + letter
        board[2][1] = '\u001b[32;1m' + letter
    if zerotwo == True and onetwo == True and twotwo == True:
        board[0][2] = '\u001b[32;1m' + letter
        board[1][2] = '\u001b[32;1m' + letter
        board[2][2] = '\u001b[32;1m' + letter
    if zerozero == True and oneone == True and twotwo == True:
        board[0][0] = '\u001b[32;1m' + letter
        board[1][1] = '\u001b[32;1m' + letter
        board[2][2] = '\u001b[32;1m' + letter
    if zerotwo == True and oneone == True and twozero == True:
        board[0][2] = '\u001b[32;1m' + letter
        board[1][1] = '\u001b[32;1m' + letter
        board[2][0] = '\u001b[32;1m' + letter

color_win('X')
display_board()

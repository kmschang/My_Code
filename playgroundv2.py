board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']]


def display_board():
    for x in range(3):
        for y in range(3):
            if board[x][y] == 'X':
                board[x][y] = '\u001b[31;1mX\u001b[37;1m'
            if board[x][y] == 'O':
                board[x][y] = '\u001b[34;1mO\u001b[37;1m'
            else:
                board[x][y] == '\u001b[37;1m '
    for col in range(3):
        for row in range(3):
            print(board[col][row], end='')
            if row != 2:
                print('\u001b[31;0m | ', end='')
            if row == 2 and col != 2:
                print('\u001b[31;0m\n---------\n', end='')
            if col == 2 and row == 2:
                print('\n')

display_board()

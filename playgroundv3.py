board = [['X', 'X', 'X'],[' ', ' ', ' '], ['O', 'O', 'O']]


def display_board():
    for x in range(3):
        count = 0
        for y in range(3):
            if board[x][y] == 'X':
                count += 1
            if count == 3:
                board[x][y] = '\u001b[32; 1mX'
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

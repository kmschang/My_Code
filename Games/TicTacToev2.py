cell = [['X',' ',' '],['X',' ',' '],['X',' ',' ']]

def coltonum(x, y):
    return (x*3) + y

def check_for_win(letter):
    for x in range(3):
        count = 0
        for y in range(3):
            if cell[x][y] == letter:
                count += 1
        if count == 3:
            print(f"{letter} won!")
    for x in range(3):
        count = 0
        for y in range(3):
            if cell[y][x] == letter:
                count += 1
        if count == 3:
            print(f"{letter} won!")
    for x in range(3):
        count = 0
        if cell[y][x] == letter:
            count += 1
        if count == 3:
            print(f"{letter} won!")
    for x in range(3):
        if cell[x][x-2] == letter:
            count += 1
        if count == 3:
            print(f"{letter} won!")

def display_board():
    for col in range(3):
        for row in range(3):
            print (cell[col][row],end = '')
            if row != 2: print (' | ',end='')
        print ('\n')

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

turn = int(input(f"Where would you like to put the first {player}? (1-9)\n:"))

turn-=1
col = turn // 3
row = turn % 3

cell[col][row] = player

display_board()

check_for_win('X')

def check_going_for_win():
    pass

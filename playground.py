letter = 'X'
print(f"\u001b[31;1m{letter}")
print(f"\u001b[31;0m{letter}")

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

from random import randint

while True:
    print(randint(0,2))

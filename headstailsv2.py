from random import randint


def poor_man_clear(num=100):
    print('\n'*num)


def headstails():
    if randint(1, 3) == 1:
        return True
    if randint(1, 3) == 2:
        return False


def again():
    while True:
        if str(input("Do you want to play again? (y or n)\n:")) == 'y':
            return True
        while True:
            if str(input("Are you sure want quit? (y or n)\n:")) == 'y':
                return False
            else:
                break
        else:
            print("Please only type 'y' for yes and 'n' for no.")


poor_man_clear(100)

while True:

    while True:

        if str(input("Do you want heads or tails?\n:")) == 'heads':
            qheads = True
            break
        else:
            qheads = False
            break

    isheads = headstails()

    if isheads == True and qheads == True:
        print("It was heads. You won!")

    if isheads == True and qheads == False:
        print("It was heads. You lost!")

    if isheads == False and qheads == False:
        print("It was tails. You won!")

    if isheads == False and qheads == True:
        print("It was tails. You lost!")

    if again() == False:
        break

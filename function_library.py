def poor_man_clear(num=100):
    '''
    This clears the screen to make it look nicer
    '''
    print('\n'*num)


def headstails():
    '''
    Make sure that you import randint before. This chooses between 1 and 2.
    '''
    from random import randint
    if randint(1, 3) == 1:
        return True
    if randint(1, 3) == 2:
        return False


def again():
    '''
    This askes you if you want to play again and askes you to confirm if you say no.
    '''
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


def lesser_of_two_evens(a, b):
    '''
    Prints the smaller number if both are even and the larger one if one or more is odd. Don't forget to add the print feature if you want to see the output.
    '''
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)

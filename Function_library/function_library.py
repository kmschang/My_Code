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


def lesser_of_two_evens(a, b):
    '''
    Prints the smaller number if both are even and the larger one if one or more is odd. Don't forget to add the print feature if you want to see the output.
    '''
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


def anaimal_crackers(text="test test"):
    '''
    Tells you if the first letter of two words is the same.
    '''
    wordlist = text.split()

    return wordlist[0].lower()[0] == wordlist[1].lower()[0]


def makes_twenty(num1, num2):

    return (num1+num2) == 20 or num1 == 20 or num2 == 20 or (num1-num2) == 20 or (num2-num1) == 20


def old_macdonald(name="macdonalds"):
    firstn = name[0:3]
    secondn = name[3::]

    return firstn.capitalize() + secondn.capitalize()


def master_yoda(sentence="We are ready"):
    word_list = sentence.split()
    reverse_word_list = word_list[::-1]
    return " ".join(reverse_word_list)


def almost_there(num):

    return (abs(num-100)) <= 10 or (abs(num+100)) <= 10 or (abs(num-200)) <= 10 or (abs(num+200)) <= 10


def seconds_old():
    secinday = 86400
    secinyear = 31536000
    year = int(input("What year were you born in?\n:"))
    yearold = (2020 - year)*secinyear

    month = int(input("What month were you born?\n:"))
    if month == 1:
        monthdays = 0
    if month == 2:
        monthdays = 31
    if month == 3:
        monthdays = 59
    if month == 4:
        monthdays = 90
    if month == 5:
        monthdays = 120
    if month == 6:
        monthdays = 151
    if month == 7:
        monthdays = 181
    if month == 8:
        monthdays = 212
    if month == 9:
        monthdays = 243
    if month == 10:
        monthdays = 273
    if month == 11:
        monthdays = 304
    if month == 12:
        monthdays = 334
    monthold = monthdays * secinday

    day = int(input("What day of the month were you born?\n:"))
    dayold = day * secinday

    secold = yearold + monthold + dayold

    return (secold)


def minutes_old():
    secinday = 86400
    secinyear = 31536000
    year = int(input("What year were you born in?\n:"))
    yearold = (2020 - year)*secinyear

    month = int(input("What month were you born?\n:"))
    if month == 1:
        monthdays = 0
    if month == 2:
        monthdays = 31
    if month == 3:
        monthdays = 59
    if month == 4:
        monthdays = 90
    if month == 5:
        monthdays = 120
    if month == 6:
        monthdays = 151
    if month == 7:
        monthdays = 181
    if month == 8:
        monthdays = 212
    if month == 9:
        monthdays = 243
    if month == 10:
        monthdays = 273
    if month == 11:
        monthdays = 304
    if month == 12:
        monthdays = 334
    monthold = monthdays * secinday

    day = int(input("What day of the month were you born?\n:"))
    dayold = day * secinday

    secold = yearold + monthold + dayold
    minold = secold / 60
    return int((minold))


def black_jack(num1, num2, num3):
    if num1+num2+num3 > 21:
        return 'Bust'
    else:
        return num1+num2+num3


def check_even(num):
    return num % 2 == 0


def square(num):
    return num**2


def loading2():
    import sys
    import time
    print("Loading progress bar...")
    for i in range(0, 100):
        time.sleep(0.05)
        width = (i + 1) / 4
        bar = "[" + "#" * int(width) + " " * (25 - int(width)) + "]"
        sys.stdout.write(u"\u001b[1000D" + bar)
        sys.stdout.flush()
    print("\n")


def one_ten():
    # Makes sure that you only out in integers.
    while True:
        try:
            question = int(input("Pick a number 1-10.\n:"))
        except:
            print("Please only input integers. Thank you.")
            question = ("Try again.")
        else:
            if question > 0 and question < 11:
                break
            else:
                print ('Please only input integers 1-10. Thank you.')



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


def againv2():

    while True:
        try:
            yorn = int(input("Do you want to play again? (1 = yes or 0 = no)\n:"))
        except:
            print("Please only input 1 for yes or 0 for no. Thank you.")
        else:
            if yorn == 1:
                return True
            elif yorn == 0:
                return False
            else:
                print("Please only input 0 or 1.")


againv2()
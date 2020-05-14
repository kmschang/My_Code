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

def poor_man_clear(num=100):
    print("\n"*num)


def again():
    while True:
        question = input("Do you want to play again? (y or n)\n:")
        if question.lower() == 'n':
            return False
        if question.lower() == 'y':
            return True


yes = True

while yes == True:

    while True:
        poor_man_clear(100)
        question2 = input("'yes' or 'no'\n:")
        if question2.lower() == 'yes':
            print("You lost! LOL.\n")
            break
        if question2.lower() == 'no':
            print("You won! Good Job.\n")
            break
        else:
            print("Please type eith 'yes' or 'no'.")

    if again() == False:
        break

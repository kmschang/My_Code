def poor_man_clear(num=100):
    print('\n'*num)

while True:
    try:
        num = int(input("How many spaces do you want to clear?\n:"))
    except:
        print("Please only input integers. Thank you")
        num = "Try again."
    else:
        if num > 0 and num < 101:
            break
        else:
            print('Please only use numbers 1-100. Thank you')

poor_man_clear(num)
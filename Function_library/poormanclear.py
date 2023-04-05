def poor_man_clear(num=100):
    while True:
        try:
            num = int(input("How many spaces do you want to clear?\n:"))
        except ValueError:
            print("Please only input integers. Thank you")
        else:
            if num > 0 and num < 101:
                break
            else:
                print("Please only use numbers 1-100. Thank you")

    print("\n" * num)


poor_man_clear()


def clear_screen():
    print("\033[H\033[J")

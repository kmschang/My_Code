check = int(input("What number do you want to check?\n:"))


def is_prime(num):
    for number in range(2, num):
        if num % number == 0:
            return False
    else:
        return True


print(is_prime(check))


def binary_input():
    while True:
        cont = True
        question = input("Enter binary number\n:")

        for num in question:
            if num != "1" and num != "0":
                print("Please only input binary (1 or 0). Thank you.")
                cont = False
                break

        if cont == True:
            return question


def conversion(num):
    length = len(num)
    n = 0
    values = []
    for digit in num:
        binary_number = num[length-(1+n)]
        binary_number_int = int(binary_number)
        expoential_number = (2**(0+n))
        addition = binary_number_int*expoential_number
        values.append(addition)
        n += 1

    while len(values) != 1:
        values_length = len(values)
        values.append(values[0]+values[1])
        values.pop(0)
        values.pop(0)

        if len(values) == 1:
            break

    output = values[0]

    return output


print(conversion(binary_input()))

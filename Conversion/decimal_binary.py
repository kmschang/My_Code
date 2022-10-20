def integer_input():
    while True:
        try:
            question = int(input("Pick an integer.\n:"))
        except:
            print("Please only input integers. Thank you.")
        else:
            if isinstance(question, int):
                return question


def conversion(num):
    n = 0

    if num == 1:
        return 1

    values = []
    while num != 0:
        values.append(str(num % 2))
        num = num // 2

    while len(values) != 1:
        values_length = len(values)
        values.append(values[-1 - n] + values[-2 - n])
        values.pop(-2)
        values.pop(-2)
        if values_length == values_length:
            pass

        n += 0

        if len(values) == 1:
            return values[0]


print(conversion(integer_input()))

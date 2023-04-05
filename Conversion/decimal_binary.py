def integer_input():
    while True:
        try:
            question = int(input("Pick an integer.\n:"))
        except ValueError:
            print("Please only input integers. Thank you.")
        else:
            if isinstance(question, int):
                return question


def conversion(num):
    if num == 1:
        return 1

    values = []
    while num != 0:
        values.append(str(num % 2))
        num = num // 2

    while len(values) != 1:
        len(values)
        values.append(values[-1] + values[-2])
        values.pop(-2)
        values.pop(-2)

        if len(values) == 1:
            return values[0]


print(conversion(integer_input()))

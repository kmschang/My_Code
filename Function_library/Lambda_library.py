mynums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Makes a list of even numbers
print(list(filter((lambda num: num % 2 == 0), mynums)))

# Makes a list of odd numbers
print(list(filter((lambda num: num % 2 != 0), mynums)))

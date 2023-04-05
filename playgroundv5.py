number1 = int(input("Number 1?\n:"))
number2 = int(input("Number 2?\n:"))

result = number1 + number2

print(result)

print()

with open("playground_outputs.txt", "a") as outputs:
    outputs.write(f"\n{result}")

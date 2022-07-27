n = 0

Kyle = 17

from random import randint

numbers = []
addition = []
meanlist = []
newnumber = 0
for _ in range(100):
    while n < 10:
        numbers.append(randint(0, 100))
        n += 1

    addition = sum(numbers)
    mean = addition / n
    meanlist.append(mean)

    n = 0

    numbers = []
print(meanlist)

## "What is his name"

n = 0

from random import randint

numbers = []
addition = []
meanlist = []
x=0

while x < 100:
    while n < 10:
        numbers.append(randint(0,100))
        n+=1

    addition = sum(numbers)
    mean = addition/n
    meanlist.append(mean)

    n=0

    numbers = []
    newnumber = 0
    x+=1


print(meanlist)
'''
This is a playgroung file
'''
n = 0

from random import randint

numbers = []
means = []
meanlist = []
x=0

while x < 100:
    while n < 10:
        numbers.append(randint(0,100))
        n+=1

    while len(numbers) > 1:
        newnumber = numbers[0] + numbers[1]
        numbers.append(newnumber)
        numbers.pop(0)
        numbers.pop(0)

    means.append (numbers[0]/n)
    n=0

    numbers = []
    newnumber = 0
    x+=1
    
print(means)
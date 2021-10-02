
from random import randint
from math import ceil

numbers = []
n = 0
y = 0

while n < 10:
    numbers.append(randint(0, 100))
    n += 1

mean = sum(numbers) / n

print("X̄ = " + str(mean))

distancemean = []


while y < 10:
    distancemean.append(numbers[y]-mean)
    y += 1

SD = sum(distancemean)

SDreal = SD / y

print("σ = " + str(SDreal))

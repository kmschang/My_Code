while True:

    num = int(input("What number do you want to check?\n:"))

    if num > 1:

       for numb in range(2,num):
           if (num % numb) == 0:
               print(f"{num} is not a prime number.")
               print(f"{numb} times {num // numb} is {num}.")
               break
       else:
           print(f"{num} is a prime number.")

    if num <= 0:

        print ("Please only put in whole numbers.")

    if num == 666:

        print ("Your operation has been stopped.")
        break

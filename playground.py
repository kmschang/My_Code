def splicer(mylist):
    if len(mylist)%2 == 0:
        return ("Even")
    else:
        return mylist

mylist = ['Kyle','Nathan','Katelyn']

for name in map(splicer,mylist):
    print (name)

def check_even(num):
    return num%2 == 0

mynums = [1,2,3,4,5,6,7,8]

for num in filter(check_even,mynums):
    print (num)
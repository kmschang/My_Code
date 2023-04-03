def binary():
    x = "{:b}".format(
        1859718347812739481235781674623847901283498123948213567861271083567816308478934708917238496357106982374897123896571620849723894782365781032784682342434689027
    )

    while True:
        if x == 1:
            x = "\u001b[37; 1m" + x
        if x == 0:
            x = "\u001b[37;1m" + x
        print(x)
        x = x * 7


def counter():
    x = 1

    while True:
        print(x)
        x += 1


ques = str(input("Do you want binary or counter?\n:"))

if ques.lower() == "binary":
    print(binary())
elif ques.lower() == "counter":
    print(counter())
else:
    print("There is nothing like that here. Please try again.")

    # this is a test

slogin = False

while slogin is False:
    tname = False
    tmail = False
    tpass = False

    print(
        "If you are new, type 'm' to make a new login, if you just make a login, type 'l' to login.\nIf you want to "
        "leave just type end."
    )
    question = input("Do you want to login (l) or make a login (m)?\n:")
    nques = question.lower()

    if nques == "m":
        while True:
            name = input("what is your name?\n:")
            capname = name.capitalize()

            if name == "end":
                print("Your operation has been ended.")
                break

            while True:
                yn = input(f"Are you sure you want {name} as your name? (y or n)?\n:")

                if yn == "y":
                    tname = True
                    bk = True
                    break

                if yn.lower() == "end":
                    print("Your operation has been ended.")
                    break

                else:
                    print("Yes (y) or No (n) please.")
                    bk = False
                    break

            if bk is True:
                break

        while tname is True:
            email = input(f"{capname}, what is your email?\n:")

            if email == "end":
                print("Your operation has been ended.")
                break

            while True:
                yn = input(f"Are you sure you want {email} as your email? (y or n)?\n:")

                if yn == "y":
                    tmail = True
                    bk = True
                    break

                if yn.lower() == "end":
                    print("Your operation has been ended.")
                    break

                else:
                    print("Yes (y) or No (n) please.")
                    bk = False
                    break

            if bk is True:
                break

        while tmail is True:
            password = input(f"{capname}, what password do you want for {email}?\n:")

            if password == "end":
                print("Your operation has been ended.")
                break

            while True:
                yn = input(
                    f"Are you sure you want {password} as your password? (y or n)?\n:"
                )

                if yn == "y":
                    tpass = True
                    bk = True
                    break

                if yn.lower() == "end":
                    print("Your operation has been ended.")
                    break

                else:
                    print("Yes (y) or No (n) please.")
                    bk = False
                    break

            if bk is True:
                break

    if nques == "l":
        tpass = True
        cornam = False
        login = False
        admin = False

        while tpass is True:
            inname = input("What is you name?\n:")

            if inname.lower() == "admin":
                cornam = True
                admin = True
                break

            if inname.lower() == name.lower():
                print(f"Hello {capname}")
                cornam = True
                break

            if inname.lower() == "end":
                print("Your operation has been ended.\n")
                break

            else:
                print("You are not in our system. Please Try again.\n")

        while cornam is True:
            if admin is True:
                break
            else:
                inmail = input(f"What is your email {capname}?\n:")

                if inmail.lower() == "end":
                    print("Your operation has been ended.\n")
                    break

                if inmail.lower() == email.lower():
                    while True:
                        inpass = input(f"What is your password {capname}?\n:")

                        if inpass.lower() == "end":
                            print("Your operation has been ended.\n")
                            break

                        if inpass == password:
                            print(f"Welcome {capname}!")
                            login = True
                            break

                        else:
                            print("Incorrect password! Please try again.")

                    break

                else:
                    print("Incorrect e-mail! Please try again.")

            if login is True:
                print("This is where you put your secret.")
                slogin = True

            break

    if nques == "end":
        break
    print("You passed the test")

import userFunctions


def login():
    while True:
        user = input("Please enter your employee id or student id , it must be starting with e or s")
        if 'e' in user:
            return user
        elif 's' in user:
            return user
        else:
            print("invalid input , must be employee or student")


def menu_staff():
    while True:
        print("*"*52)
        print(" **************Employee vending machine **************")
        print("*" * 52)
        print("E1. Buy")
        print("E2. Add")
        print("E3. Display item")
        print("E4. Quit")
        choice = input("your input choice from [E1-E4]: ")
        choice = choice.upper()
        if choice == "E1" or choice == "E2" or choice == "E3" or choice == "E4":
            return choice
        else:
            print("Invalid choice")


def menu_student():
    while True:
        print("*"*40)
        print("*******  Student vending machine *******")
        print("*" * 40)
        print("S1. Buy")
        print("S2. Display item")
        print("S3. Quit")
        choice = input("your input choice from [S1-S3]: ")
        if choice == "S1" or choice == "S2" or choice == "S3":
            return choice
        else:
            print("Invalid choice")


def main():
    userFunctions.load_vm()
    userFunctions.disp()
    userID = login()
    while True:
        print("welcome to python vending machine")
        if 'e' in userID:
            option = menu_staff()
        elif 's' in userID:
            option = menu_student()
        if option == "E1" or option == "S1":
            userFunctions.buy_item(userID)
        elif option == "E2":
            userFunctions.add_item()
        elif option == "E3" or option == "S2":
            userFunctions.disp()
        elif option == "E4" or option == "S3":
            userFunctions.quit_vm()
            break
        else:
            print(option)
            print("invalid menu option")


print(f"the name is : {__name__}")

if __name__ == '__main__':
    main()



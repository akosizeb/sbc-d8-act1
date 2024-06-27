usernames = {}

def register(username, password):
    write = open("storage.txt", "a")
    usernames[username] = password
    if username in usernames:
        print(f"Username: {username} Password: {usernames[username]}", file=write)
        print(f"\nHi {username} Your Successfuly Registered Your Account!")
        write.close()
    else:
        print(f"The Username {username} Is Already Exist!")

def login(username, password):
    if username in usernames and password in usernames[username]:
            print(f"\nHi {username}, You have successfully logged in!")
    else:
        print("Invalid Username or Password. Please Check and Please Try Again.")
    return False

def change_password(username, old_password, new_password):
    write = open("storage.txt", "a")
    if username in usernames and password in usernames[username]:
            usernames[username] = new_password
            print(f"Username: {username} Password: {usernames[username]}", file=write)
            print(f"Password for {username} Has Been Changed!")
            write.close()
    else:
            print("Invalid Username or Password. Please try again.")

while True:
    print("\nOptions: PILIA ANG NAA SA OPTION DILI KAY MAGPATAKA KAG BUTANG SA NUMBER!!! ")
    print("\n1. Register")
    print("\n2. Login")
    print("\n3. Change Password")
    print("\n4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        username = input("\nEnter Username: ")
        password = input("\nEnter Password: ")
        register(username, password)
    elif choice == '2':
        username = input("\nEnter username: ")
        password = input("\nEnter password: ")
        if login(username, password):
            
            pass
    elif choice == '3':
        username = input("\nEnter username: ")
        old_password = input("\nEnter old password: ")
        new_password = input("\nEnter new password: ")
        change_password(username, old_password, new_password)
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid Choice! Please Select a Valid Option.")
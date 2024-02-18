import pyinputplus as pyip

# Global dictionary to store user data
users = {}


def print_users():
    print(users)


def register_user():
    username = pyip.inputStr("Enter a username: ")
    while username in users:
        print("Username already exists. Please choose another one.")
        username = pyip.inputStr("Enter a username: ")

    password = pyip.inputPassword("Enter a password: ")

    users[username] = {'password': password}
    print(f"User {username} registered successfully!")


def login():
    username = pyip.inputStr("Enter your username: ")
    password = pyip.inputPassword("Enter your password: ")

    if username in users and users[username]['password'] == password:
        print(f"Welcome, {username}!")
    else:
        print("Invalid username or password.")


def list_users():
    if users:
        print("\nList of users:")
        print_users()
        # for username in users:
        #     print(username)
    else:
        print("No users found.")


def change_password():
    username = pyip.inputStr("Enter your username: ")
    if username in users:
        new_password = pyip.inputPassword("Enter your new password: ")
        users[username]['password'] = new_password
        print(f"Password for user {username} changed successfully!")
    else:
        print("User not found.")


def delete_user():
    username = pyip.inputStr("Enter the username to delete: ")
    if username in users:
        del users[username]
        print(f"User {username} deleted successfully!")
    else:
        print("User not found.")


def main():
    while True:
        print("\n1. Register\n2. Login\n3. List users\n4. Change Password\n5. Delete User\n6. Exit\n")
        choice = pyip.inputChoice(
            ['1', '2', '3', '4', '5', '6'], prompt="Select an option: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            login()
        elif choice == '3':
            list_users()
        elif choice == '4':
            change_password()
        elif choice == '5':
            delete_user()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break


if __name__ == "__main__":
    main()

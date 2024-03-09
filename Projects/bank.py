'''
This is a simple bank application. 

1. Create account
2. Deposit
3. Withdraw
4. Check Balance
5. Exit

'''

import json

ACCOUNTS_FILE = "accounts.json"


def load_accounts():
    try:
        with open(ACCOUNTS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_accounts(accounts):
    with open(ACCOUNTS_FILE, 'w') as file:
        json.dump(accounts, file, indent=2)

def create_account(accounts, account_number, account_holder):
    accounts[account_number] = {"holder": account_holder, "balance": 0}
    save_accounts(accounts)
    print("Account created successfully.")

def deposit(accounts, account_number, amount):
    if account_number in accounts:
        accounts[account_number]["balance"] += amount
        save_accounts(accounts)
        print(f"Deposited ${amount}. New balance: ${accounts[account_number]['balance']}")
    else:
        print("Account not found.")


def withdraw(accounts, account_number, amount):
    if account_number in accounts:
        if 0 < amount <= accounts[account_number]["balance"]:
            accounts[account_number]["balance"] -= amount
            save_accounts(accounts)
            print(f"Withdrew ${amount}. New balance: ${accounts[account_number]['balance']}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
    else:
        print("Account not found.")

def check_balance(accounts, account_number):
    if account_number in accounts:
        print(f"Account Balance for {accounts[account_number]['holder']}: ${accounts[account_number]['balance']}")
    else:
        print("Account not found.")


def main():
    accounts = load_accounts()

    print(accounts)

    while True:
        print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder name: ")
            create_account(accounts, account_number, account_holder)

        elif choice == '2':
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            deposit(accounts, account_number, amount)

        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            withdraw(accounts, account_number, amount)

        elif choice == '4':
            account_number = input("Enter account number: ")
            check_balance(accounts, account_number)

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()

import json 

# users = []


# try:
#     with open('user.json') as f:
#         data = json.load(f)
#         if data:
#             users = data
# except Exception:
#     print('ther is error')

# def add_user(users):
#     print(users)

#     name = input("Enter your name: ")
#     age = input("Enter Your age: ")
#     number = input("Enter you Number: ")

#     user = {
#         "name":name,
#         "age": age,
#         "number":number
#     }

#     users.append(user)

#     print(users)

#     with open('user.json','w') as f:
#        json.dump(users,f)



# while True:

#     print('1. register')
#     print('2. list users')
#     print('3. exit')

#     i = input()

#     if i == '1':
#         add_user(users)
#     elif i == '2':
#         print(users)
#     elif i == '3':
#         break



# create account
    # account number
    # name 
    # amount



# json.load() # file object
# json.loads() # string 

# json.dump() # data object, file object
# json.dumps() # data 


def save_accounts(accounts):
       with open('user.json','w') as f:
            json.dump(accounts,f,indent=2)

accounts = {}
try:
    with open('user.json') as f:
        data = json.load(f)
        if data:
            accounts = data
except Exception:
    pass


def create_account(accounts):

    account_number = input("Enter  Your Accountn No.: ")
    name = input("Enter your name: ")
    amount = int(input("Enter Amount: "))

    isExists = account_number in accounts

    if isExists:
        print("This Account number alread exists try another.")
    else:
        accounts[account_number] = {
            'name': name,
            "amount":amount
        }
        print(accounts)
        save_accounts(accounts)
     

def deposit(accounts):
    account_no = input('Enter you account no: ')
    amount = int(input("Enter Amount: "))
    if accounts.get(account_no, False):
        accounts[account_no]['amount'] += amount
        save_accounts(accounts)
    else:
        print("This account no not exists")


def withdraw(accounts):
    account_no = input('Enter you account no: ')
    amount = int(input("Enter Amount: "))

    if accounts.get(account_no, False):
        if amount>0 and amount <= accounts[account_no]['amount']:
            accounts[account_no]['amount'] -= amount
            save_accounts(accounts)
    else:
        print("This Accountn no is not exists!")


def display(accounts):
    account_no = input("Enter your account no: ")

    if accounts.get(account_no, False):
        name = accounts[account_no]['name']
        amount = accounts[account_no]['amount']
        print(f"Hello {name}, Your account balance is {amount}")
    else:
        print("no account with this acount no!")
# create_account(accounts)
# deposit(accounts)
# withdraw(accounts)
        

while True:

    print("1. create")
    print("2. deposit")
    print("3. witdraw")
    print("4. display")
    print("5. exit")

    i = input()

    if i == '1':
        create_account(accounts)
    elif i == '2':
        deposit(accounts)
    elif i == '3':
        withdraw(accounts)
    elif i == '4':
        display(accounts)
    elif i == '5':
        break
    else:
        print("you have selected wrong option")

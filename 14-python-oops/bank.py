

class Account:
    def __init__(self, account_holder, balance, account_number):
        self.account_holder = account_holder
        self.account_number = account_number
        self.__balance = balance
    
    @property
    def balance(self):
        print("getting balance")
        return self.__balance
class User:
    def __init__(self, name, initial_balance):
        self.name = name
        self.account = None

    def create_account(self, account_number, initial_balance):
        self.account = Account(self.name, initial_balance, account_number)

user1 = User("John", 1000)
print(user1.account)
user1.create_account("12345", 1000)
print(user1.account.balance)
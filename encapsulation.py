#class is BankAccount with a private attribute that is balance
# should have the function to deposit and also withdraw
# balance should not be accessed or modified outside the class outside the class
# In general, it should be able to perform deposit and withdraw while maintaining encapsulation
class BankAccount:
    def __init__(self, balance=0):
        # to encapsulate the balance i need to add two underscores before balance
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return f"amount can't be zero"
        self.__balance += amount
        print(f"{amount} has been deposited successfully,your balance is: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            return f"Insufficient funds"
        self.__balance -= amount
        print(f"{amount} has been withdrawn successfully,your balance is: {self.__balance}")



account = BankAccount()
account.deposit(1000)
account.withdraw(500)












# Implement the basic structure of a parent class Account and a child class SavingAccount.


class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount=0):
        self.balance = self.balance + amount

    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            print("Insufficient balance to withdraw.")


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.interestRate * self.balance) / 100


account = SavingsAccount("Mark", 5000, 5)
print(account.get_balance())
print(account.interestAmount())

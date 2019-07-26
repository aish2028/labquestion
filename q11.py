class Account:

    def __init__(self,accno,name,balance):
        self.accno=accno
        self.name=name
        self.balance=balance

    def deposit(self,deposit_amount):
        self.balance += self.deposit_amount
        print(f"enter depositing the balance is:{self.balance}")
    def withdraw(self,withdraw_amount):
        self.balance += self.withdraw_amount
    def showinfo(self):
        pass

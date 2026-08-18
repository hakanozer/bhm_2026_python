from .BankAccount import BankAccount

class Customer(BankAccount):
    def __init__(self, name, number: int, balance: int):
        self.name = name
        self.number = number
        self.balance = balance

    def accountNumber(self):
        return self.number

    def balanceAmount(self):
        return self.balance

    def showInfo(self):
        print(f"Müşteri : {self.name}")
        print(f"Hesap No : {self.number}")
        print(f"Bakiye : {self.balance}")
      
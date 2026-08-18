from abc import ABC, abstractmethod

class BankAccount(ABC):

    @abstractmethod
    def accountNumber(self) -> int:
        pass

    @abstractmethod    
    def balanceAmount(self) -> int:
        pass


    def deposit(self, amount):
        self.number = self.accountNumber()
        self.balance = self.balanceAmount()
        if (amount > 0):
            self.balance += amount
        else:
            print("Negatif Değer Girilemez")


    def withdraw(self, amount):
        self.number = self.accountNumber()
        self.balance = self.balanceAmount()
        if (amount < self.balance):
            self.balance -= amount
        else:
            print("Yetersiz Bakiye!")

            



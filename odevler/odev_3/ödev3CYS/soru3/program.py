from abc import ABC,abstractmethod

class BankAccount:

    @abstractmethod
    def accountNumber(self) -> int:
        pass 

    def showAccount(self):
        self.number = self.accountNumber()
        return print(f"Hesap Numaranız : {self.number}")


class Customer(BankAccount):
    def __init__(self, number: int):
        self.number = number

    def accountNumber(self):
        return self.number
        


customer = Customer(100)
print(customer.accountNumber())
customer.showAccount()



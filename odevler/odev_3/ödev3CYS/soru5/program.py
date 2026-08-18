from .Customer import Customer


customer = Customer("Çağın",100,1000)
print("Başlangıç------------")
customer.showInfo()

print("Deposit 500-------------------")
customer.deposit(500)
customer.showInfo()

print("Withdraw 2000---------------")
customer.withdraw(2000)
customer.showInfo()

print("Withdraw 300-------------")
customer.withdraw(300)
customer.showInfo()


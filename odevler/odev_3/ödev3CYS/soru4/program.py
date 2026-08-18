class Employee:
    def work():
        pass

class Developer(Employee):
    def work(self):
        return print("Yazılım Geliştiriyor")
        

class Manager(Employee):
    def work(self):
        return print("Ekibi Yönetiyor")

def showWork(employee):
    employee.work()


developer = Developer()
manager = Manager()

showWork(developer)
showWork(manager)
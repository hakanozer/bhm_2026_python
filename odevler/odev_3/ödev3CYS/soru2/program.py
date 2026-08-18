class Person:
    def __init__(self, name):
        self.name = name
        pass

class Student(Person):
    def __init__(self, name, studentNumber):
        self.studentNumber = studentNumber
        super().__init__(name)

    def showInfo(self):
        print(f"Öğrenci: {self.name}")
        print(f"Numara: {self.studentNumber}")


student = Student("Çağın",12345)
student.showInfo()

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Köpek havlıyor"

class Cat(Animal):
    def speak(self):
        return "Kedi Miyavlıyor"

dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())
class Dog:
    pass
dog0 = Dog()
dog0.name = "dog0 name"
dog0.age = "dog0 age"

print(dog0.name)
class Dog:
    def __init__(self, name, age):
        self.name = name

        self.age = age

dog1 = Dog("Tyson", 6)
dog2 = Dog("Bruno", 5)

print(f"{dog1.name} is my first dog and it is {dog1.age} years old")

print(f"{dog2.name} is my first dog and it is {dog2.age} years old")
print()

class Cat:
    created = 0 # static values
    def __init__(self, name = "Milo", age = 12, color = "white", sound = "miau miau"):
        self.name = name
        self.age = age
        self.color = color
        self.sound = sound

    def __str__(self):
        return f"Soy un gato llamado {self.name}"

    def bark(self, times):

        for i in range(times):
            print(self.sound)
        return

milo = Cat()
noni = Cat("Noni", 20, "brown")

print(milo)
milo.bark(2)
print()
print(noni)
noni.bark(4)
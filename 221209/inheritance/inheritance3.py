# Polymorphism

class Animal:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method!")
    
class Cat(Animal):
    def talk(self):
        return "미야옹"

class Dog(Animal):
    def talk(self):
        return "멍멍"

animals = [Cat("노랑이"), Cat("고냥이"), Dog("멍멍이")]

for animal in animals:
    print(animal.name + ': ' + animal.talk())
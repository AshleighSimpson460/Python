# multi-level inheritance = when a derived (child) class inherits another derived (child) class

class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print("This animal is eating")
class Dog(Animal):
    def bark(self):
        print("This dog is barking")

dog = Dog()

print(dog.alive)
print(dog.eat())
print(dog.bark())

# the dog inherits the eat()  method from the Animal class and the alive from the Organism class-  this is an example of multi-level inheritance
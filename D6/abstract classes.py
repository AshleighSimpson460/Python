# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation.

# prevents a user from creating an object of that class it compels a user to override abstract methods in a child class

from abc import ABC, abstractmethod # this will create abstract classes / methods

class Vehicle(ABC): # We put ABC in the parantheses to make the class abstract
    @abstractmethod # this will make the go method an abstract method
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car") # these will not print as we created an object of the parent class
    def stop(self):
        print("This car will stop")
class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")
    def stop(self):
        print("This motorcycle will stop")

# all the children classes must override the abstract method in the parent class as well as have def go(self) in order for the program to run.
        # if we do not have def go(self) in the child class, the program will not run.
        # Children must override their parent class abstract methods. By adding its own implementation
car = Car()
# vehicle = Vehicle()
motorcycle = Motorcycle()   
# print(vehicle.go())
        
car.go()

# the benefits of having abstract classes is that it prevents users from creating an object of that class
class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def slumber(self):
        print("This animal is slumbering")

class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")
    def eat(self):
        print("This rabbit is eating a carrot") # this is known as method overriding
class Fish(Animal):
    def swim(self):
        print("This fish is swimming")
    def eat(self):
        print("This fish is eating a worm") # this is known as method overriding
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")
    def eat(self):
        print("This hawk is eating a worm") # this is known as method overriding

# Parents can have their own methods and the Children which are the rabbit, fish and hawk can inherit the parents methods as well as have their own

Rabbit = Rabbit()
Rabbit.eat() # This method was inherited by the parent class 'Animal' but we used method override to make the eat more specific
from car import Car

# the difference between a class variable and instance variable is that you can set the class variable outside of an instance and it will represent
    # all instances and an instance variable is a unique variable.

wheels = 4 # class variable


Car_1 = Car("Volkswagen", "E-Golf", 2020, "Navy")
Car_2 = Car("Ford","Mustang",2022,"red")

print(Car_2.make)
print(Car_2.model)
print(Car_2.year)
print(Car_2.color)

Car_1.drive()
Car_2.stop()
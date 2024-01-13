# str.format() = optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

# print("The {} jumped over the {}".format(animal, item))
# # The cow jumped over the moon

# print("The {1} jumped over the {0}".format(animal, item)) # positional arguments
# The moon jumped over the cow

# print("The {animal} jumped over the {item}".format(animal = "cow", item = "moon")) # keyword arguments

# you can reuse arguments to show the same words in the logs.

text = "The {} jumped over the {}"

print(text.format(animal, item))

name = "Ashleigh"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:<10}. Nice to meet you".format(name))
print("Hello, my name is {:^10}. Nice to meet you".format(name))
print("Hello, my name is {:>10}. Nice to meet you".format(name))

number = 3.14159

print("The number pi is {:.2f}".format(number)) # f means floating point numbers so it stands for 2 floating points (2 decimal places)
print("The number is {:,}".format(number)) # this will place a comma at every thousand place (if the number is bigger than a thousand)
print("The number is {:b}".format(number)) # this will put the number in binary
print("The number is {:o}".format(number)) # this will put the number in octal
print("The number is {:x}".format(number)) # this will put the number in hexadecimal
print("The number is {:E}".format(number)) # this will put the number in scientific notation

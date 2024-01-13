#inputs give you a value of the string data type.
#if you need to use the value for any sort of math youll need to convert it to a number 
#using int() or float() depending if it is a whole number or decimal.


# name = input("What is your name?: ")
# age = int(input("What is your age?: "))
# height = float(input("What is your height: "))cl
# hobby = input("What is your hobby?: ")

# print("Hello " + name)
# print("You are " + str(age) + " years old")
# print("You are " + str(height) + "ft tall")
# print("Your hobby is " + hobby)



import math

pi = 3.14

#print(round(pi)) #rounds to the nearest whole number
#print(abs(-3)) #returns the absolute value of a number)

#print(math.ceil(pi)) #rounds up to the nearest whole number
#print(math.floor(pi)) #rounds down to the nearest whole number
#print(math.sqrt(pi)) #returns the square root of a number
#print(math.pow(pi, 2)) #returns the power of a number
# print(math.log(pi)) #returns the log of a number
# print(math.log10(pi)) #returns the log of a number in base 10
#print(math.pow(2, 10)) #returns the power of a number
#print(math.max(2, 10)) #returns the max of varaibles numbers
#print(math.min(2, 10)) #returns the min of varaibles numbers)





#slicing = create a substring by extracting elements from another string indexing[] or slice()
# [start:stop:step] is how indexing works in python
# step is how many elements you want to skip automatically it is set to 1 by default

name = "Ashleigh Simpson"

first_name = name[0:8]
last_name = name[9:]
weird_name = name[::3] #or name[::2]python will fill in the blank spaces
# you can leave the 0 blank to start at the beginning of the string
name_reversed = name[::-1] #or name[::-2]python will fill in the blank spaces

# print(name_reversed)


slice = slice(7,-4) #slices from the 7th element to the end it also slices from the end to the 4th element 
# but it does not include the 4th element

website1 = "http://google.com"
website2 = "http://youtube.com"

# print(website2[slice])




# if statement = a block of code that will execute if it's condition is true
#code for if statements run in order - if the first statement is true the rest of the statements will not run 
#for example if the first statement is false the rest of the statements will not run even if the second statement is == and true

# age = int(input("How old are you?: "))

# if age == 100:
#     print("You have been on earth for a century")
# elif age >= 18:
#     print("You are an adult")
# elif age < 0:
#     print("You haven't been born yet")
# else: 
#     print("You are not an adult")

# logical operators = used to combine conditional statements and checks if two or more conditional statements are true

temp = int(input("What is the temperature outside?: "))

# if temp <= 0 and temp >= 30:
#     print("The temperature is good")
#     print("Go outside")
# elif temp > 0 or temp < 30:
#     print("The temperature is bad")
#     print("Stay inside")    

#if you wrap the if statement with the not logical operator it will reverse the condition see example below
    
if not(temp <= 0 and temp >= 30):
    print("The temperature is bad")
    print("Stay inside")    
elif not(temp >= 0 or temp < 30):
    print("The temperature is good")
    print("Go outside")
    


# while loop = a loop that will execute it's block of code as long as it's condition is true,
    #   as long as the condition is true the code will keep running

# username = ""

# while len(username) == 0:
#     username = input("Enter your username: ")

# print("Hello " + username)

#if you use not once again it will mean the opposite of the condition see example below

username = None

while not username:
    username = input("Enter your name: ")

print("Hello " + username)



# for loop = a loop that will execute it's block of code a specified number of times
    # while loop = a loop that will execute it's block of code as long as it's condition is true,
        #   as long as the condition is true the code will keep running
    # for loop = a loop that will execute it's block of code for each item in a sequence

# for i in range(10): #this will count from 0 to 9
#     print(i) # you can use print(i+1) to print 1 to 10

#range a function that creates a sequence of numbers [start,stop,step]

# for i in range(50, 100+1,2): #this will count from 50 to 100 but will skip every 2
#     print(i)

# for i in "Ashleigh Simpson": # this line of code prints each letter in the string to the console
#     print(i)

# to create a timer you need to import the time module as after each second we will be counting down in the for loop.

import time

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")
# **kwargs = parameter that will pack all arguments into a dictionary
    # useful so that a function can accept a varying amount of keyword arguments

# use **kwargs when you don't know how many keyword arguments will be passed into your function
 

def hello(**kwargs): # does not need to be named kwargs but needs **, but it is a good practice to name it kwargs is a dictionary
    print("Hello" +" "+ kwargs["first"] + " " + kwargs["last"])
hello(first="John", last="Smith")

# alternatively you can do something a little different such as the following   
def hello2(**kwargs):
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")
        
hello2(first="John", last="Smith")
# now if you want to add anything inside of hello2 it will print in the order you provide as it is assigned a key value
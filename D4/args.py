# *args = parameter that will pack all arguments into a tuple
    # useful so that a function can accept a varying amount of arguments

def add(sum1, sum2):
    return sum1 + sum2
print(add(1, 2))
# this line of code above will only accept 2 arguments as stated in the parameters.
    # If we wanted to use more than 2 arguments we would need to use *args as shown below


def add2(*args):
    sum = 0
    args = list(args) # if you wanted to edit a value within the list you would need to convert it to a list. As lists are mutable
    args.pop()
    for i in args:
        sum += i
    return sum
print(add2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
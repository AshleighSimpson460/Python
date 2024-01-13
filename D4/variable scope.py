# scope = a region of a program where a variable is recognized
    # a variable is only available from inside the region it is created.
    # this region is called scope.

name = "Jim" # global variable available in the local scope and global

def display_name():
    name = "John"   # local variable only available inside the function
    print(name)

display_name() # will print the local variable
print(name) # will print the global variable
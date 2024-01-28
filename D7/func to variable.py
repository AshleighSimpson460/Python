def hello():
    print("hello")

hi = hello
hello()
hi()

say = print # do not add paranthesis when you are assigning the function to a variable as it will not work 
say("This variable acts as print instead")
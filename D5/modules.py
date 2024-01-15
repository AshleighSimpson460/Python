# module = a file containing python code. May contain functions, classes, etc.
# used with modular programming, which is to separate a program into parts.

# import messages as msg

# msg.hello("Ashleigh")
# msg.bye("Ashleigh")

# you can also determine what functions to call using the following:

from messages import hello, bye

# this allows you to call the function directly without having to write anything else.
    # you can use import * to import all functions from a module. BUT do not use it due to if you use a large project you can come across conflicts.

hello("Ashleigh")
bye("Ashleigh")
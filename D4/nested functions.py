# nested function calls = function calls inside other function calls the returned value is used as argument for the next function call

# num = input("Enter a number: ")
# num = float(num)
# num = abs(num)
# num = round(num)

#this will become one line of code but nested

print(round(abs(float(input("Enter a number: ")))))
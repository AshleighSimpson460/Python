# exception = events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print(result)
    
except ZeroDivisionError:
    print("Cannot divide by zero!")
    
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except Exception:
    print("Something went wrong")
else:
    print("result is", result)
finally:
    print("This will always execute")
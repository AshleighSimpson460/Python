# nested loops = a nested loop is a loop inside a loop.
    # in this case the "inner loop" will finish all of it's iterations before finishing one iteration of the "outer loop"



# I will create another minigame where you can create a certain amount of rows and columns with a symbol of your choosing.
    # I will be creating a game where the user inputs a number and the program will create a grid with that number of rows and columns.

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbols = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbols, end="")
    print()



# I will be creating a minigame where a user inputs a number and the program tells the user if the number is even or odd.
    # the program will then ask the user if they want to play again.

value = input("Enter a number to find out if the value is even or odd: ")

while True:
    for i in value:
        if int(i) % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")
            
    play_again = input("Do you want to play again? (y/n): ")
    if play_again == "y":
        value = input("Enter a number: ")
        continue
    elif play_again == "n":
        break


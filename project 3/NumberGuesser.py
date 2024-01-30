import random

guess = int()
guess_amount = 0
maximum_guess = 5
correct_value = random.randint(1,15)

name = input("What is your name?: ")
while not name or any(char.isdigit() for char in name):
        print("Name is not valid enter a real name")
        name = input("What is your name?: ")
   

while True:
    print("Hello," + name + " let's see if you can figure out the number I am thinking of. You have " + str(maximum_guess) + " guesses")

    while guess_amount < maximum_guess:
        guess = int(input("Guess a number between 1 and 15: "))
        guess_amount += 1
        if guess == correct_value:
            print("You guessed correctly!")
            break
        elif guess < correct_value:
            print("Your guess is too low")
        elif guess > correct_value:
            print("Your guess is too high")
            
    if guess_amount == maximum_guess:
        print("You have run out of guesses. The correct value was "+ str(correct_value))
        
    play_again = input("Play again? (y/n): ").lower()
    if play_again != "y":
        break
    guess_amount = 0
    correct_value = random.randint(1,15)
    
print("Bye!")

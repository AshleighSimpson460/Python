def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-----------------------------")
        print(key)

        for i in answers[question_num-1]:
            print(i)
        guess = input("Enter (A,B or C)")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    
    display_score(correct_guesses, guesses)

def check_answer(ans, guess):
    if ans == guess:
        print("Correct!")
        return 1
    else:
        print("Incorrect")
        return 0

def display_score(correct_guesses, guesses):
    print("-----------------------------")
    print("Results")
    print("-----------------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses)/len(questions)*100)
    print("Your score is: " + str(score)+ "%")

def play_again():
    response = input("Would you like to play again: (y/n)")
    response = response.upper()
    if response == "y":
        return True
    else:
        return False


questions = {
    "What is the worlds longest river called?":"A",
    "What sport does Cristiano Ronaldo play?":"C",
    "What is the name of the 1993 movie about dinosaurs?":"C",
    "Is the Earth round?":"B"
}

answers = [["A. The Nile","B. Rahad River", "C. Gash River"],
           ["A. Basketball", "B. Baseball", "C. Football/Soccer"],
           ["A. Rush Hour","B. Ice Age", "C. Jurassic Park"],
           ["A. No", "B. Yes", "C. I have a theory"]]

new_game()

while play_again():
    new_game()

print("Have a great day!")
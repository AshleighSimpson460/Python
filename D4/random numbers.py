import random

x = random.randint(1,6) # this will print numbers randomly 1 through 6

print(x)

y = random.random() # this will print numbers randomly 0 through 1

print(y)

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList) # this will print random choice from list

print(z)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]

random.shuffle(cards) # this will shuffle the cards

print(cards)
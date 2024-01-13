# list = used to store multiple items in a single variable

food = ["kebab","burger","hotdog","spaghetti","pizza"]

food[2] = "fries"

# food.append("ice cream")
# food.remove("hotdog")
# food.pop()
# food.insert(0,"cake")
food.sort()
# food.clear()

for x in food:
    print(x)

# 2D lists = a list of lists

drinks = ["coffee","soda","tea"]
dinner = ["curry","burger","hotdog"]
dessert = ["cake","ice cream","cookie dough"]

food = [drinks,dinner,dessert]

print(food)

# to access a specific item in a list of lists, you need to specify the index of the list and the index of the item in that list.

print(food[2][1]) # this will print "ice cream"
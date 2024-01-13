# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife","tray"}
dishes = {"bowl", "plate", "cup","tray"}

# utensils.add("napkin")
# utensils.remove("knife")
# utensils.clear()

# utensils.update(dishes)
# dishes.update(utensils) # this will add the items from utensils to dishes
dinner_table = utensils.union(dishes) # this will combine the two sets into one set

# for x in dinner_table:
#     print(x)

print(utensils.difference(dishes)) # this will print the items in dishes that are not in utensils
print(utensils.intersection(dishes)) # this will print the items that are in both sets
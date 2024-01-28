#   sort() method = used with lists
#   sorted() function = used with iterable objects

students = ["Isagi", "Rin", "Bachira", "Sae", "Hiori", "Kaiser"]
studentss = ("Isagi", "Rin", "Bachira", "Sae", "Hiori", "Kaiser")

students.sort()
for i in students:
    print(i)

sorted_students = sorted(studentss, reverse=True)

for i in sorted_students:
    print(i)

bl_students = [("Isagi","striker"),
               ("Rin","striker"),
               ("Bachira","playmaker"),
               ("Sae","playmaker"),
               ("Hiori","playmaker"),
               ("Kaiser","striker")]

position = lambda position:position[1] # [1] because machines operate starting from 0 - 0 will be the names 1 is the position
bl_students.sort(key=position)

for i in bl_students:
    print(i)

# sorted_students = sorted(bl_students, key=position[1]) if the list was a tuple meaning inside of () instead of [] you would use sorted
# and do the same for loop as above
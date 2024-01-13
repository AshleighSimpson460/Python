# tuple = a collection which is ordered and unchangeable used to group together related data.

student = ("Ashleigh", 23, "male")

print(student.count("Ashleigh"))
print(student.index("male"))

for x in student:
    print(x)

if "Ashleigh" in student:
    print("Ashleigh is present!")
else:
    print("Ashleigh is hiding!")
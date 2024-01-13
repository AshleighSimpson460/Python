import os

path = "c:\\Users\\Ashleigh\\Desktop\\New Text Document.txt"

if os.path.exists(path):
    print("File exists")
    if os.path.isfile(path):
        print("File is a file")
    elif os.path.isdir(path):
        print("This is a directory")
else:
    print("File does not exist")
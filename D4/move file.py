import os

source = "c:\\Users\Ashleigh\\Desktop\\text.txt"
destination = "c:\\Users\Ashleigh\\Downloads"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved") 
except: FileNotFoundError


with open('c:\\Users\Ashleigh\\Desktop\\New Text Document.txt') as file: 
    print(file.read())
# the way the code is written it will close the file automatically after opening
    
print(file.closed) # we can use this code to see if the file was closed or opened

try:
    with open('c:\\Users\Ashleigh\\Desktop\\New Text Document.txt') as file: 
        print(file.read())
except FileNotFoundError:
    print("File not found") 
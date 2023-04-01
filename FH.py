'''         File Handling
f = open("Assignment.txt","r")
for lines in f:
    print(f.readlines())
modes of a file:-
r - read
w - write
a - append
x - create
t - text
b - binary 
'''
'''f = open("Intro.txt", "r")
lines = f.read(5)
print(lines)
f.close'''


'''with open("Intro.txt","r") as reader:
    for line in reader:
        print(line, end ="")'''
'''file1 = open("Intro.txt","r")
count = 0
while True:
    count += 1
    line = file1.readline()
    if not line:
        break
    else:
        print(f"line-{count}: {line.strip()}")
file1.close()'''

'''with open("Intro.txt","r") as reader:
    lines = reader.readlines()
    for line in lines:
        print(line,end="")'''

'''f = open("Intro.txt","r")
cursor_position = f.tell()
print("cursor position: ", cursor_position)
data = f.read(5)
cursor_position = f.tell()
print("After reading cursor position: ", cursor_position)
f.seek(20)
data = f.read()
print(data)'''

'''file = open("Intro.txt","w")
file.write("This is line 1\n")
file.write("This is another line\n ")
file.write("This is 3rd line ")
file.close()'''

'''with open("Intro.txt","r") as reader:
    lines = reader.read()
    lines = lines[::-1]
with open("Intro_copy.txt","w") as writer:
    writer.write(lines)'''

'''f = open("Intro.txt","a")
f.write("/nThis line is appended!!")
print("Operation successful!")
f.close()'''

'''with open("Intro.txt","r") as reader, open("Intro_copy.txt","w")as writer:
    lines = reader.readlines()
    writer.writelines(lines)
print("file created....")

import re
newlines = ""
searchstr = input("Enter search string: ")
newstr = input("Enter new string: ")
with open("Intro.txt") as reader:
    lines = reader.readlines()
    for line in lines:
        newlines += re.sub(fr"\b{searchstr}\b",newstr,line)
with open("Intro_copy.txt","w") as writer:
    writer.writelines(newlines)
print("Replacement Done...")
with open("pic.png","rb") as reader, open("home_copy.png","wb") as writer:
    lines = reader.readlines()
    writer.writelines(lines)
print("Copy Created")'''
'''
import os.path
isfile("name") - True if name is file
isdir("name") - True if name is directory
exists("name") - True if name is a file or directory
'''
'''import os.path
filename = "Intro.txt"
flag = os.path.isfile(filename)
if flag:
    print(f"File {filename} exixts!")
else:
    print(f"File {filename} does not exists!")'''

'''import os.path
filename = "C:\\Users\\Abhinav\\BullseyeCoverageError.txt"
dirname = "C:\\Java Program"
flag = os.path.isfile(filename) and os.path.exists(dirname)
if flag:
    print(f"File {filename} and directory {dirname} exixts!")
else:
    print(f"File {filename} and directory {dirname} does not exists!")
'''
import os
import os.path
dirname  = "C:\\Python"
result = os.listdir(dirname)
for r in result:
    if os.path.isfile(r):
        print(r,"is file")
    else:
        print(r,"is directory")

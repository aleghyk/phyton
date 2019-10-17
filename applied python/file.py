f = open("file.txt", "wt")
import os
path = os.getcwd()
f.write("String1/n")
f.write("String2/n")
f.close()
f = open("file.txt", "at")
print (f.tell())
f.write("String3/n")
f.close()
f = open("file.txt", "rt")
txt = f.read()
print (txt)
f.close()
f = open("file.txt", "rt")
txt = f.readline()
for lie in f:
    print(line)
f.close()
with open ("file.txt", "rt") as f:
    for lie in f:
        print(line)

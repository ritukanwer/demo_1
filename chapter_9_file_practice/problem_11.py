# write a python program to rename a file  to "renamed_by_python.txt"



with open("xyz.txt",'r') as f:
    a = f.read()

with open("renamed_by_python.txt",'w') as f:
    f.write(a)
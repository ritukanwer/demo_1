# write a program to fnd out whether a file is identical and matches then content of another file.


with open("this.txt",'r') as f:
    a1 = f.read()

with open("this_copy.txt",'r') as f:
    a2 = f.read()

if a1 == a2:
    print("yes this is identical and matches")

else:
    print("no, this is not identical and matches")
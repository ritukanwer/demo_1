
# write a program to make a copy of a txt file"this.txt

with open("this.txt",'r') as f:
    a = f.read()

with open("this_copy.txt",'w') as f:
    f.write(a)
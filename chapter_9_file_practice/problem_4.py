# a file conatains A word "donkey" multiple time. you need to write a program which replace this word with 
##### by updating the same file.

new = "donkey"
with open("file.txt", "r") as f:
    a = f.read()

b = a.replace(new , "######")

with open("file.txt","w") as f:
    f.write(b)
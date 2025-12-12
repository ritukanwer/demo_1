# /write a program  to read the text from given file "poems,text"and find out weather it contains the word "twinkle"




f = open("poems.txt")

a =f.read()

if ("twinkle" in a):
    print("twinkle is present")
else:
    print("twinkle is not present")
f.close()
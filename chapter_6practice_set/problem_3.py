# a spam comment is defined as a text containing keywords  "make a lot of money" ,"buy now","subscribe this"
# "click this". write a program to detected these spam .

a= "make a lot of money"
b = "buy now"
c = "subscribe this"
d = "click this"

n = input("enter your words")

if (a in n) or (b in n) or (c in n) or (d in n):
    print("this is spam")

else:
    print("this is not a spam")
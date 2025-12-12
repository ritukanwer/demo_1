# write a program to find weather a given number is primary or not


n = int(input("enter your number"))

for i in range (2,n):
    if i % 2 == 0:
        print("this is not a primary number")
        break
    else:
        print("this is a primary number")


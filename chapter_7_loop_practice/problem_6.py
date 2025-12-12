# write a python program to calculate the factorial of given number using for loop.
# 
# 
a = int(input("enter your number"))  

b= 1
for i in range(1, a+1):
    b *= i

print(b)
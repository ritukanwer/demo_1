# write a python program to find the su of first  n natural numbers usin while loop.
a = int(input("enter_your_number"))

i = 1
sum = 0
while i <= a:
    sum += i
    i += 1
print(sum)
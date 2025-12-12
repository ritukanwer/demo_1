#write a python program to find the greatest of four numbers entered by the user.

a = int(input("enter_first_no"))
b = int(input("enter_second_no"))
c = int(input("enter_third_no"))
d = int(input("enter_4th_number"))

if (a>b and a>c and a> d):
    print("a is greatest")
elif (b>a and b>c and b>d):
    print("b is greatest")

elif (c>a and c>b and c>d):
    print("c is greatest")

else:
    print("d is greatest")

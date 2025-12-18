# write a program to   display a/b where a and b are interger . if b = 0 , display
#  infinite by handling the zero division error 

try:
    a = int(input("enter any number:-"))
    b = int(input("enter any number:-"))
    print(f"the division a/b is {a/b}")

except ZeroDivisionError as v:

    print("infinite")
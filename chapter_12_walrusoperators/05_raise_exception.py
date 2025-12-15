a = int(input("enter any number:-"))
b = int(input("enter any number:-"))


if (b == 0):
    raise ZeroDivisionError("it is not divided by zero")

else:
    print(f"the division a/b is {a/b}")
# write a program using functions to find greatest of three numbers
a= 3
b =90
c = 80

def greatest(a,b,c):
    if (a > b and a > c):
        return a
    elif (b>a and b>c):
        return b
    else:
        return c
print(greatest(a,b,c))
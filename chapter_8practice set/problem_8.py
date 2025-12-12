# write a pyhton function to print multiplication table of given number

n = int(input("enter your number:-"))

def multiplication(n):
    for i in range(1,11):
        print(n * i)
    
print(multiplication(n))
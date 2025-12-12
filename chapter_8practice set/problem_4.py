# write a recursive function to calculate the sum of first natural number

n = int(input("enter your number"))
def sum(n):
    if n==1:
        return 1
    return sum(n-1)+n

print(sum(n))
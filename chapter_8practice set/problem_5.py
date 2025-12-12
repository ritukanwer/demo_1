# write a python function to print a first n linesof the followin patterns
# i have little doubt i didn't undestand properly
# ***
# **
# * -for n = 3

n = int(input("enter your number"))
def pattern(n):
    if n ==0 :
        return 
    print("*"*n)
    pattern(n-1)
pattern(n)


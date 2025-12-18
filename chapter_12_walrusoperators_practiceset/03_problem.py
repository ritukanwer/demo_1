# write a list comprehesion to print a list which contains the multiplication table of 
# a user enter.
# 
# 

users_input = int(input("enter any number :- "))

multiplication_table = [users_input * i for i in range(1,11)]
print(multiplication_table)
# for i, value in enumerate(multiplication_table, start=1):
#     print(f"{users_input} x {i} = {value}")
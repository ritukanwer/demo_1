# write a program to   print third ,fifth and seventh element in from a list using enumrate 
# function 

l1 = [1,2,3,4,5,6,7,8,8,9,9,7]
for index, i in enumerate(l1):
    if index == 3 or index == 5 or index == 7:
        print(f"the item number at the  index {index} number is {i}")

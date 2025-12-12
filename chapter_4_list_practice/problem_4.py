# write a python program to sum a list with 4 number

l1 = [20,30,40,50]

def sum_of_numbers(l1):
    sum_no = 0
    for i in l1:
        sum_no += i
    return sum_no
print(sum_of_numbers(l1))
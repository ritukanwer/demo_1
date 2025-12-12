# write a python program to acceptmarks of 6students and display them in sorted manoer


st_marks = [20,30,40,10,50,50]
def sum_marks(st_marks):
    sum = 0
    for i in st_marks:
        sum +=i
    return sum
print(sum_marks(st_marks))

new = []
mark1 = int(input("enter_1st_no:-"))
mark2 = int(input("enter_2nd_no:-"))
mark3 = int(input("enter_3rd_no:-"))
mark4 = int(input("enter_4th_no:-"))
mark5 = int(input("enter_5th_no:-"))
mark6 = int(input("enter_6th_no:-"))

new.append(mark1)
new.append(mark2)
new.append(mark3)
new.append(mark4)
new.append(mark5)
new.append(mark6)
print(new)
print(sum(new))
#store the multiplication tables generated in problem 3 in a file name tables.txt

users_input = int(input("enter any number :- "))

multiplication_table = [users_input * i for i in range(1,11)]
with open("table.txt","a") as f:  

    f.write(str(multiplication_table)+ "\n")
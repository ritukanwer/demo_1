#write a python program to find weather  a given username contain less than 10 characters or not
# 
# 
username = input("enter user name")

if len(username) < 10:
    print("yes length is less than 10")
else:
    print("not length is more than 10")
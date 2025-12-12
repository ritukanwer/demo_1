# if language of two friends are same:what we happen to the program in problem 6?


# nothing because dict can't accept duplicate keys but it can accept duplicate values

dic = {}
name1 = input("enter friends name:-")
language1 = input("enter_favorite_language")
name2 = input("enter friends name:-")
language2 = input("enter_favorite_language")
name3 = input("enter friends name:-")
language3 = input("enter_favorite_language")

name4 = input("enter friends name:-")
language4 = input("enter_favorite_language")

dic.update({name1:language1})
dic.update({name2:language2})
dic.update({name3:language3})
dic.update({name4:language4})
# dic = {'ritu': 'python', 'ritu': 'sql', 'ss': 'c', 's': 'c++'}
print(dic)
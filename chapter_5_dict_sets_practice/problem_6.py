# create a empty dictionary .type allow 4 friends to enter their favorite   
# language as value and use keys
# as their name . assume that the names are unique

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

print(dic)
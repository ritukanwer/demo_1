# create a class with a class attribute a; creat an object from it and set 'a' directly 
# using object.a = o. does this change the class attribute


class demo:
    a =4  #classs attribute doesn't change

o= demo()
print(o.a)

o.a= 0
print(o.a)


print(demo.a)



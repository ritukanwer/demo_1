

class employee:
    def __init__(self):
        print("constructer of emplyee")
    a =1

class programmer(employee):
    def __init__(self):
        print("constructer of programmer")
    b = 2

class manager(programmer):
    def __init__(self):
        super().__init__()
        print("constructer of manger")
    c = 3


# o = employee()

# print(o.a)


# o = programmer()
# print(o.a,o.b)



o = manager()
print(o.a,o.b,o.c)

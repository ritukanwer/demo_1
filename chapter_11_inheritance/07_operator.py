

class number:
    def __init__(self,n):
        self.n = n
        

    def __add__(self,num):
        return self.n +num.n
    
n = number(30)
m = number(40)
print(n+m)


# ----------------substraction/
class number:
    def __init__(self,n):
        self.n = n
        

    def __sub__(self,num):
        return self.n-num.n
    
n = number(30)
m = number(40)
print(n-m)









class number:
    def __init__(self,n):
        self.n = n
        

    def __mul__(self,num):
        return self.n *num.n
    
n = number(30)
m = number(40)
print(n*m)




class number:
    def __init__(self,n):
        self.n = n
        

    def __truediv__(self,num):
        return self.n /num.n
    
n = number(30)
m = number(40)
print(n/m)
# write a class vectore representing a vector of n dimenstions. overload the  + and * operator which is 
# calculate the sum and dot(.) product of them .


class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self,other):
        result = Vector(self.x+ other.x,self.y + other.y,self.z+ other.z)
        return result 
    

    def __mul__(self,other):
        result = Vector(self.x* other.x,self.y * other.y,self.z* other.z)
        return result 
    
    def __str__(self):
        return f"vector({self.x},{self.y},{self.z})"
    


v1 = Vector(2,3,4)
v2 = Vector(7,6,5)
v3 = Vector(10,20,30)

print(v1 + v2)
print(v1 * v2)

print(v1 + v3)
print(v1 * v3)
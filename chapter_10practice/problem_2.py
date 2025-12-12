# write a class "calculator" capable  of finding squre ,cube and sequare root of a  number


class calculator:
    def __init__(self,n):
        self.n = n
        
    def square(self):
        print(f"the square id {self.n * self.n}")

    def cube(self):
        print(f"the cube id {self.n * self.n *self.n}")


    def squareroot(self):
        print(f"the square id {self.n ** 1/2}")

a = calculator(4)
a.square()
a.cube()
a.squareroot()





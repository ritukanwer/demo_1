# add static mehtod to in problem 2, to greet the user with hello.




class calculator:
    def __init__(self,n):
        self.n = n
        
    def square(self):
        print(f"the square id {self.n * self.n}")

    def cube(self):
        print(f"the cube id {self.n * self.n *self.n}")


    def squareroot(self):
        print(f"the square id {self.n ** 1/2}")

    @staticmethod

    def hello():
        print("hello there !")



a = calculator(4)
a.square()
a.cube()
a.squareroot()
a.hello()




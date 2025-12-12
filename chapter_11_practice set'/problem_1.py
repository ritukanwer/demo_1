# create a class   (2-d vector) and use it to create a another class repreasenting a another class.
# representing a 3-d vectore.



class twodvectore:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"the vectore is {self.i}i +{self.j}j")


class threedvectore(twodvectore):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f"the vectore is {self.i}i +{self.j}j + {self.k}k")



a = twodvectore(1,2)
a.show()

b= threedvectore(1,2,3)
b.show()
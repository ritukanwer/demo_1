class employee:
    company  = 'itc'
    name = "default"
    def show(self):
        print(f"the name is {self.name}  and the salary is {self.company}")


class coder:
    language  = 'python'
    def printlanguage(self):
        print(f"the language is {self.language}")


class programmer(employee,coder):
    company  = 'itc info tech'
    def showlanguage(self):
        print(f"the name is {self.name} , and the language is {self.language}")


        
a = employee()
b = programmer()

b.show()
b.showlanguage()
b.printlanguage()
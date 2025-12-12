

class employee:
    company  = 'itc'
    def show(self):
        print(f"the name is {self.name} , and the salary is {self.salary}")


# class programmer:
#     company  = 'itc info tech'
#     def showlanguage(self):
#         print(f"the name is {self.name} , and the language is {self.language}")


class programmer(employee):
    company  = 'itc info tech'
    def showlanguage(self):
        print(f"the name is {self.name} , and the language is {self.language}")


        
a = employee()
b = programmer()

print(a.company,b.company)

# create  a class "prgrammer"  for storing information of few programmers  working at microsof.

class programmer:
    company = "microsoft"

    def __init__(self,name,salary,age):
        self.name = name
        self.salary = salary
        self.age = age


r = programmer("ritu",200000,20)
p = programmer("priya",200000,20)

print(p.name,p.salary,p.age,p.company)
print(r.name,r.salary,r.age,r.company)


# nothing happend but readablility was change
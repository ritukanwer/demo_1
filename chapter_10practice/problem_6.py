
class programmer:
    company = "microsoft"

    def __init__(ritu,name,salary,age):
        ritu.name = name
        ritu.salary = salary
        ritu.age = age


r = programmer("ritu",200000,20)
p = programmer("priya",200000,20)

print(p.name,p.salary,p.age,p.company)
print(r.name,r.salary,r.age,r.company)
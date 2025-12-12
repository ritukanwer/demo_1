

class employee():
    name = "ritu"
    language = "python"
    age = 20

    def getinfo(self):
        print(f"the language is {self.language}.the salary is {self.age}")

ritu = employee()
# ritu.language = "javascript"
ritu.getinfo()
# employee.getinfo(ritu)

# print(ritu.name,ritu.language,ritu.age)
class employee():
    name = "ritu"
    language = "python"
    age = 20

    def __init__(self,name,age,language):
        self.name = name
        self.age = age
        self.language = language
        print("i am creating a object")

    def getinfo(self):
        print(f"the language is {self.language} . and the age is {self.age}")


    @staticmethod
    def greet():
        print("good morning")

ritu = employee("ritu",20,"python")
# ritu.language = "javascript"
print(ritu.name,ritu.language,ritu.age)
# Write a Python program to create an instance of a specified class and display the namespace of the said instance.


class ritu:    #here i have created a class , and class name is ritu.
    name = 'ridhi' # here i am creating a object
    age = 30 #object
    salary = 300000 #object all three are called class object okay

a = ritu() #i assign my function to call a varibles and variable storing the return value of the function

a.name ='ssiya'   #here i am creating a instance object , firstly computer check object class then 
# if class object is available so then it check instance object if istance oobject is here ot tabke value 
     # of instanse object if instance object is not here so it use class object 
    #   basically id=t give first priority instance if both object was there
print(f"name is {a.name}, age is {a.age}, salary is {a.salary}")
# here i  print the name and age and salary , i  also use f string because inside in print istment i 
# can write some what i need to print





# now i am solving the same question using function okay

class ritu:
   

    def __init__(self,name, age , salary):
        self.name = name
        self.age = age
        self.salary = salary 

a =  ritu("ritu",20,800000)

a.name = "garima"  #instance object

print(f"name is {a.name},age is {a.age}, salary is {a.salary}")


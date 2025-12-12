# Write a Python program to create an instance of a 
# specified class and display the name
# space of the said instance.


class student:
    class_st = "10th"
    name = "ritu"
    age = 20

ritu = student()

ritu.class_st = "9th"

print(f"name is {ritu.name},and class is {ritu.class_st}, and age is {ritu.age}")

# write a python program to calculate the grade of students from his marks from the following scheme

# 90- 100 => ex
# 80-90=>a
# 70-80 => b
# 60-70 => c
# 50-60=>d 
# <50 =>f


marks = int(input("entr your marks"))

if marks < 100 and marks > 90:
    print("level ex")
elif marks <=90 and marks > 80:
    print("level a")
elif marks <= 80 and marks >70:
    print("level b")
elif marks <= 70 and marks > 60:
    print("level c")
elif marks <= 60 and  marks>50:
    print("level d")
else:
    print("level f")


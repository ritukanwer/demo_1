with open("log_2.txt") as f:
    lines = f.readlines()

lineno = 1
for i in lines:
    if "python" in i:
        print(f"yes python is present. line no : {lineno}")
        break
    lineno +=1

else:
    print("python is not present")

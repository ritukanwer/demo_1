# write a program to mine a log file and find out whether it contains "python"


with open("log.txt","r") as f:
    f.read()

if "python" in "log.txt":
    print("pyhton is present")
else:
    print("python is not present")
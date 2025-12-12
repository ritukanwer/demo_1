# write a program to find  out whether a student paased or failed if it require atotsl of 40% and 
# at least 30 % in each subject to pass . assume 3 subjectedand take marks input from a user.



mark1 = int(input("enter marks"))
mark2 = int(input("enter marks"))
mark3 = int(input("enter marks"))


per = (mark1+mark2+mark3)/3
if (per >40 and mark1 >= 33 and mark2>=33 and mark3 >= 33):
    print("you are pass")
else:

    print("you are fail")
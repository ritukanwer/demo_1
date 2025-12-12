# write a program to greet all the person name stored in a list 'l' and which start with s

l=["ritu","siya","diya","sonu","rinu","sadhi"]
new_list = []
for i in l:
    if i[0] == 's':
        new_list.append(i)
print(new_list)
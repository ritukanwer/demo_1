# repeat program 4 for a list of such word to be censord


new = ["ritu","how","food"]
with open("new-file.txt", "r") as f:
    a = f.read()
for i in new:
    a = a.replace(i , "#"*len(i))

with open("new-file.txt","w") as f:
    f.write(a)
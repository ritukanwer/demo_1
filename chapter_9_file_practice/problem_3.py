# write a program to generate multiplication tables from   2 to 20. 
# and write it to the different file place these files in a folder  for a 13 year old.


def generate_table(n):
    table = ""
    for n in range(1,11):
        table += f"{n} x {i} = {n * i}\n"

    with open(f"tables/table_{n}.txt","w") as f:
        f.write(table)


for i in range(2,21):
    generate_table(i)

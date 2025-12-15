li = [10,20,30,40,50,60]
# index =0
# for i in li:
#     # index += 1 # at this place index started from 1 i need to start from 0 because python start index from 0
#     print(f"the item number at  index {index} is {i}")
#     index += 1 # i am writting this here because is start from 0 

for index, i in enumerate(li):
    print(f"the item number at  index {index} is {i}")

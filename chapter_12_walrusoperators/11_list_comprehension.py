mylist = [1,2,3,4,5]
sequre_list = []
# for i in mylist:
#     sequre_list.append(i*i)
# print(sequre_list)

sequre_list = [i * i for i in mylist]   # using list comrehension
print(sequre_list)
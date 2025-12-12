# write a python function to remove a given word  from a list ad strip it at the end.


l1 = ["ritu","naruka","vinu","hinu"]

def remove_a_word(l1,w):
    l2 = []
    for i in l1:
        if not (i == w):
            l2.append(i.strip(w))
    return l2

print(remove_a_word(l1,"hinu"))

# oaky now i understand proply first i think remove a specific value but now i understand 
# which value i ave in pramerter that word remove from whole list like i remove hinu it remove h,n,i,u
# from every value
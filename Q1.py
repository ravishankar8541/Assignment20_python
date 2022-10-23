"""Write a python program to create a function that takes a list and returns a new list
with the original list's unique elements."""
def f1(*t):
    list=[]
    for a in t:
        list.append(a)
    return list
list1=["ravi",3,"mohan",3]
bag=f1(*list1)
print(type(bag))
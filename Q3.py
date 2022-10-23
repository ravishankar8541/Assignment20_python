"""Write a python program to create a function that prints the even numbers from a
given list."""
def fun(*t):
    list=[]
    for a in t:
        if a%2==0:
            list.append(a)
    return list        
l=[1, 2, 3, 4, 5, 6, 7, 8, 9]
bag=fun(*l)
print(bag)

#Write a python program to create a function to find the Min of three numbers.
def fun(a,b,c):
    if a<b:
        if a<c:
            print(a)
        else:
            print(c)    
    else:
        if b<c:
            print(b)
        else:
            print(c)     
fun(2,1,5)                   
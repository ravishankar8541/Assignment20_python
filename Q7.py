#Write a python program to access a function inside a function.
def f1(str):
    newStr=f2(str)
    if newStr==str:
        print("palindrome")
    else:
        print(" not palindrome")    
def f2(a):
    return a[: : -1]  
f1("pap")     
    

   
   


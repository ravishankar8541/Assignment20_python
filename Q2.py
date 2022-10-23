"""Write a python program to create a function that takes a number as a parameter and
checks if the number is prime or not."""

def f(a):
    count=0
    for r in range(1,a+1):
        if a%r==0:
            count+=1
    if count==2:
        print("Prime number ")
    else:
        print("Not prime number")         
          
f(7)    
   
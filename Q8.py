"""Write a python program to create a function that accepts a string and calculate the
number of upper case letters and lower case letters."""

def findUpperAndLower(str):
    upperCase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowerCase="abcdefghijklmnopqrstuvwxyz"
    sumUpper=0
    sumLower=0
    for a in str:
       if a in upperCase:
        sumUpper+=1
       else:
        sumLower+=1     
    print("total upper case =",sumUpper)    
    print("total Lower case =",sumLower)
findUpperAndLower("RaviShankarKumarRay")
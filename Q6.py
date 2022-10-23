"""Write a python program to create a function and print a list where the values are
square of numbers between 1 and 30."""

def printSquare(a,b):
 print([a*a for a in range(1,30,1)])
printSquare(1,30)
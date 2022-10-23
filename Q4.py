"""Write a python program to create a function that checks whether a passed string is
palindrome or not."""

def isString(str):
    newStr=str[: :-1]
    if newStr==str:
        print(str,"is Palindrome")
    else:
        print(str,"is not palindrome")    

isString("mam")
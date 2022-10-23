"""Write a python program to create a function to check whether a string is a pangram
or not."""

def checkPangram(str):
    letter="abcdefghijklmnopqrstuvxwyz"
    print(str.lower())
    count=0
    for x in letter:
        if x in str:
            count+=1
    if count==26:
        print("String is pangram")
    else:
        print("String is not a pangram")    
checkPangram("A quick brown fox jumps over the lazy dog ")
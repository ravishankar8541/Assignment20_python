"""Write a python program to create a function to check whether a string is an anagram
or not."""

def checkanagram(str1,str2):
    count=0
    for a in range(0,len(str1)):
        if str1[a] in str2:
         count+=1
    if count==len(str1):
        print("anagram")   
    else:
        print("not anagram")     
checkanagram("abdek","eadcb")        
# 2 Write a python program that takes a list of words as input and return a new list containing only the words that start with a vowel.

def func(l):
    vowels = ['a','e','i','o','u']
    new_list = []
    for i in l:
        for j in range(len(i)):
            if i[0] in vowels:
                new_list.append(i)
                break
    return new_list
print("Input a list of element sepearted by whitespace")
l = list(map(str,input().split()))
res = func(l)
print(f"New string is : {res}")
# Output:
# Input a list of element sepearted by whitespace
# python akhand even india java
# New string is : ['akhand', 'even', 'india']
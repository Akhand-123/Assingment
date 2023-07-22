# 1 Write a Python program to take a string as input and return a new string where the first and last characters have been exchanged.
mystr = input("Enter a string :")
l = list(mystr)
temp = l[0]
l[0]=l[-1]
l[-1]=temp
print("".join(l))

# Output 
# Enter a string :The big brown fox
# xhe big brown foT

# 2.Create a Python function that takes a list of strings as input and returns the longest string in the list.
def func(l):
    a=0
    max_len=0
    for i in l:
        if len(i)>max_len:
           a, max_len=i,len(i)
    return f"max length char in given list is : {a} and its length is : {max_len}"
# l = ["PHP","Python","Java","Programming"]
print("Enter elements in the list seperated by whitespace")
l = list(map(str,input().split()))
print(func(l))

# Output:
# Enter elements in the list seperated by whitespace
# php python java smallTalk
# max length char in given list is : smallTalk and its length is : 9

# 3.Write a Python program to check if a given string is a palindrome (a word, phrase, number, or other sequence of characters that reads the same forward and backward).

def check_palindrome(mystr):        
    a = mystr[::-1]
    if mystr == a:
        return ("String is palindrome")
    else:
        return ("String is not palindrome")

# Function calling 
mystr = input("Enter a string : ").lower()
res = check_palindrome(mystr)
# Printing the result 
print(res)

# Output
# Enter a string : 1234321
# String is palindrome

# Enter a string : akhand
# String is not palindrome

# 4.Create a Python function that takes a sentence as input and returns the number of words in the sentence

def func(n):
    a = n.split()
    
    return len(a)
mystr = input("Enter a string : ")
# Calling the function 
res = func(mystr)
# Printing the restult
print(res)

# Output
# Enter a string : the big fat dog
# 4

# 5.Write a Python program to remove all the vowels from a given string.

mystr = input("Enter a string : ")
vowels = "aeiou"
a=[]
for i in list(mystr):
    if i in list(vowels):
        continue
    else:
        a.append(i)

print("".join(a))

# Output
# Enter a string : akhand
# khnd
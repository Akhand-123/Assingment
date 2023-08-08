# Q. 1] Write a Python Program to check whether a number is prime or not.(Take numbers whatever you want)
def isprime(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
    if count > 2:
        return False
    else:
        return True
num = int(input("Enter a number : "))
# Return True is num is prime else return False
res = isprime(num)
print(res)

# Q. 2] How can you randomize the items of a list in place?
# List = [‘He’, ‘Loves’, ‘To’, ‘Code’, ‘In’, ‘Python’]

import random
l = list(map(str,input().split()))
print(l)
random.shuffle(l)
print(l)

# Output
# He Loves To Code In Python
# ['He', 'Loves', 'To', 'Code', 'In', 'Python']        
# ['Python', 'Loves', 'To', 'Code', 'In', 'He'] 

# Q. 3] How will you remove duplicate elements from a list?
# demo_list = [5, 4, 4, 6, 8, 12, 12, 1, 5]
def remove_duplicat(l):
    a = set(l)
    b = list(a)
    return b
l = list(map(int,input().split()))
# Calling function
res = remove_duplicat(l)
print(res)

# Output
# 5 4 4 6 8 12 12 1 5
# [1, 4, 5, 6, 8, 12]

# Q. 4] Write a code to sort a numerical list (Take numbers as your wish).
l = list(map(int,input().split()))
print(l)
res = sorted(l)
print(res)

# output
# 5 4 4 6 8 23 12 1 5
# [5, 4, 4, 6, 8, 23, 12, 1, 5]
# [1, 4, 4, 5, 5, 6, 8, 12, 23]

# Q. 5] Write a program in Python to produce Star triangle.
num = int(input("Enter no. of rows : "))
for i in range(1,num+1):
    print("*"*i)

# Output
# Enter no. of rows : 5
# *
# **
# ***
# ****
# *****
# 1.) Write a python program for given example :
# example: a4b3c2
# output: aaaabbbcc
# import re
# mystr = input("Enter a string : ")
# l=list(mystr)
# # print(l)
# l1 = re.findall('[a-z]',mystr)
# l2 = re.findall('\d',mystr)
# for i in range(len(l1)):
#     print(l1[i]*int(l2[i]),end="")


# output:
# Enter a string : a4b3c2
# aaaabbbcc

# 2.) Python program to interchange first and last elements in a list
# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]
# mylist = list(map(int,input().split()))
# print(f"list before swapping : {mylist}")
# temp = mylist[0]
# mylist[0] = mylist[-1]
# mylist[-1] = temp
# print(f"list after swapping : {mylist}")

# Output:
# list before swapping : [12, 35, 9, 56, 24]
# list after swapping : [24, 35, 9, 56, 12]

# 3.) Python program to find second largest number in a list
# Input : [12, 10,35, 9, 56, 24,56,55]
# Output : 55

# print("Enter a list element with whitespace line")
# l = list(map(int,input().split()))
# a = set(l)
# b = list(a)
# b.sort()
# print(b[-2])

# Output
# Enter a list element with whitespace line
# 12 10 35 9 56 24 56 55
# 55

# 4.) Check if two lists have at-least one element common or not
# Input : a = [1, 2, 3, 4, 5]
# b = [5, 6, 7, 8, 9]
# Output : True
# Input : a=[1, 2, 3, 4, 5]
# b=[6, 7, 8, 9]
# Output : False

print("Enter element in list a seperated via whitespace")
a = list(map(int,input().split()))
print("Enter element in list b seperated via whitespace")
b = list(map(int,input().split()))
if set(a).intersection(set(b)) != set():
    print(True)
else:
    print(False)
    
# Output1
# Enter element in list a seperated via whitespace
# 1 2 3 4 5
# Enter element in list b seperated via whitespace
# 5 6 7 8 9
# True
# Output2
# Enter element in list a seperated via whitespace
# 1 2 3 4 5
# Enter element in list b seperated via whitespace
# 6 7 8 9
# False











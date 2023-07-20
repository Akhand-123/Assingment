# Write a Python program to triple all numbers of a given list of integers. Use Python map.

# sample list: [1, 2, 3, 4, 5, 6, 7]


# Triple of list numbers:

# [3, 6, 9, 12, 15, 18, 21]

print("Enter the element in a list seperated with white space")
l = list(map(int,input().split()))
a = list(map(lambda x:x*3,l))
# printing the result
print(a)

# Output:
# Enter the element in a list seperated with white space
# 1 2 3 4 5 6 7
# [3, 6, 9, 12, 15, 18, 21]
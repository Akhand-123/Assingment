# Write a Python program to square the elements of a list using map() function.

# Sample List: [4, 5, 2, 9]

# Square the elements of the list:

# [16, 25, 4, 81]
print("Enter the element of the list with whitespace")
l = list(map(int,input().split()))
a = list(map(lambda x:x**2,l))
# Printing the result 
print(a)

# Output:
# Enter the element of the list with whitespace
# 4 5 2 9
# [16, 25, 4, 81]
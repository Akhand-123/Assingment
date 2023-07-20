# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.

# sample input: 10

# sample output: 35
# taking input
num = int(input("Enter a number : "))

a = lambda x : x+25
# calling lambda function and passing input num
print(a(num))

# output:
# Enter a number : 10
# 35
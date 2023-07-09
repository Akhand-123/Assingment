# Write a Python function to sum all the numbers in a list.

# Sample List : (8, 2, 3, 0, 7)

# Expected Output : 20

def sum_digit(n):
    sum = 0
    for i in n:
        sum +=i
    return sum

sample_list = [8,2,3,0,7]
# function calling 
a = sum_digit(sample_list)
# printing result
print(a)

# Output: 20
# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

# Sample String : 'The quick Brow Fox'

# Expected Output :

# No. of Upper case characters : 3

# No. of Lower case Characters : 12

def count_upper_lower(n):
    count_upper=0
    count_lower=0
    for i in n:
        if i.isupper()==True:
            count_upper +=1
        if i.islower()==True:
            count_lower +=1
    return f"No. of Upper case characters : {count_upper}\nNo. of Lower case Characters : {count_lower}"

# sample_string = "The quick Brow Fox"
sample_string = input("Enter a string : ")
# function calling 
result = count_upper_lower(sample_string)
# printing result
print(result)

# Output:
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
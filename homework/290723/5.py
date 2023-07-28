# 5. Write a program in Python to count lower, upper, numeric and special characters in a string.

# Input : @pyThOnlobb!Y34

# Expected output :
# Numeric counts 2
# Lower counts 8
# Upper counts 3
# Special counts 2
import re
mystr = input("Enter a string : ")
num = re.findall("\d",mystr)
lower = re.findall("[a-z]",mystr)
upper = re.findall("[A-Z]",mystr)
special = re.findall("\W",mystr)
print(f"Numeric count : {len(num)}")
print(f"Lower count : {len(lower)}")
print(f"Upper count : {len(upper)}")
print(f"Special count : {len(special)}")

# Output
# Enter a string : @pyThOnlobb!Y34
# Numeric count : 2
# Lower count : 8
# Upper count : 3
# Special count : 2

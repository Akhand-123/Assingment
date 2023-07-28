# 5. Write a program in Python to count lower, upper, numeric and special characters in a string.

# Input : @pyThOnlobb!Y34

# Expected output :
# Numeric counts 2
# Lower counts 8
# Upper counts 3
# Special counts 2
def counter(mystr):
    count_num=0
    count_lower=0
    count_upper=0
    count_special=0
    for i in mystr:
        if i.isnumeric()==True:
            count_num +=1
        elif i.islower()==True:
            count_lower +=1
        elif i.isupper()==True:
            count_upper +=1
        else:
            count_special +=1

    print(f"Numeric count : {count_num}")
    print(f"Lower count : {count_lower}")
    print(f"Upper count : {count_upper}")
    print(f"Special count : {count_special}")
    return ""

mystr = input("Enter a String : ")
# Calling function
res = counter(mystr)
# Printing the result
print(res)
# Output 
# Enter a String : @pyThOnlobb!Y34
# Numeric count : 2
# Lower count : 8
# Upper count : 3
# Special count : 2
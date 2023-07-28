# 1. Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of given two numbers.

def gcd(x,y):
    if x>y:
        small=y
    else:
        small=x
    for i in range(1,small+1):
        if x%i==0 and y%i==0:
            gcd_num = i
    return gcd_num
x = int(input("Enter first number : "))
y = int(input("Enter second number : "))
# Calling function 
res = gcd(x,y)
# Printing result 
print(f"GCD of the {x} and {y} is : {res}")

# Output1
# Enter first number : 60
# Enter second number : 65
# GCD of the 60 and 65 is : 5
# Output2
# Enter first number : 12
# Enter second number : 60
# GCD of the 12 and 60 is : 12
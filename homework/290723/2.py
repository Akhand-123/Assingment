# 2. Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print average and product of all numbers.
from functools import reduce
l = []
def func():
    while True:
        num = input("Enter input : ").lower()
        print("Press 'q' to quite else press enter")
        if num == 'q':
            break
        else:
            l.append(int(num))
        
    sum = reduce(lambda x,y:x+y,l)
    avg = sum/len(l)
    prod = reduce(lambda x,y:x*y,l)
    print(f"Average of all the number entered is : {avg}")
    print(f"Product of all the number entered is : {prod}")
    return ""
# calling function 
res = func()
# Printing restult
print(res)

# Output
# Enter input : 1
# Press 'q' to quite else press enter
# Enter input : 2
# Press 'q' to quite else press enter
# Enter input : 3
# Press 'q' to quite else press enter
# Enter input : 4
# Press 'q' to quite else press enter
# Enter input : 5
# Press 'q' to quite else press enter
# Enter input : 6
# Press 'q' to quite else press enter
# Enter input : 7
# Press 'q' to quite else press enter
# Enter input : q
# Press 'q' to quite else press enter
# Average of all the number entered is : 4.0
# Product of all the number entered is : 5040



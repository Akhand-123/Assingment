# 1.) Write a python program for given example :
# example: a4b3c2
# output: aaaabbbcc
import re
mystr = input("Enter a string : ")
l=list(mystr)
# print(l)
l1 = re.findall('[a-z]',mystr)
l2 = re.findall('\d',mystr)
for i in range(len(l1)):
    print(l1[i]*int(l2[i]),end="")


# output:
# Enter a string : a4b3c2
# aaaabbbcc

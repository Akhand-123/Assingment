# Q4. Write a program to print the first non-repeated character from a string?
def func(mystr):
    l = []
    for i in mystr:
        if mystr.count(i)>1:
            continue
        else:
            l.append(i)
    return l[0]

mystr = input("Enter a string : ")
# function calling
res = func(mystr)
# printing result
print(res)
        
# output
# Enter a string : geeks
# g
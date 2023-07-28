# 4. Write a python program to sort letters of word by lower to upper case format.

# Input:
# Enter a String: pytHOnloBBy
# Expected output : p y t n l o y H O B B

def sort_lower_upper(mystr):
    l = []
    for i in mystr:
        if i.islower() == True:
            l.append(i)
    for i in mystr:
        if i.isupper() == True:
            l.append(i)
    return (" ".join(l))

mystr = input("Enter a string to see the magic : ")
# Calling the function
res = sort_lower_upper(mystr)
# Printing the result
print(res)
# Output
# Enter a string to see the magic : pytHOnloBBy
# p y t n l o y H O B B







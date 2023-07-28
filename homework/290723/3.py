# 3. Write a program to remove duplicates in a string(Without Using Sets).

# Input: pythonlobby
# Expected output: p y t h o n l b

def remove_duplicate(mystr):
    l = []
    for i in mystr:
        if i in l:
            continue
        else:
            l.append(i)
    return (" ".join(l))
mystr = input("Enter a string : ")
# Calling function
res = remove_duplicate(mystr)
# printing the restult
print(res)

# Output
# Enter a string : pythonlobby
# p y t h o n l b
    
    















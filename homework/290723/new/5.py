# Create a python function that takes a list of strings as input and returns a new containing only the strings with the maximum length.
def func(l):
    max_len = 0
    for i in range(len(l)):
        if len(l[i])>max_len:
            max_len = len(l[i])
            a = l[i]
    return a
print("Enter element in the list with seperated whitespace")
l = list(map(str, input().split()))
res = func(l)
print(f"Maximum length of string in the list is : {res}")
        
# Output:  
# Enter element in the list with seperated whitespace
# python java php programming ruby
# Maximum length of string in the list is : programming
# ​
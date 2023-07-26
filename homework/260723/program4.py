# 4.) Check if two lists have at-least one element common or not
# Input : a = [1, 2, 3, 4, 5]
# b = [5, 6, 7, 8, 9]
# Output : True
# Input : a=[1, 2, 3, 4, 5]
# b=[6, 7, 8, 9]
# Output : False

print("Enter element in list a seperated via whitespace")
a = list(map(int,input().split()))
print("Enter element in list b seperated via whitespace")
b = list(map(int,input().split()))
if set(a).intersection(set(b)) != set():
    print(True)
else:
    print(False)
    
# Output1
# Enter element in list a seperated via whitespace
# 1 2 3 4 5
# Enter element in list b seperated via whitespace
# 5 6 7 8 9
# True
# Output2
# Enter element in list a seperated via whitespace
# 1 2 3 4 5
# Enter element in list b seperated via whitespace
# 6 7 8 9
# False
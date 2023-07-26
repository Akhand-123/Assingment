# 2.) Python program to interchange first and last elements in a list
# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

mylist = list(map(int,input().split()))
print(f"list before swapping : {mylist}")
temp = mylist[0]
mylist[0] = mylist[-1]
mylist[-1] = temp
print(f"list after swapping : {mylist}")

# Output:
# list before swapping : [12, 35, 9, 56, 24]
# list after swapping : [24, 35, 9, 56, 12]
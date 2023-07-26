# 3.) Python program to find second largest number in a list
# Input : [12, 10,35, 9, 56, 24,56,55]
# Output : 55

print("Enter a list element with whitespace line")
l = list(map(int,input().split()))
a = set(l)
b = list(a)
b.sort()
print(b[-2])

# Output
# Enter a list element with whitespace line
# 12 10 35 9 56 24 56 55
# 55
# 1.Create a python function that takes a list if integers as input and returns the sum of all positive integers in the list.
def func(l):
    sum = 0
    for i in l:
        if i>0:
            sum +=i
    return sum
l = list(map(int,input().split()))
res = func(l)
print(l)
print(res)
# output:
# -2 -5 12 25 56
# [-2, -5, 12, 25, 56]
# 93
# 3.Create a python function that takes a list of numbers as input and returns the largest even number in the list.
def func(l):
    max_num = 0
    for i in l:
        if i>max_num and i%2==0:
            max_num=i
    return max_num
print("Input a list of element sepearted by whitespace")
l = list(map(int,input().split()))
res = func(l)
print(f"So the largest even no. in the list is {res}")

# Output:
# Input a list of element sepearted by whitespace
# 1 2 67 89 56
# So the largest even no. in the list is 56
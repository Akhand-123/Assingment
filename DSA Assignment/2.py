# Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

def reverse_array(arr):
    return arr[::-1]
arr = list(map(int,input("Enter element in array seperated with whitespace : ").split()))
# calling function
res = reverse_array(arr)
# printing result
print(res)

# Output:
# Enter element in array seperated with whitespace : 1 2 3 4 5 6 7 8
# [8, 7, 6, 5, 4, 3, 2, 1]
# Q10. Write a program to find the smallest number using a stack
class Stack:
    def __init__(self):
        self.array=[]

    def push(self,data):
        self.array.append(data)
        return self.array
    def pop(self):
        if len(self.array)<1:
            return "You cannot perform operation in array it is empty"
        elif len(self.array)>0:
            return self.array.pop(-1)
    def peek(self):
        return self.array[-1]
stack1 = Stack()
n = int(input("Enter the size of the stack : "))
for i in range(n):
    data = int(input("Enter data : "))
    stack1.push(data)
    
# stack2 = Stack()
def min_in_stack(s1):
    s2 = Stack()
    min = 0
    for i in range(n):
        a=s1.pop()
        print(a)
        if a > min:
            min = a
    return min

res = min_in_stack(stack1)
print(res)
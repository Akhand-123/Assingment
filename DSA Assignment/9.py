# Q9. Write a program to reverse a stack.
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
stack2 = Stack()
n = input("Enter no. of element that you want to enter in stack : ")
for i in range(int(n)):
    data = int(input("Enter data : "))
    stack1.push(data)
print(f"stack : {stack1.array}")
print(f"Peek of stack is : {stack1.peek()}")
while len(stack1.array) != 0:
    stack2.push(stack1.pop())
print(f"Reverse of stack : {stack2.array}")
print(f"Peek of reverse stack is : {stack2.peek()}")

# Output
# Enter no. of element that you want to enter in stack : 5
# Enter data : 1
# Enter data : 23
# Enter data : 45
# Enter data : 67
# Enter data : 89
# stack : [1, 23, 45, 67, 89]
# Peek of stack is : 89
# Reverse of stack : [89, 67, 45, 23, 1]
# Peek of reverse stack is : 1

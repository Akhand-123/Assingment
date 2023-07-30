# Implement a Calculator Class

class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return print(self.a+self.b)
    def subtract(self):
        return print(self.b-self.a)
    def multiply(self):
        return print(self.a*self.b)
    def divide(self):
        return print(self.b/self.a)
    
a = float(input("Enter the value of a : "))
b = float(input("Enter the value of b : "))
obj = Calculator(a,b)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()

# Output
# Enter the value of a : 10
# Enter the value of b : 94
# 104.0
# 84.0
# 940.0
# 9.4
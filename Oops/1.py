# Challenge1:Square Numbers and Returns Their sum
class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def sqSum(self):
        sum = 0
        sum = self.x**2 +self.y**2 +self.z**2
        return sum
# Createing the object
obj = Point(1,3,5)
# Printing the result 
print(obj.sqSum())

# Output:
# 35
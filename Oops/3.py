# Implement the Complete Student class

class Student:
    
    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name
    def setRollNumber(self,rollno):
        self.__rollno = rollno
    def getRollNumber(self):
        return self.__rollno
x = Student()
x.setName("Akhand Pratap Singh")
x.setRollNumber(2)
print(x.getName())
print(x.getRollNumber())

# Output:
# Akhand Pratap Singh
# 2
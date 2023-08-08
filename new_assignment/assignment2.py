class Dog:
    def __init__(self,name,age,coat_color):
        self.name = name 
        self.age = age
        self.coat_color = coat_color
    def description(self):
        print(f"Dog name is {self.name} and it's age is {self.age}")
    def get_info(self):
        print(f"Coat color of dog is of {self.coat_color}")

class JacRussellTerrier(Dog):    
    def guard(self):
        print("This bread is very active in guarding ")
    def familypet(self):
        print("These dogs are good family pet")

class Bulldog(Dog):    
    def dangerous(self):
        print("This bread of dog is kind of dangerous for theves")
    def courageous(self):
        print("These bread of dogs are very courageous")
a = Bulldog("Tommy",7,"Black")
b = JacRussellTerrier("Tiger",6,"golden")
a.description()
a.get_info()
a.dangerous()
a.courageous()
b.description()
b.get_info()
b.guard()
b.familypet()

# Output
# Dog name is Tommy and it's age is 7
# Coat color of dog is of Black
# This bread of dog is kind of dangerous for theves    
# These bread of dogs are very courageous
# Dog name is Tiger and it's age is 6
# Coat color of dog is of golden
# This bread is very active in guarding
# These dogs are good family pet
# Task 1: Implement properties as innstance variables, and set them to None or 0
class  Account:  
    
    def __init__(self,title=None,balance=0):
        self.title = title
        self.balance = balance    
        


class SavingAccount(Account):
    def __init__(self,title=None,balance=0,intrestRate=0):
        super().__init__(title,balance)       
        # self.title = "Ashish"  #Initializing the title in child class       
        # self.balance = 5000 #Initializing the balance in the child class
        self.interestRate=intrestRate
        
# Creating object for the base class 
a = Account("Akhand",5000) #Creating obj of the base class 
# Printing the instance variable of Account class 
print(a.title)
print(a.balance)
# Creating the object for the child class 
b = SavingAccount("Ashish",5000,5) #Creating obj for the derived class
print(b.title)  
print(b.balance)
print(b.interestRate)  

# Output
# Akhand
# 5000
# Ashish
# 5000
# 5

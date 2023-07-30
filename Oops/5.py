# Handling a Bank Account
class Account:
   
    def __init__(self,title=None,balance=0):
        
        self.title = title
        self.balance = balance
        
    def deposit(self,amount):
        self.balance += amount
    def withdrawal(self,amount):
        if amount>self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        
        # return self.amount
    def getBalance(self):        
        return self.balance
    
        
class SavingsAccount(Account):
    def __init__(self,title=None,balance = 0,interestRate=0):        
        super().__init__(title,balance)        
        self.intrestRate = interestRate
        # amount = 0
        
    def intrestAmount(self):
        self.intrestAmount = (self.intrestRate*self.balance)/100
        return self.intrestAmount

# Code to test
def main():
    a = SavingsAccount("Ashish",2000,5)
    dp_amt = int(input("Enter amount that you want to deposit in your account : "))
    a.deposit(dp_amt)
    print("Amount deposited successfully")
    print(f"Your current balance is : Rs 2{a.getBalance()} ")

    amount = int(input("Enter the amount that you want to withdrawal : "))
    try:
        a.withdrawal(amount)
        print("Withdrawal successfully")    
       
    except ValueError:
        print("Insufficient balance") 
    print(f"Your current balance is : Rs {a.getBalance()} ")
    print(f"Your current balance is : Rs {a.getBalance()} ")
    
    print(a.intrestAmount())


if __name__=="__main__":
    main()
    
# Output
# Enter amount that you want to deposit in your account : 500
# Amount deposited successfully
# Your current balance is : Rs 22500 
# Enter the amount that you want to withdrawal : 500
# Withdrawal successfully
# Your current balance is : Rs 2000 
# Your current balance is : Rs 2000 
# 100.0 
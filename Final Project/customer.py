import json
import random
import sys
class User:
    def __init__(self):
        self.customer_detail = {}
        self.order_list=[]
        self.food_list=[]
        self.oder_history_list =[]
        self.order_history_dict = {}
    
    def Registation(self):        
        self.name = input("Enter your name : ")
        self.phone = input("Enter your phone no. : ")
        self.email = input("Enter your email id : ")
        self.address = input("Enter your address : ")
        self.password = input("Enter your password : ")
        self.user_detail = {"User name":self.name,"phone":self.phone,"email":self.email,"address":self.address,"password":self.password}
        self.customer_detail[self.email]=self.user_detail
        with open("registation.json","w") as f:
            json.dump(self.customer_detail,f,indent=4)
        return self.customer_detail
    
    def logIn(self):        
        id = input("Enter your email for login : ")
        password = input("Enter your password : ")
        with open("registation.json","r") as f:
            data = json.load(f)
        # print(data)
        self.auth = []
        for k,v in data.items():
            for key,value in v.items():
                if key == "email":
                    self.auth.append(value)
                if key == "password":
                    self.auth.append(value)
        # print(self.auth)
        if id in self.auth and password in self.auth:
            return True
        else:
            return False
        
    
        
    def place_new_order(self):
        self.food_list = []
        with open("food.json","r") as f:
            food_item = json.load(f)
        for k,v in food_item.items():
            self.food_list.append(v)
        # print(self.food_list)        
        for i in range(len(self.food_list)):
            print(f"{i+1}: {self.food_list[i]['Food_name']} ({self.food_list[i]['Stock']} pieces) [INR {self.food_list[i]['Food Price']}]")
            order_dict={i+1:self.food_list[i]['Food_name']}
        self.order_list = list(map(int,input("Enter your food no. which you want to order : ").split()))
        
        
        for i in self.order_list:
            print(f"Your selcted item is : {self.food_list[i-1]['Food_name']}")
            self.oder_history_list.append(self.food_list[i-1]['Food_name'])
            
            
        while True:
            order = input("Press 1 for placing your order or pres anything for discard : ")
            if int(order)==1:
                self.order_history_dict[len(self.oder_history_list)]=self.oder_history_list            
                print("Order placed successfully!!! Thank you for placing order")
                with open("Order_history.json","w") as f:
                    json.dump(self.order_history_dict,f,indent=4)
                break
            else:
                break
        return self.oder_history_list
    def Order_History(self): 
        with open("Order_history.json","r") as f:
            data_history=json.load(f)  
        print(data_history) 
        # print(self.oder_history_list)
        for k,v in data_history.items():
            print(f"Order histroy id : {k} || Order items : {v}")
            self.oder_history_list.append(v)                
        return self.oder_history_list
    
    def Update_profile(self):
        
        with open("registation.json","r") as f:
            data = json.load(f)
        print(data)
        id = input("Enter the id from which you want to update : ")
        field = input("Enter the field from which you want to update : ")
        updated_value = input("Enter your updated value : ")
        data[id][field]=updated_value
        with open("registation.json","w") as f:
            json.dump(data,f,indent=4)
        return data
    
    def menue(self):
        menue_list = ["Place New Order","Order History","Update Profile"]
        print("*"*100)
        for i in range(len(menue_list)):
            print(f"Press {i+1} for {menue_list[i]}")
        print("*"*100)
        while True:
            a = int(input("Enter no. from menu : "))
            if a == 1:
                return self.place_new_order()
            elif a == 2:
                return self.Order_History()
            elif a == 3:
                return self.Update_profile()
            else:
                sys.exit()
        
            
x = User()
# print(x.place_new_order())
# print("func is called")
print(x.Order_History())
# print(x.Update_profile())
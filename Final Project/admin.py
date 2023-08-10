import random
import json

class Admin:
    def __init__(self):
        self.food = {}
    
    def admin_login(self,username,password):
        if username=="admin" and password=="password":
            return True
        return False
        
    def Add_food_Items(self):
        self.food_id = random.randint(1,10000)
        self.food_name = input("Enter Food name : ")
        self.quantity = input("Enter Food quantity of the food : ")   
        self.price = float(input("Enter Price of the Food : "))
        self.discount = float(input("Enter discount on the Food : "))
        self.stock = int(input("Enter Stock : "))
        self.item = {"Food_id":self.food_id,"Food_name":self.food_name,"Food Quantity":self.quantity,"Food Price":self.price,"Discount":self.discount,"Stock":self.stock}
        self.food[self.food_id] = self.item
        with open("food.json","w") as f:
            json.dump(self.food,f,indent=4)
        return self.food
    
    def Remove_Food(self):
        with open("food.json",'r') as f:
            ele = json.load(f)
        for k,v in ele.items():
            print(f"'food id':{k}, 'food item': {v}")
        id = (input("Enter the Food Id which you want to delete : "))    
        del ele[id]
        with open("food.json","w") as f:
            json.dump(ele,f,indent=4)
        return self.food
    
    def View_Food_items(self):
        with open("food.json",'r') as f:
            ele = json.load(f)
        for k,v in ele.items():
            print(f"'food id':{k}, 'food item': {v}")
            
    def Edit_Food_items(self):
        with open("food.json",'r') as f:
            ele = json.load(f)
        for k,v in ele.items():
            print(f"'food id':{k}, 'food item': {v}")
        id = (input("Enter the Food Id which you want to update : "))
        field = input("Enter the Field Which you want to update: ")
        updated_value = input("Enter the undated value : ")
        ele[id][field]=updated_value
        with open("food.json","w") as f:
            json.dump(ele,f,indent=4)
        return self.food
        
# x = Admin()
# x.Add_food_Items()
# print("*"*100)
# x.Add_food_Items()
# x.Add_food_Items()
# print("*"*100)
 
# x.Remove_Food()
# x.View_Food_items()
# x.Edit_Food_items()
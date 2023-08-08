import json
# num = int(input("Enter the number of employees : "))
# d1 = {}
# # By this process we enter the name of 5 employees and stored in json file
# for i in range(1,num+1):
#     name = input(f"Enter the name of {i} employee : ")
#     DOB = input(f"Enter the DOB of {i} employee : ")
#     height = input(f"Enter the height of {i} employee : ")
#     city = input(f"Enter the city of {i} employee : ")
#     state = input(f"Enter the state of {i} employee : ")
#     print("*"*100)
#     d = {"name":name,"DOB":DOB,"height":height,"city":city,"state":state}
#     d1[i]=d
#     with open("employee.json","w") as f:
#         json.dump(d1,f,indent=4)
with open("employee.json","r") as f:
    d = json.load(f)
# print(d)
class Employee:
    def __init__(self):
        pass
    def list_of_employee(self):
        # self.a = []
        self.b = []
        for key,value in d.items():
            self.b.append(value)
            
       
        return self.b
    
x = Employee()
print(x.list_of_employee())

# Output:
# [{'name': 'A', 'DOB': '01/01/2000', 'height': '5.5', 'city': 'Indore', 'state': 'Madhya Pradesh'}, {'name': 'B', 'DOB': '02/02/2001', 'height': '5.6', 'city': 'gurgram', 'state': 'Delhi'}, {'name': 'C', 'DOB': '03/03/2002', 'height': '5.9', 'city': 'Rewa', 'state': 'Madhya Pradesh'}, {'name': 'D', 'DOB': '10/09/2001', 'height': '6', 'city': 'Hyderabad', 'state': 'Andhra Pradesh'}, {'name': 'E', 'DOB': '12/12/1996', 'height': '5.8', 'city': 'Lucknow', 'state': 'Uttra Pradesh'}]
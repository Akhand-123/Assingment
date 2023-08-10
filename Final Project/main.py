from admin import *
from customer import *
import sys
admin = Admin()
customer = User()
while True:
    print("Press 1 for Admin Login : ")
    print("Press 2 for User login : ")
    print("Press 3 for User Registation : ")
    print("Press 4 for Exit : ")
    print("*"*100)
    choice = int(input("Enter Your choice : "))
    print("*"*100)
    if choice == 1:
        print("*****************************************************Admin Login**********************************")
        username = input("Enter Admin Username : ")
        password = input("Enter Admin password : ")
        temp = admin.admin_login(username,password)
        if temp:
            print("Logged in successfully")
            print("Press 1 for Add food items")
            print("Press 2 for Remove food items")
            print("Press 3 for View food items")
            print("Press 4 for Edit food items")
            
            option = int(input("Enter your choice : "))
            if option == 1:
                a = int(input("Enter how many food items you want to add"))
                for i in range(a):                    
                    print(admin.Add_food_Items())
                print("*"*100)
                print("Food Item addes Successfully")
                print("*"*100)
            
            elif option==2:
                print(admin.Remove_Food())
                print("*"*100)
                print("Food item removed successfully")
                print("*"*100)
            
            elif option==3:
                print(admin.View_Food_items())
                print("*"*100)
                
            elif option==4:
                print(admin.Edit_Food_items())
                print("*"*100)
                print("Food item Edited successfully")
                print("*"*100)
            
            else:
                print("Please give Valid input")
        
        else:
            print("Please give Valid Username and Password")
    elif choice==2:
        print("*****************************************************User Login**********************************")
        temp=customer.logIn()
        if temp:
            print("Logged in successfully")
            print("Press 1 for view menue")
            user_option = int(input("Enter your choice : "))
            if user_option == 1:
                customer.menue()
            else:
                print("Please give valid input")
        else:
            print("You are not registered in our app please do registation first")
    elif choice==3:
        print("**********************************Registation***************************************************")
        customer.Registation()
        print("Registaion Successfully completed now you can use our app.")
    elif choice==4:
        print("Thank you for using our application")
        sys.exit()
        
    
            
        
            
        
            
                
            
from datetime import datetime
from Coustomers import *
from Supper_user import *

cos = Courstomer()
bus = Super_User()

print()
print(f"""Date & time : {datetime.today()}
@aurthor :  Ansh Srivastav""")

while True:
    print("--------------------------------------------------->>>>>>> Welcome to Booty Shoes App <<<<<<<-----------------------------------------------\n")
    print("+="*55)
    print(" 1 For Register As Business User ")
    print(" 2 For Login As Business User")
    print(" 3 For Register As Coustomer")
    print(" 4 For Login As Coustomer")
    print(" 0 For Exit")
    print("+="*55)
    choice = input(" Please Choose An Options :")
    
    if choice == "1":
        print(bus.registered())
    
    if choice == "2":
        if bus.login() == True:
            while True:
                print("~"*51)
                print(" 1. For View Profile ")
                print(" 2. For Update Profile ")
                print(" 3. For Add Shoes ")
                print(" 4. For View Added Shoes ")
                print(" 5  For Update Shoes ")
                print(" 0  For Exit ")
                print("~"*51)
                bus_choice = input(" Select a Choice : ")

                if bus_choice == "1":
                    print(bus.view_profile())
                
                if bus_choice =="2":
                    print(bus.update_profile())
                
                if bus_choice == "3":
                    print(bus.add_shoes_with_category())
                
                if bus_choice == "4":
                    print(bus.View_added_shoes())
                
                if bus_choice == "5":
                    print(bus.Edit_shoes_Details())
                
                if bus_choice == "0":
                    break
    if choice == "3":
        print(cos.registered())
    
    if choice == "4":
        if cos.login() == True:
            while True:
                print("~"*51)
                print(" 1. For View Your Profile ")
                print(" 2. For Update Profile ")
                print(" 3. For View All Shoes ")
                print(" 4. For Search An Item ")
                print(" 5. For Filter An Items ")
                print(" 6. For Mange Cart ")
                print(" 7. For Place Order ")
                print(" 0 For Exit ")
                print("~"*51)

                cous_input = input(" Select a Choise :")
                if cous_input == "1":
                    print(cos.View_profile())
                
                if cous_input == "2":
                    print(cos.update_profile())
                
                if cous_input == "3":
                    print(cos.view_items())
                
                if cous_input == "4":
                    print(cos.search())

                if cous_input == "5":
                    print(cos.filter_record())
                
                if cous_input == "6":
                    while True:
                        print("+="*23)
                        print(" 1. For Add Items in Cart ")
                        print(" 2. For View Added Item to Cart")
                        print(" 3. For Remove Item From Your Cart ")
                        print(" 0 For Exit ")
                        print("+="*23)
                        cart_option = input(" Choose Your Option ")
                        
                        if cart_option == "1":
                            print(cos.Add_item_to_cart())
                        
                        if cart_option == "2":
                            print(cos.view_cart())
                        
                        if cart_option == "3":
                            print(cos.remove_item())
                        
                        if cart_option == "0":
                            break
                if cous_input =="7":
                    while True:
                        print("+="*23)
                        print(" 1 For Place An Order ")
                        print(" 2 For View Previous History ")
                        print(" 3 For Clear History")
                        print(" 0 For Exit ")
                        print("=+"*23)
                        ord_choice = input(" Select An Options :")
                        if ord_choice =="1":
                            print(cos.place_order())
                        
                        if ord_choice =="2":
                            print(cos.view_history())
                        
                        if ord_choice == "3":
                            print(cos.clear_history())
                        
                        if ord_choice == "0":
                            break
                    
                if cous_input == "0":
                    print("  Bye ")
                    break
    
    if choice == "0":
        print()
        print( "       🙂 Thanks For Use App  🙂      ")
        break



                    


            






from office_domain import *
import random
import json
from datetime import datetime 

class Courstomer:
    courser.execute('USE db_booty')
    def __init__(self):
        pass

    def registered(self):
        print("----------->>> Registered Domain <<<--------------\n")
        User_ID = random.randint(1,100)
        try:
            Name = input("Enter Your Name :")
            try:
                Age = int(input("Enter Your AGE :"))
                
            except :
                print()
                return "    Please Enter Valid AGE      "  
            else:
                try:
                   mobile = int(input("Enter Your Mobile Number :"))
                except :
                    return "Enter A Valid Number"     
                gender = input("Enter Your Gender Here :")
                
                email = input("Enter Your Email ID :")
                res = self.check_email(email)
                if res == False:
                    Password = input("Enter Your Password Here :")
                    print()
                    print("----------->>> Address <<<-----------\n")
                    Country = input("Enter Your Country Name :")
                    State = input('Enter Your State Name :')
                    City = input("Enter Your City Name :")
                    LandMark = input("Enter Your Nearest LandMark :")
                    try:
                        Pincode = int(input("Enter Your PinCode Here :"))
                    except :
                        return "Enter A Valid Pincode"
                else:
                    print()
                    print("               Account Alread Exist                     \n")
                    return False
        except Exception as e :
            print(e)
        else:
            try:
                query = "Insert into coustomer values ({},'{}',{} ,'{}' , {} , '{}' , '{}' , '{}' , '{}' , '{}' ,'{}' , {} )".format(
                    User_ID,Name.title().strip(),Age,gender.upper().strip(),mobile,email.lower().strip(),Password,Country.upper().strip(),State.title().strip(),City.title().strip(),LandMark.title().strip(),Pincode
                )
                courser.execute(query)
                mybd.commit()
                print()
                print("         🌟🌟   Account Create Sucessfully 🌟🌟      \n")
                return True
            except Exception as e:
                print(e)


    def check_email(self,Email_Id):
        query = "select Email_ID from COUSTOMER"
        courser.execute(query)
        temp = courser.fetchall()
        d = 0
        for i in range(len(temp)):
            if Email_Id in temp[i]:
                d=1
        if d ==1:
            return True
        return False
    
    def login(self):
        print("----------->> Login Domin <<-------------\n")
        self.email = input("Enter Your Mail ID :")
        temp = self.check_email(self.email.lower())
        if temp == True:
            courser.execute('select Password from coustomer where Email_ID = "{}"'.format(self.email.lower()))
            temp = courser.fetchall()
            password= input("Enter Your Password :")
            if temp[0][0] == password:
                print(   )
                print("         🌟🌟Login Sucessfully 🌟🌟          ")
                return True
            else:
                print()
                print("    ❌  InValid Password  ❌    ")
                return False
        else:
            print()
            return "        ❌  User not Exist    ❌        "
            

    def View_profile(self):
        print()
        print("------------------->>>>  Your Profile <<<<-------------------\n")
        query = (f"select * from coustomer where Email_ID = '{self.email}' ").format()
        courser.execute(query)
        temp = courser.fetchall()
        print(f"""
 User_ID                     :               {temp[0][0]}
 Name                        :               {temp[0][1]}
 Age                         :               {temp[0][2]}
 Gender                      :               {temp[0][3]}
 Mobile_Number               :               {temp[0][4]}
 Email_ID                    :               {temp[0][5]}
 Password                    :               {temp[0][6]}
 Country                     :               {temp[0][7]}
 State                       :               {temp[0][8]}
 City                        :               {temp[0][9]}
 Landmark                    :               {temp[0][10]}
 Pincode                     :               {temp[0][11]}
 """)


    def update_profile(self):
        print()
        print("------------->>> Update Profile <<<--------------\n")
        print(self.View_profile())
        try:
            field = input("Please Select Your Details :")
            updated_value = input("Enter Your Updated Value :")
            query = "Update coustomer set {}= '{}' where Email_Id = '{}'".format(field,updated_value,self.email)
            courser.execute(query) 
            mybd.commit()
        except Exception as e:
            print(e)
        else:
            print()
            print(f"---->>> Your Profile Got Update \nand the updated {field} is {updated_value}")
            print()


    def search(self):
        search = input("Search Your Shoes [Formal Shoes | Nike Shoes ] :").title()
        query = "select ID , Brands ,Size, Price from tbl_shoes where Shoes_Type Like '{}%' or Brands Like '{}%' ".format(search.title().strip() , search.title().strip())
        courser.execute(query)
        self.res = courser.fetchall()
        print("------------->>>>> Result Based on Your Search <<<<<-------------\n")
        for i in range(len(self.res)):
            print(f""" 
 Shoes ID                 :             {self.res[i][0]}
 Shoes Name               :             {self.res[i][1]}
 Shoes Size               :             {self.res[i][2]}
 Shoes Price              :             {self.res[i][3]}""")    

    def view_items(self):
        courser.execute("select ID, Brands ,Shoes_Type ,Size, Price from tbl_shoes") 
        record  = courser.fetchall()
        for i in range(len(record)):
            print(f"""
 Shoes ID                 :             {record[i][0]}
 Shoes_Type               :             {record[i][1]} 
 Shoes Name               :             {record[i][2]}
 Shoes Size               :             {record[i][3]}
 Shoes Price              :             {record[i][4]}""")    


    def filter_record(self):
        print(self.view_items())
        while True:
            print("+="*55)
            print(" 1 Filter By Shoes Types ")
            print(" 2 Filter By Price Range ")
            print(" 3 Filter By Size  ")
            print(" 0 For Exit ")
            print("+="*55)
            choiec = input(" Press the Particular key which you want to filter :")
            if choiec == "1":
                shoes_choise = input("Enter Your Choice :")
                query = " select ID , Brands ,Size, Price from tbl_shoes where shoes_type = '{}' ".format(shoes_choise.title().strip())
                courser.execute(query)
                temp = courser.fetchall()
                print("""--------------->>>  Filter By Records <<<------------""")
                for i in range(len(temp)):
                    print(f""" 
 Shoes ID                 :             {temp[i][0]}
 Shoes Name               :             {temp[i][1]}
 Shoes Size               :             {temp[i][2]}
 Shoes Price              :             {temp[i][3]}
 
 """)
            if choiec == "2":
                start_price = int(input(" Enter Your Stating Range Price :"))
                End_price =   int(input(" Enter Your Last Range Price   :"))
                courser.execute("select ID , Brands ,Size, Price from tbl_shoes where Price >= {} and price <= {}".format(start_price,End_price))
                temp = courser.fetchall()
                print("""--------------->>>  Filter By Records <<<------------""")
                for i in range(len(temp)):
                    print(f""" 
 Shoes ID                 :             {temp[i][0]}
 Shoes Name               :             {temp[i][1]}
 Shoes Size               :             {temp[i][2]}
 Shoes Price              :             {temp[i][3]}
 
 """)
            if choiec == "3":
                shoe_size = input(" Enter Your Shoes Size :")
                courser.execute("select ID , Brands ,Size, Price from tbl_shoes where size = '{}'".format(shoe_size))
                temp = courser.fetchall()
                print("""--------------->>>  Filter By Records <<<------------""")
                for i in range(len(temp)):
                    print(f""" 
 Shoes ID                 :             {temp[i][0]}
 Shoes Name               :             {temp[i][1]}
 Shoes Size               :             {temp[i][2]}
 Shoes Price              :             {temp[i][3]}
 
 """) 
            if choiec =="0":
                break
          

    def Add_item_to_cart(self):
        d = {}
        while True:
            print("------------------------------------------")
            print("0 For Exit ")
            print("Press Any Key for Add shoe in your Cart ")  
            print("------------------------------------------\n")
            choise = input("-->>")
            if choise ==  "0":
                break 
            
            item_name = input("Enter Shoes ID Number Which You Want to Add  :")
            try:
                Qty = int(input("Enter How Much Shoes You Want :"))
                courser.execute("select ID ,  Shoes_Type, Brands ,Size, Price from tbl_shoes where ID = '{}'".format(item_name))
                t = courser.fetchall()
                for i in range(len(t)):
                    query = "insert into cart values ({},'{}','{}',{},{},{},'{}')".format(t[i][0],t[i][1],t[i][2],t[i][3],Qty,t[i][4],self.email)
                    courser.execute(query)
                    mybd.commit()
                    print()
                    print("   Your Item Got Added Sucessfully ")
            except:
                return " Enter A Valid Record "
            
    def view_cart(self):
        courser.execute("select * from cart where User_ID = '{}'".format(self.email))
        content = courser.fetchall()
        print("------------>>> Your Added Item in Cart is <<-------------\n")
        for i in range(len(content)):
                                print(f""" 
 Shoes ID                 :             {content[i][0]}
 Shoes Type               :             {content[i][1]}
 Shoes Brand              :             {content[i][2]}
 Shoes Size               :             {content[i][3]}
 Shoes QTY                :             {content[i][4]} 
 Shoes Price              :             {content[i][5]}  
 """) 
    
    def remove_item(self):
        shoes_id = input("Enter Shoes ID Which You Want to Remove :")
        courser.execute("delete from cart where ID = {}".format(shoes_id))
        print()
        print("          Your Item Got Remove        ")        
    
    def place_order(self):
        while True:
            print("------------->> Order Domain <<< ----------- \n")
            print(" Are Sure your Want to Order you Cart ")
            print("+="*55)
            print(" 1. For Contiune ")
            print(" 2. For Exit ")
            print("+="*55)
            choise = input(" Choose Your Options :")
            if choise == "1":
                query =  "select * from cart where User_ID = '{}'".format(self.email)
                courser.execute(query)
                temp = courser.fetchall()
                now = datetime.now()
                formated_date = now.strftime('%Y-%m-%d %H:%M:%S')
                for i in range(len(temp)):
                    query2 = "insert into order_history values ({},'{}',{},{},{},'{}','{}')".format(temp[i][0],temp[i][2],temp[i][3],temp[i][4],temp[i][5],temp[i][6],formated_date)
                    courser.execute(query2)
                    mybd.commit()
                    print()
                    return "  🎊🎊   Order Place Sucessfully  🎊🎊 "
            if choise =="0":
                print()
                print( "          🙂 Thank You 🙂         ")
                break
    
    def view_history(self):
        courser.execute("select * From order_history")
        temp = courser.fetchall()
        print("----------->>> Your Previous Record is <<<------------\n")
        for i in range(len(temp)):
            print(f""" 
ID              :               {temp[i][0]}
Shoes           :               {temp[i][1]}
Shoes Size      :               {temp[i][2]}
Shoes Qty       :               {temp[i][3]}
Shoes Price     :               {temp[i][4]}
Order Date      :               {temp[i][6]}
            """)
    
    def clear_history(self):
        courser.execute("delete from order_history where User_ID = '{}' ".format(self.email))
        print( "  Your History is Cleared  ")









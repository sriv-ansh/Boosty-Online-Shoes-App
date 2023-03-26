from office_domain import *
import json
import random

class Super_User:
    def __init__(self) -> None:
        self.Shoes = {}
    
    courser.execute("use db_booty")
    
    def registered(self):
        print("---------------- >>>   Registered Domin <<<-------------------\n")
        User_ID = random.randint(1,10000000)
        Name = input("Enter Your Name :")
        try:    
            Age = int(input("Enter Your Age Here :"))
            gender = input("Enter Your Gender :")
            Number = int(input("Enter Mobile Number :"))
        except :
            print("Enter A Valid Mobile Number :")
            return ""
        else:
            Email_ID = input("Enter Your Email ID Here :")
            temp = self.ckeck(Email_ID)
            if temp  == True:
                print()
                print( "        Enter Your Valid Email       " )
                return False
            Password  = input("Enter Your Password Here :")
            country = input("Enter Your Country Name :")
            city = input("Enter Your City Name :")
            Pincode = int(input("Enter Your Pin-Code :"))

            try:
                query = "Insert into super_user_details values ({},'{}',{},{},'{}','{}', '{}','{}',{},'{}')".format(User_ID,Name.title().strip(),Age,
                Number,Email_ID.lower().strip(),Password.strip(),country.title().strip(),city.title().strip(),Pincode,gender.title().strip())
                courser.execute(query)
                mybd.commit()
                print()
                print("               Registered Sucessfully          ")    
                return ""
            
            except Exception as e:
                print(e)
                return False


    def ckeck(self,email):
        courser.execute("select Email_ID from super_user_details")
        d = 0
        res = courser.fetchall()
        for i in range(len(res)):
            if email in res[i]:
                d = 1
        if d == 1:
            return True
        return False

    def login(self):
        print("---------------- >>>   Login Domin <<<-------------------\n")
        self.email = input("Enter Your Mail ID :").lower().strip()
        temp = self.ckeck(self.email)
        if temp == True:
            query = ("select Password from super_user_details where Email_ID = '{}'").format(self.email)
            courser.execute(query)
            res  = courser.fetchall()
            password = input("Enter Your Password :")                     
            if password == res[0][0]:
                print()
                print("             🌟✨ Login Sucessfully 🌟✨             ")
                return True
            else:
                print()
                print("       ❌  Incorrect Password Please Try Again   ❌    ")
                return False
        else:
            print()
            print("      ❌  Your Haven't Registered Please Registered First ❌      ")          
            return False
    
    def update_profile(self):
        print("---------------- >>>   Updated  Profile <<<-------------------\n")
        self.view_profile()
        try:
            field = input("Please Select Your Details :")
            updated_value = input("Enter Your Updated Value :")
            query = "Update super_user_details set {}= '{}' where Email_Id = '{}'".format(field,updated_value,self.email)
            courser.execute(query) 
            mybd.commit()
        except Exception as e:
            print(e)
        else:
            print()
            print(f"---->>> Your Profile Got Update \nand the updated {field} is {updated_value}")
            print()


    def view_profile(self):
        print("---------------- >>>   Details Are <<<-------------------\n")
        temp = self.ckeck(self.email)
        if temp == True:
            query = "select * from super_user_details where Email_ID = '{}'".format(self.email)
            courser.execute(query)
            res = courser.fetchall()
            print(f"""
Name :                          {res[0][1]} 
Age  :                          {res[0][2]}
Gender :                        {res[0][9]}
Mobile Number :                 {res[0][3]}
Email ID :                      {res[0][4]}
Password :                      {res[0][5]}
County :                        {res[0][6]}
City :                          {res[0][7]}
Pincode :                       {res[0][8]}
----------------------------------------------------------
            """)
      
   
    def add_shoes_with_category(self):
        print("---------------------->> Add Shoes <<<----------------------------\n")
        while True:
            print(" 0 For Exit ")
            print(" Press Any Key For Enter New Record ")
            key = input("-->")
            print()
            if key != "0":
                try:
                    User_ID = random.randint(1,10000000)
                    Shoes_Type = input("Enter Your Shoes Type :")
                    Brand = input(f"Enter Your Brand Name For {Shoes_Type} :")
                    size = input(f"Enter Your Shoes Size For {Brand} Shoes :")
                    Quentity = input(f"Enter Your Shoes Quentity for {Brand} Shoes :")
                    Price = input(f"Enter Your Price for {Brand} Shoes:")
                    query = "Insert into tbl_shoes values ({},'{}','{}','{}','{}','{}','{}')".format(
                    User_ID,Shoes_Type.title().strip(),Brand.title().strip(),size.strip(),Quentity.strip(),Price.strip(),self.email.lower().strip())
                    courser.execute(query)
                    mybd.commit()
                except Exception as e:
                    print(e)
                else:
                    print()
                    print("             🌟🌟   Shoes Added Sucessfully   🌟🌟               ")
            else:
                break
    
    def View_added_shoes(self):
        temp = self.ckeck(self.email)
        if temp ==True:
            try:
                query = "select * from tbl_shoes where User_ID = '{}'".format(self.email)
                courser.execute(query)
                res = courser.fetchall()
            except Exception as e:
                print(e)
            else:
                print("------------------>>>>  Your Added Shoes Are <<<<-------------------\n")
                for i in range(len(res)):
                    print(f"Your {i+1} Shoes is :")
                    print(f"""
Shoes ID    :                              {res[i][0]}
Shoes_Type  :                              {res[i][1]}                  
Brand       :                              {res[i][2]}                  
Size        :                              {res[i][3]} No.              
Qty         :                              {res[i][4]} Piece            
Price       :                              {res[i][5]} ₹                
------------------------------------------------------------------ 
 \n""")
                    



    def Edit_shoes_Details(self):
        print(self.View_added_shoes())
        try:
            id = input("Enter Your Shoe ID :")
            field= input("Enter Your Field Which You Want to Edit :")
            Update_value = input(f"Enter Your Updated Value for {field} :")
            query = "Update tbl_shoes set {} = '{}' where ID = {}".format(field,Update_value,id)
            courser.execute(query)
            mybd.commit()
            print()
            print(f"---->>> Your {field} Got Updated For Shoes ID {id}\nand the updated {field} is {Update_value}")
            print()
        except Exception as e:
            print(e)


 


                

from main_menu import *
import maskpass

def login():
     count = 0
     while count < 3:
          a = input("Enter the user_id: ")
          b = maskpass.askpass("Enter the password: " ,mask="*")

          with open(f"students/{a}.txt","r") as f :
               val = eval(f.read())
               p = val["password"]
               # print(p)
               q = val["id_status"]
               if b == p:
                    if q == False:
                         print("Your id is blocked")

                    else:
                         print("You Logged In")
                         mainmenu(a)
                         
                    break
               else:
                    count = count+1
                    print("Oops! You entered wrong Password.\n Enter the password again")

     if count == 3:
          val["id_status"] = False
          with open(f"students/{a}.txt","w") as x:
               x.write(str(val))
          print("Your id is blocked.")

      
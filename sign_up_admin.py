import os
import re
import maskpass

flag = 0
def admin():
     while(True):
          admin_id = input("Enter your ADMIN_id: ")


          if os.path.isfile(f"admin/{admin_id}.txt") == True:
               print("This admin_Id is already exits.\n Input another User_Id")
               print("Enter the Admin_id again.")
          else:
               break


     while(True):
          password = maskpass.askpass("Enter the password: " ,mask="*")
          if(len(password) <= 8):
               print("The password is not valid.")
               break
          elif not re.search("[a-z]",password):
               flag = -1
               break
          elif not re.search("[A-Z]",password):
               flag = -1
               break
          elif not re.search("[0-9]",password):
               flag = -1
               break
          elif not re.search("[a-zA-Z0-9_@!#$%^*]",password):
               print("The password is not valid.")
               break
          else:
               break
          

     password1 = maskpass.askpass("Enter the password again: ",mask="*")

     if password == password1:

          admin_id_status = True
     
          print("Thank You.")
          print("Your id is created.")

          with open(f"admin/{admin_id}.txt",'w')as f2:
               f2.write('{'f"'admin_id': '{admin_id}',")
               f2.write(f"'password': '{password}',")
               f2.write(f"'admin_id_status': {admin_id_status},"'}')

     else:
          # passwords not matching
          print("Password not matching.")

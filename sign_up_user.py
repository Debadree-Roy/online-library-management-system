import os
import re
import maskpass

flag = 0
def signuser():
     while(True):
          user_id = input("Enter your User_id: ")
     # a = os.path.isfile(f"students/{user_id}.txt")

          if os.path.isfile(f"students/{user_id}.txt") == True:
               print("This User_Id is already exits.\n Input another User_Id")
               print("Enter the User_id again.")
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
          

     password1 = maskpass.askpass("Enter the password again: " ,mask="*")

     if password == password1:
          name = input("Enter your Name: ")
          roll = input("Enter your Roll: ")
          sec = input("Enter your Sec: ")
          clss = input("Enter your Class: ")
          id_status = True
          borrowed_books = []
     
          print("Thank You.")
          print("Your id is created.")

          with open(f"students/{user_id}.txt",'w')as f2:
               f2.write('{'f"'user_id': '{user_id}',")
               f2.write(f"'password': '{password}',")
               f2.write(f"'name': '{name}',")
               f2.write(f"'roll': '{roll}',")
               f2.write(f"'sec': '{sec}',")
               f2.write(f"'clss': '{clss}',")
               f2.write(f"'id_status': '{id_status}',")
               f2.write(f"'borrowed_books': {borrowed_books}"'}')
     else:
          # passwords not matching
          print("Password not matching.")

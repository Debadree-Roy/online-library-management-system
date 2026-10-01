import os
import time
from sign_up_user import signuser
from sign_up_admin import admin
from log_in_user import login
from log_in_admin import admin_login


def user():
          while(True):
               print("Welcome")
               print("Press 1 to login this lib.")
               print("Press 2 to Sign Up.")
               print("Press 3 to exit.")

               a = int(input("Enter your Choice: "))

               if a == 1:
                    login()  
                    # pass
               elif a==2:
                    signuser()
                    pass
               elif a==3:
                    break
               else:
                    print("Invalid Choice. Enter your choice again.....")
                    time.sleep(1)
                    os.system("clear")


print("Welcome Sir/Madam")
print("press 1 to Enter ADMIN login")
print("press 2 to Enter USER login")

a = int(input("Enter your choice: "))

if a == 1:

     while(True):
               print("Welcome to admin menu")
               print("Press 1 to login admin.")
               print("Press 2 to Sign Up.")
               print("Press 3 to exit.")

               a = int(input("Enter your Choice: "))

               if a == 1:
                    admin_login()
               elif a==2:
                    admin()
               elif a==3:
                    break
               else:
                    print("Invalid Choice. Enter your choice again.....")
                    time.sleep(1)
                    os.system("clear")

elif a == 2:
     user()

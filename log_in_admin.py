import maskpass

def admin_login():
     count = 0
     while count < 3:
          a = input("Enter ADMIN ID: ")
          b = maskpass.askpass("Enter ADMIN password: ",mask="*")

          with open(f"admin/{a}.txt",'r') as f:
               val = eval(f.read())
               p = val['password']
               q = val['admin_id_status']

          if b == p :
               if q == False:
                    print("your admin potral is blocked.")
               else:
                    print("welcome to the admin page")
                    print(" ")
               # gjbhjgyfy
                    print("Enter 1 to change the password: ")
                    print("Enter 2 to add book in library: ")
                    print("Enter 3 to Edit the quantity of a book: ")
                    print("Enter 4 to delete a Book: ")

                    e = int(input("Enter your choice: "))

                    if e == 1:
                         p1 = maskpass.askpass("Enter the old password: " ,mask="*") 
                         if p == p1:
                              p2 = maskpass.askpass("Enter the new password: ", mask="*") 
                              p3 = maskpass.askpass("Enter the new password again: " , mask="*") 
                              if p2 == p3 and p1 != p2:
                                   with open(f"admin/{a}.txt",'w') as f:
                                        val['password'] = p2
                                        f.write(str(val))
                              elif p2 != p3:
                                   print("Passwords don't match.")
                              elif p1 == p2:
                                   print("New password can't be same as old password.")
                         else:
                              print('Old password is wrong!')

                    elif e == 2:
                         book_name = input("Enter the Name of Book: ")
                         topic = input("Enter the topic of book: ")
                         quantity = input("Enter book quantity: ")

                         with open(f"books.txt",'r')as f2:
                              val = eval(f2.read())

                         val[book_name] = {'quantity': quantity,'topic': topic}

                         with open(f"books.txt",'w')as f2:
                              f2.write(str(val))



                    elif e == 3:

                         # Edit the quantity of a book
                         # j = input("Enter the book name you want to set the quantity: ")
                         # with open(f"books.txt",'r') as f1:
                         #      val1 = eval(f1.read())
                         #      with open(f"books.txt",'w') as f1:
                         #           f1.write val1['book_name']['quantity']= j


                         book_name = input("Enter the book name you want to set the quantity: ")
                         new_quantity = input("Enter the new quantity value: ")

                         with open("books.txt", "r") as f:
                              books = eval(f.read())

                         if book_name in books:
                              books[book_name]["quantity"] = int(new_quantity)
                              with open("books.txt", "w") as f:
                                   f.write(str(books))
                                   print(f"Quantity of {book_name} set to {new_quantity}.")
                         else:
                              print(f"{book_name} not found in the list of books.")

                    elif e == 4:
                         h = input("Enter the book name you want to remove: ")
                         with open(f"books.txt",'r') as f1:
                              val1 = eval(f1.read())
                         
                         val1.pop(h)
                         with open(f"books.txt",'w') as f1:
                              f1.write(str(val1))


          else:
               count = count + 1
               print("enterd wrong Password.")
               print("Enter the password again.")

     if count == 3:
          val["admin_id_status"] = False
          with open(f"{a}.txt","w") as f:
               f.write(str(val))
          print("Your admin id is blocked.")
def mainmenu(user_id):
     while(True):
          print('''Welcome to login menu.''')
          print("Press 1 to Borrow Book")
          print("Press 2 to Return Book")
          print("Press 3 to show available Books")
          print("Press 4 to Back to main menu")

          a = int(input("Enter your choice: "))

          if a == 1:
               with open(f"students/{user_id}.txt",'r') as f:
                         val = eval(f.read())
                         books = val["borrowed_books"]

               book_count = len(val['borrowed_books'])
               
               if book_count >= 3:
                    print("You can't take more than three books.")
               else:
                    book_name = input("select book: ")
                    with open(f"books.txt",'r') as f1:
                         val1 = eval(f1.read())
                         # books = val["borrowed_books"]
                         # print(val1[book_name]["quantity"])
                    
                    for book_name in val1: 
                         # my_dict['Data structure using C']['quantity']
                         p = int(val1[book_name]['quantity'])


                         if p != 0:
                              print("This Book is available in library.")
                              print("press 1 to borrow the book.")
                              print("press 2 to exit.")
                              h = int(input("Enter your choice: "))
                              if h == 1:
                                   with open(f"students/{user_id}.txt",'r') as f:
                                        val = eval(f.read())
                                        # with open(f"students/{user_id}.txt",'w') as f:
                                        #      val["borrowed_books"] = book_name

                                        #      f.write(val["borrowed_books"].append(book_name))
                                        #      # my_dict['borrowed_books'].append(book_name)
                                        #      print(val['borrowed_books'])
                                        #      # f.write(f"'borrowed_books': '{book_name}'")
                                        #           # books.append(book_name)

                                   with open(f"students/{user_id}.txt", 'w') as f:
                                        books.append(book_name)
                                        val["borrowed_books"] = books
                                        f.write(str(val))
          
                                   p = p - 1
                                   val1[book_name]['quantity'] = p
                                   print(p)
                                        # with open(f"books.txt",'r') as f1:
                                        #      val1 = eval(f1.read())
                                             # val1[book_name]['quantity'] = val1[book_name]['quantity']-1
                                   with open(f"books.txt",'r') as f1:
                                        val2 = eval(f1.read())
                                   with open(f"books.txt",'w') as f1:
                                        val2[book_name]['quantity'] = p
                                        f1.write(str(val2))

                                             # val["borrowed_books"] = books

                                        # with open(f"students/{user_id}.txt",'w') as f:
                                        #      f.write(str(val))
                                        #      print(val['borrowed_books'])



                                        book_count = book_count + 1
                                   print("you Borrow this this Book")
                                   break
                                        
                              else:
                                   break

          elif a == 2:
               with open(f"students/{user_id}.txt",'r') as f:
                         val = eval(f.read())
                         # books = val["borrowed_books"]
                         print("you have this books: ")
                         print(val["borrowed_books"])
                         return_book = input("Enter the Book name you want to Return : ")
                         
                         with open(f"students/{user_id}.txt",'r') as f:
                              val = eval(f.read())

                         with open(f"students/{user_id}.txt",'w') as f:
                              # f.write(str(val))
                              # user_info['borrowed_books'].remove('Let us C')
                              val['borrowed_books'].remove(return_book)
                              # val["borrowed_books"] = books
                              f.write(str(val))

                         with open(f"books.txt",'r') as f1:
                              val1 = eval(f1.read())
                         if return_book in val1:
                              val1[return_book]["quantity"] += 1
                              print(val1)

                         with open(f"books.txt",'w') as f1:
                              # val1[return_book]["quantity"] += 1
                              f1.write(str(val1))
                              # val["borrowed_books"] = books

          elif a == 3:
               print("This books are available: ")
               with open(f"books.txt",'r') as f1:
                    val1 = eval(f1.read())
                    for book_name in val1:
                         print(book_name)

          elif a == 4:
               return

          else:
               print("Invalid Choice. Enter your choice again.....")
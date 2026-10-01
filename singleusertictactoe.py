import random 

def win_combination(board, players, current_player):
     for i in range (3):
          if board[i][0] == players[current_player] and board[i][1] == players[current_player] and board[i][2] == players[current_player]:
               print(players[current_player], "win")
               return True
          if board[0][i] == players[current_player] and board[1][i] == players[current_player] and board[2][i] == players[current_player]:
               print(players[current_player], "win")
               return True
          
          if board[0][0] == players[current_player] and board[1][1] == players[current_player] and board[2][2] == players[current_player]:
               print(players[current_player], "win")
               return True
          if board[2][0] == players[current_player] and board[1][1] == players[current_player] and board[0][2] == players[current_player]:
               print(players[current_player], "win")
               return True

print("welcome to tic tac toe game.")

board = [[" "," "," "] for _ in range(3)]
players = ["*","O"]
current_player = 0
a = input("Enter the symbol user want to play with(*/O): ")
while(True):
     rows = len(board)
     cols = len(board)
     
     for i in range(rows):
          for j in range(rows):
               print(board[i][0], " |", board[i][1], "|", board[i][2])
               break
          if i != 2:
               print("---+---+---")

     b = random.randint(1, 3)
     c = random.randint(1, 3)

     if players[current_player] == a:
          row = int(input("players " + players[current_player] + ", enter row (1-3) : ")) -1
          column = int(input("players " + players[current_player] + ", enter column (1-3) : ")) -1 
     # print("Enter your choice : ")
     # a = input("players " + players[current_player] + ", enter your choice : ")
     else:
          row = b-1
          column = c-1

     if board[row][column] != " ":
          print("The box is already filled, ")
          print("Try Again")
     else:
          board[row][column] = players[current_player]
          
          if win_combination(board, players, current_player):
               print("Game over!")
               break
          else:
               print("Continue playing...")
          

          for row in board:
               if " " in row:
                    break
               elif row != " " and column != " ":
                    print("Its tie.")
                    break

          
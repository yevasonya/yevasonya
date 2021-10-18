
         
       
board=[[' ',' ',' ',],[' ',' ',' '],[' ',' ',' ']]

def printboard():
        for i in range(3):
         print()
         print(board[i])

def wincondition(board):
        if board[0][0]==board[0][1]==board[0][2]=='X' or board[1][0]==board[1][1]==board[1][2]=='X' \
        or board[2][0]==board[2][1]==board[2][2]=='X' or board[0][0]==board[1][0]==board[2][0]=='X' \
        or board[0][1]==board[1][1]==board[2][1]=='X' or board[0][2]==board[1][2]==board[2][2]=='X' \
        or board[0][0]==board[1][1]==board[2][2]=='X' or board[2][0]==board[1][1]==board[0][2]=='X':
                print('player 1 wins')
                return True
        if board[0][0]==board[0][1]==board[0][2]=='O' or board[1][0]==board[1][1]==board[1][2]=='O' or board[2][0]==board[2][1]==board[2][2]=='O' or board[0][0]==board[1][0]==board[2][0]=='O' or board[0][1]==board[1][1]==board[2][1]=='O' or board[0][2]==board[1][2]==board[2][2]=='O' or board[0][0]==board[1][1]==board[2][2]=='O' or board[2][0]==board[1][1]==board[0][2]=='O':
                print('player 2 wins')
                return True
        return False      


for j in range(9):
  if j%2==0: 
   print('player 1')
   turn='X'
  else:    
   print('player 2')
   turn='O'

  while True:
   n = (input(''))
   if n not in ["1","2","3","4","5","6","7","8","9"]:
    print('Invalid input!')
   else:
           
    n= int(n)
    m = int((n-1)/3)
    p = int((n-1)%3)
    if board[m][p] == "X" or board[m][p] == "O":
     print("You can't go there. Try again")
    else:
     board[m][p] =turn
     break
  

  printboard()
  print
  if wincondition(board):
          wincondition(board)
          break
      

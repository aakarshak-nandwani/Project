board = {"7":" ","8":" ","9":" ",
         "4":" ","5":" ","6":" ",
         "1":" ","2":" ","3":" "}

board_keys = []

for key in board:
    board_keys.append(key)

def printBoard(board):
    print(board["7"] +"|" + board["8"]+"|"+ board["9"])
    print("-+-+-")
    print(board["4"] +"|" + board["5"]+"|"+ board["6"])
    print("-+-+-")
    print(board["1"] +"|" + board["2"]+"|"+ board["3"])

def game():

    turn = "X"
    count = 0 

    for i in range(10):
        printBoard(board)
        print("Its your Turn "+ turn +".Move to which place?")

        move = input()

        if board[move]==" ":
            board[move] = turn
            count+=1
        else:
            print("The place is already filled.\n Move to which place?")
            continue  

        if count>=5:

            if board['7']==board["8"]==board["9"]!=" ":
                printBoard(board)
                print("game over")
                print("Winner is: "+ turn)
                break 

            elif board['4']==board["5"]==board["6"]!=" ":
                printBoard(board)
                print("game over")
                print("Winner is: "+ turn)
                break 

            elif board['1']==board["2"]==board["3"]!=" ":
                printBoard(board)
                print("game over")
                print("Winner is: "+ turn)
                break 

            elif board['1']==board["5"]==board["9"]!=" ":
                printBoard(board)
                print("game over")
                print("Winner is: "+ turn)
                break 

            elif board['7']==board["5"]==board["3"]!=" ":
                printBoard(board)
                print("game over")
                print("Winner is: "+ turn)
                break 
            
            elif board['7']==board["4"]==board["1"]!=" ":
                printBoard(board)
                print("game over")
                print("Winner is: "+ turn)
                break 

            elif board['8']==board["5"]==board["2"]!=" ":
                printBoard(board)
                print("game over")
                print("Winner is: "+ turn)
                break

            elif board['9']==board["6"]==board["3"]!=" ":
                printBoard(board)
                print("game over")
                print("Winner is: "+ turn)
                break 

        if count == 9:
            print("game over")
            print("Its a tie!!")

        if turn == "X":
            turn = "O"
        
        else:
            turn = "X"



    restart = input("Do you want to play again?(y/n)")

    if restart == "y" or restart == "Y":
        for key in board_keys:
            board[key]=" "

        game()

    
if __name__ == "__main__":
    game()
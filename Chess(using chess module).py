import chess 

#create a board
board=chess.Board()

#Function to Draw the board with markings with their Addresses
def DrawBoard(Pboard):
    board=str(Pboard)
    lines=board.split('\n')
    for i in range(len(lines)):
        print(f"\033[1m{str(8-i)}\033[0m",end="  ")
        print(lines[i])
    print('\033[1m\n   a b c d e f g h\033[0m')

####Game Start####
#printing the Instructions
print("""Game Instructions:
R/r-Rook
N/n-Knight
B/b-Bishop
Q/q-Queen
K/k-King
P/p-Pawn
Upper Case Characters Represent White Player 
Lower Case Characters Represent Black Player""")

#printing the board at the start of the game
DrawBoard(board)

#Tracking the player's Turn
whiteMove=True

#Game Loop
while not board.outcome():#Keep Game running till a checkmate/stalemate/draw

    #asking for input from the player according the players turn
    if whiteMove:
        print('White to move,Enter your move in uci format')
    else:
        print('Black to Move,Enter your move in uci format')

    #Keep inputting moves till a legal move is acquired
    while True:
        userMove=input().strip()
        try:
            move=chess.Move.from_uci(userMove)
            if move in board.legal_moves:
                board.push(move)
                break
            else:
                print('Invalid Move')
        except Exception as err:
            print('Error, please Enter again:',err)
            continue
    
    #Draw the updated board
    DrawBoard(board)

    #Check if the game has ended
    outcome=board.outcome()
    if outcome:
        if outcome.winner ==True:
            print('White Wins')
        elif outcome.winner==False:
            print('Black Wins')
        else:
            print('The Match Ended in a draw'.center(20))
        print(f"due to {outcome.termination}".center(20))
        print(board)
        break

    
    #check if a player is checked
    if board.is_check():
        print('Black is Checked')if whiteMove else print('White is Checked')

    #toggling the player's Turn 
    whiteMove=not whiteMove
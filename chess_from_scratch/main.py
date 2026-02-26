from Helper import *
import copy
from makeMove import *
from printBoard import *
from generateAllLegalMoves import *
from isValidNotation import *

StartingBoard = [
        ['r' , 'n' , 'b' , 'q' , 'k' , 'b' , 'n' , 'r'],#0 #8
        ['p' , 'p' , 'p' , 'p' , 'p' , 'p' , 'p' , 'p'],#1 #7
        ['.' , '.' , '.' , '.' , '.' , '.' , '.' , '.'],#2 #6
        ['.' , '.' , '.' , '.' , '.' , '.' , '.' , '.'],#3 #5
        ['.' , '.' , '.' , '.' , '.' , '.' , '.' , '.'],#4 #4
        ['.' , '.' , '.' , '.' , '.' , '.' , '.' , '.'],#5 #3
        ['P' , 'P' , 'P' , 'P' , 'P' , 'P' , 'P' , 'P'],#6 #2
        ['R' , 'N' , 'B' , 'Q' , 'K' , 'B' , 'N' , 'R'] #7 #1
    ]    #0     1     2     3     4     5     6     7
         #a     b     c     d     e     f     g     h


gameBoard = copy.deepcopy(StartingBoard)
movesHistory = []
currentTurn = TURN.WHITE

while(True):

    legalMoves = generateAllLegalMoves(gameBoard , currentTurn , movesHistory)
    if len(legalMoves) == 0:
        if currentTurn == TURN.WHITE:
            print("Black checkmates White, Black wins")
        elif currentTurn == TURN.BLACK:
            print("White checkmates Black, White wins")

        restartFlag = input("Do you want to restart the game?(Y/N)")
        if restartFlag.lower() == 'y':
            movesHistory = []
            gameBoard = copy.deepcopy(StartingBoard)
            currentTurn = TURN.WHITE
        elif restartFlag.lower() == 'n':
            break

    printBoard(gameBoard)
    if currentTurn == TURN.WHITE:
        print("White Player's turn")
    elif currentTurn == TURN.BLACK:
        print("Black Player's turn")

    move = input("Enter your move:")
    if not isValidNotation(move):
        print("The Inputted move is does not follow the notation, please enter the move again")
        continue

    if move not in legalMoves:
        print("Not a Legal Move, please enter a legal move")
        continue
    else:
        gameBoard = makeMove(gameBoard , move)
        currentTurn = TURN.BLACK if currentTurn == TURN.WHITE else TURN.WHITE
        movesHistory.append(move)


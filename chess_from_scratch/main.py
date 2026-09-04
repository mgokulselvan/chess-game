from Helper import *
import copy
from makeMove import *
from printBoard import *
from moves.generateAllLegalMoves import *
from isValidNotation import *
from Notations import *
from isSquareChecked import isKingInCheck

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

StartingCastlingRights = {
    "white-kingside":True,
    "white-queenside":True,
    "black-kingside":True,
    "black-queenside":True
}

enPassantTarget=None
halfmoveClock = 0
gameBoard = copy.deepcopy(StartingBoard)
movesHistory = []
currentTurn = TURN.WHITE
castlingRights = copy.deepcopy(StartingCastlingRights)


initialGameState= makeGameStateKey(gameBoard,currentTurn,castlingRights,None)

#to keep track of number of times the current state of game has been reached, (threefold htingy)
gameStateCounts = {initialGameState: 1}

instructions="""
CHESS CLI - INSTRUCTIONS

Move format:
- Use: e2e4 (source → destination)
- Example: g1f3, e7e5

Rules:
- Only legal moves allowed
- Game ends on checkmate or draw

Controls:
- Ctrl+C to exit

"""""
print(instructions)

try:
    while(True):

        legalMoves = generateAllLegalMoves(gameBoard , currentTurn , movesHistory,castlingRights)
        if len(legalMoves) == 0:
            if isKingInCheck(gameBoard, currentTurn, movesHistory):
                if currentTurn == TURN.WHITE:
                    print("Black checkmates White, Black wins")
                elif currentTurn == TURN.BLACK:
                    print("White checkmates Black, White wins")
            else:
                print("Stalemate, the game is a draw")

            restartFlag = input("Do you want to restart the game?(Y/N)")
            if restartFlag.lower() == 'y':
                halfmoveClock=0
                movesHistory = []
                gameBoard = copy.deepcopy(StartingBoard)
                currentTurn = TURN.WHITE
                castlingRights = copy.deepcopy(StartingCastlingRights)
                gameStateCounts = {initialGameState: 1}
                enPassantTarget=None
                continue
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

            #Check if Castling done
            currentMoveCoords=moves(move)

            if(currentMoveCoords[1]==(0,0)):castlingRights["black-queenside"]=False;
            if(currentMoveCoords[1]==(0,7)):castlingRights["black-kingside"]=False;
            if(currentMoveCoords[1]==(7,0)):castlingRights["white-queenside"]=False;
            if(currentMoveCoords[1]==(7,7)):castlingRights["white-kingside"]=False;

            if(currentTurn==TURN.BLACK):

                if currentMoveCoords[0]==(0,4):#if source is king
                    castlingRights["black-kingside"]=False;
                    castlingRights["black-queenside"]=False;
                elif currentMoveCoords[0]==(0,7):#source is black rook(king side)
                    castlingRights["black-kingside"]=False;
                elif currentMoveCoords[0]==(0,0):#source is black rook(queenside side)
                    castlingRights["black-queenside"]=False;

                currentTurn=TURN.WHITE
            else:

                if currentMoveCoords[0]==(7,4):#if source is king
                    castlingRights["white-kingside"]=False;
                    castlingRights["white-queenside"]=False;
                elif currentMoveCoords[0]==(7,7):#source is black rook(king side)
                    castlingRights["white-kingside"]=False;
                elif currentMoveCoords[0]==(7,0):#source is black rook(queenside side)
                    castlingRights["white-queenside"]=False;

                currentTurn=TURN.BLACK

            if moveClockReset(gameBoard, move,enPassantTarget):
                halfmoveClock=0
            else:
                halfmoveClock+=1


            gameBoard = makeMove(gameBoard , move)

            movesHistory.append(move)

            #checking for trifold repetition
            enPassantTarget=getEnPassantTarget(gameBoard,movesHistory)
            currentGameState = makeGameStateKey(gameBoard,currentTurn,castlingRights,enPassantTarget)
            gameStateCounts[currentGameState] = gameStateCounts.get(currentGameState,0)+1
            if gameStateCounts.get(currentGameState,0)>=3:
                print("TriFold Repetition, the game is a draw")

                restartFlag = input("Do you want to restart the game?(Y/N)")
                if restartFlag.lower() == 'y':
                    halfmoveClock=0
                    movesHistory = []
                    gameBoard = copy.deepcopy(StartingBoard)
                    currentTurn = TURN.WHITE
                    castlingRights = copy.deepcopy(StartingCastlingRights)
                    gameStateCounts = {initialGameState: 1}
                    enPassantTarget=None
                    continue
                elif restartFlag.lower() == 'n':
                    break
            
            #checking for 50-move draw condition ,update: 50 move draw is optional , so not enforcing it as an auto draw
            #75 auto draw
            if halfmoveClock >= 150:
                print("The game is a draw\nReason:75 move Draw")

                restartFlag = input("Do you want to restart the game?(Y/N)")
                if restartFlag.lower() == 'y':
                    halfmoveClock=0
                    movesHistory = []
                    gameBoard = copy.deepcopy(StartingBoard)
                    currentTurn = TURN.WHITE
                    castlingRights = copy.deepcopy(StartingCastlingRights)
                    gameStateCounts = {initialGameState: 1}
                    enPassantTarget=None
                    continue
                elif restartFlag.lower() == 'n':
                    break




except KeyboardInterrupt:
    print("\nGame Exiting...")

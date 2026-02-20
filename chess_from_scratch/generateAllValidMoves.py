from Helper import *
from generateKingMoves import *
from generateQueenMoves import *
from generateBishopMoves import *
from generateKnightMoves import *
from generateRookMoves import *
from generatePawnMoves import *

def generateAllValidMoves(board,turn,history):

    #List to gather all the moves based on the current state of the game
    moves=[]

    for rowNo in range(8):
        for columnNo in range(8):
            
            #calculating the moves only for the current player
            if board[rowNo][columnNo].isupper():
               if turn!=TURN.WHITE:
                continue
            else:
               if turn!=TURN.BLACK:
                continue

            match(board[rowNo][columnNo].lower()):
                case 'p':#calculating moves for a pawn
                    moves.extend(generatePawnMoves(board,rowNo,columnNo,turn,history))
                case 'r':#calculating moves for a rook
                    moves.extend(generateRookMoves(board,rowNo,columnNo,turn))
                case 'n':#calculating moves for a knight
                    moves.extend(generateKnightMoves(board,rowNo,columnNo,turn))
                case 'b':#calculating moves for a bishop
                    moves.extend(generateBishopMoves(board,rowNo,columnNo,turn))
                case 'q':#calculating moves for a queen
                    moves.extend(generateQueenMoves(board,rowNo,columnNo,turn))
                case 'k':#calculating moves for a king
                    moves.extend(generateKingMoves(board,rowNo,columnNo,turn))

    return moves



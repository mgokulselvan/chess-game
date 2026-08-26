from Helper import *
from moves.generateKingMoves import *
from moves.generateQueenMoves import *
from moves.generateBishopMoves import *
from moves.generateKnightMoves import *
from moves.generateRookMoves import *
from moves.generatePawnMoves import *
from moves.generateCastlingMoves import *

def generateAllPseudoMoves(board,turn,history,castlingRights):

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
    
    moves.extend(generateCastlingMoves(board,turn,castlingRights,history)) 

    return moves



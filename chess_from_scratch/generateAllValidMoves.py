from Helper import *

def generateAllValidMoves(board,turn):

    #List to gather all the moves based on the current state of the game
    moves=[]

    for rowNo in range(8):
        for columnNo in range(8):
            
            #calculating the moves only for the current player
            if board[rowNo][columnNo].isupper():
               if turn!=Turn.WHITE:
                continue
            else:
               if turn!=Turn.BLACK:
                continue

            match(board[rowNo][columnNo].lower()):
                case 'p':#calculating moves for a pawn
                    moves.append(generatePawnMoves(board,rowNo,columnNo,turn))
                case 'r':#calculating moves for a rook
                    moves.append(generateRookMoves(board,rowNo,columnNo,turn))
                case 'n':#calculating moves for a knight
                    moves.append(generateKnightMoves(board,rowNo,columnNo,turn))
                case 'b':#calculating moves for a bishop
                    moves.append(generateBishopMoves(board,rowNo,columnNo,turn))
                case 'q':#calculating moves for a queen
                    moves.append(generateQueenMoves(board,rowNo,columnNo,turn))
                case 'k':#calculating moves for a king
                    moves.append(generateKingMoves(board,rowNo,columnNo,turn))

    return moves



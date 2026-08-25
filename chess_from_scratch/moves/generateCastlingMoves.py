from Helper import *
from Notations import *
from isSquareChecked import *

#TODO: KING and the places swapping through must not be under check DONE

def generateCastlingMoves(board,turn,castlingRights,history):
    moves=[]
    if turn==TURN.WHITE:
        if castlingRights["white-kingside"]:
            #if between them is empty, 
            if board[7][5]=='.' and board[7][6]=='.':
                if isSquareChecked(board,4,7,turn,history) or isSquareChecked(board,5,7,turn,history) or isSquareChecked(board,6,7,turn,history):
                    pass
                else:
                    moves.append(Notation([(7,4),(7,6)]));
        if castlingRights["white-queenside"]:
            #if between them is empty, 
            if board[7][1]=='.' and board[7][2]=='.' and board[7][3]=='.':
                if isSquareChecked(board,4,7,turn,history) or isSquareChecked(board,3,7,turn,history) or isSquareChecked(board,2,7,turn,history):
                    pass
                else:
                    moves.append(Notation([(7,4),(7,2)]));
    else:
        if castlingRights["black-kingside"]:
            #if between them is empty, 
            if board[0][5]=='.' and board[0][6]=='.':
                if isSquareChecked(board,4,0,turn,history) or isSquareChecked(board,5,0,turn,history) or isSquareChecked(board,6,0,turn,history):
                    pass
                else:
                    moves.append(Notation([(0,4),(0,6)]));
        if castlingRights["black-queenside"]:
            #if between them is empty, 
            if board[0][1]=='.' and board[0][2]=='.' and board[0][3]=='.':
                if isSquareChecked(board,4,0,turn,history) or isSquareChecked(board,3,0,turn,history) or isSquareChecked(board,2,0,turn,history):
                    pass
                else:
                    moves.append(Notation([(0,4),(0,2)]));

    return moves

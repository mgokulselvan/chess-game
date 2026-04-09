import copy
from Notations import *

def makeMove(board, move):
    Move = moves(move)
    (srcRow,srcColumn)=Move[0]
    (destRow,destColumn)=Move[1]
    newBoard=copy.deepcopy(board)
    #CASTLING
    #WHITE KING SIDE
    if srcRow==7 and srcColumn==4 and destRow==7 and destColumn==6 and board[srcRow][srcColumn]=='K':
        newBoard[destRow][destColumn] = board[srcRow][srcColumn]
        newBoard[srcRow][srcColumn] = '.'
        newBoard[7][7] = '.'
        newBoard[7][5] = 'R'
    #WHITE QUEEN SIDE
    elif srcRow==7 and srcColumn==4 and destRow==7 and destColumn==2 and board[srcRow][srcColumn]=='K':
        newBoard[destRow][destColumn] = board[srcRow][srcColumn]
        newBoard[srcRow][srcColumn] = '.'
        newBoard[7][0] = '.'
        newBoard[7][3] = 'R'
    #BLACK KING SIDE
    elif srcRow==0 and srcColumn==4 and destRow==0 and destColumn==6 and board[srcRow][srcColumn]=='k':
        newBoard[destRow][destColumn] = board[srcRow][srcColumn]
        newBoard[srcRow][srcColumn] = '.'
        newBoard[0][7] = '.'
        newBoard[0][5] = 'r'
    #BLACK QUEEN SIDE
    elif srcRow==0 and srcColumn==4 and destRow==0 and destColumn==2 and board[srcRow][srcColumn]=='k':
        newBoard[destRow][destColumn] = board[srcRow][srcColumn]
        newBoard[srcRow][srcColumn] = '.'
        newBoard[0][0] = '.'
        newBoard[0][3] = 'r'

    #EN-PASSANT
    elif board[srcRow][srcColumn]=='p' and destRow==srcRow+1 and destColumn==srcColumn+1 and board[destRow][destColumn]=='.':
        newBoard[destRow][destColumn]=board[srcRow][srcColumn]
        newBoard[srcRow][srcColumn]='.'
        newBoard[srcRow][srcColumn+1]='.'

    elif board[srcRow][srcColumn]=='p' and destRow==srcRow+1 and destColumn==srcColumn-1 and board[destRow][destColumn]=='.':
        newBoard[destRow][destColumn]=board[srcRow][srcColumn]
        newBoard[srcRow][srcColumn]='.'
        newBoard[srcRow][srcColumn-1]='.'

    elif board[srcRow][srcColumn]=='P' and destRow==srcRow-1 and destColumn==srcColumn+1 and board[destRow][destColumn]=='.':
        newBoard[destRow][destColumn]=board[srcRow][srcColumn]
        newBoard[srcRow][srcColumn]='.'
        newBoard[srcRow][srcColumn+1]='.'


    elif board[srcRow][srcColumn]=='P' and destRow==srcRow-1 and destColumn==srcColumn-1 and board[destRow][destColumn]=='.':
        newBoard[destRow][destColumn]=board[srcRow][srcColumn]
        newBoard[srcRow][srcColumn]='.'
        newBoard[srcRow][srcColumn-1]='.'


    else:
        newBoard[destRow][destColumn] = board[srcRow][srcColumn]
        newBoard[srcRow][srcColumn] = '.'
        if len(Move) == 3:
            newBoard[destRow][destColumn] = Move[2]

    return newBoard

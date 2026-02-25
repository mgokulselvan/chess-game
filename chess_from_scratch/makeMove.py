import copy
from Notations import *

def makeMove(board, move):
    Move = moves(move)
    (srcRow,srcColumn)=Move[0]
    (destRow,destColumn)=Move[1]
    newBoard=copy.deepcopy(board)
    newBoard[destRow][destColumn] = board[srcRow][srcColumn]
    newBoard[srcRow][srcColumn] = '.'
    if len(Move) == 3:
        newBoard[destRow][destColumn] = Move[2]

    return newBoard

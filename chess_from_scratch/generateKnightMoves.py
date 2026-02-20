from Helper import *
from Notations import *

def generateKnightMoves(board,rowNo,columnNo,turn):
    moves=[]
    try:
        if board[rowNo-2][columnNo-1]=='.' or is_enemy(board[rowNo-2][columnNo-1],turn):
            if rowNo-2>-1 and columnNo-1>-1:
                moves.append(Notation([(rowNo,columnNo),(rowNo-2,columnNo-1)]))
    except IndexError:
        pass
    try:
        if board[rowNo-2][columnNo+1]=='.' or is_enemy(board[rowNo-2][columnNo+1],turn):
            if rowNo-2>-1:
                moves.append(Notation([(rowNo,columnNo),(rowNo-2,columnNo+1)]))
    except IndexError:
        pass
    try:
        if board[rowNo+2][columnNo-1]=='.' or is_enemy(board[rowNo+2][columnNo-1],turn):
            if columnNo-1>-1:
                moves.append(Notation([(rowNo,columnNo),(rowNo+2,columnNo-1)]))
    except IndexError:
        pass
    try:
        if board[rowNo+2][columnNo+1]=='.' or is_enemy(board[rowNo+2][columnNo+1],turn):
                moves.append(Notation([(rowNo,columnNo),(rowNo+2,columnNo+1)]))
    except IndexError:
        pass
    try:
        if board[rowNo-1][columnNo+2]=='.' or is_enemy(board[rowNo-1][columnNo+2],turn): 
            if rowNo-1>-1:
                moves.append(Notation([(rowNo,columnNo),(rowNo-1,columnNo+2)]))
    except IndexError:
        pass
    try:
        if board[rowNo+1][columnNo+2]=='.' or is_enemy(board[rowNo+1][columnNo+2],turn): 
                moves.append(Notation([(rowNo,columnNo),(rowNo+1,columnNo+2)]))
    except IndexError:
        pass
    try:
        if board[rowNo-1][columnNo-2]=='.' or is_enemy(board[rowNo-1][columnNo-2],turn): 
            if rowNo-1>-1 and columnNo-2>-1:
                moves.append(Notation([(rowNo,columnNo),(rowNo-1,columnNo-2)]))
    except IndexError:
        pass
    try:
        if board[rowNo+1][columnNo-2]=='.' or is_enemy(board[rowNo+1][columnNo-2],turn) :
            if columnNo-2>-1:
                moves.append(Notation([(rowNo,columnNo),(rowNo+1,columnNo-2)]))
    except IndexError:
        pass
    return moves

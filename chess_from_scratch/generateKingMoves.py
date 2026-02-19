from Helper import *
from Notations import *

def generateKingMoves(board,rowNo,columnNo,turn):
    moves = []

    #CHECKING - TOP LEFT
    try:
        if board[rowNo-1][columnNo-1]=='.' or is_enemy(board[rowNo-1][columnNo-1],turn):
            if rowNo-1>-1 and columnNo-1>-1:
                moves.append(Notation([(rowNo,columnNo),(rowNo-1,columnNo-1)]))
    except IndexError:
        pass
    #CHECKING - DIRECT TOP 
    try:
        if board[rowNo-1][columnNo]=='.' or is_enemy(board[rowNo-1][columnNo],turn):
            if rowNo-1>-1:
                moves.append(Notation([(rowNo,columnNo),(rowNo,columnNo)]))
    except IndexError:
        pass
    #CHECKING - TOP RIGHT 
    try:
        if board[rowNo][columnNo+1]=='.' or is_enemy(board[rowNo-1][columnNo+1],turn):
            if rowNo>-1 and columnNo+1<8:
                moves.append(Notation([(rowNo,columnNo),(rowNo,columnNo+1)]))
    except IndexError:
        pass
    #CHECKING - DIRECT RIGHT 
    try:
        if board[rowNo][columnNo+2]=='.' or is_enemy(board[rowNo][columnNo+1],turn):
            if columnNo+2<8:
                moves.append(Notation([(rowNo,columnNo),(rowNo,columnNo+2)]))
    except IndexError:
        pass
    #CHECKING - BOTTOM RIGHT 
    try:
        if board[rowNo+2][columnNo+1]=='.' or is_enemy(board[rowNo+1][columnNo+1],turn):
            if rowNo+2<8 and columnNo+1<8:
                moves.append(Notation([(rowNo,columnNo),(rowNo+2,columnNo+1)]))
    except IndexError:
        pass
    #CHECKING - DIRECT BOTTOM 
    try:
        if board[rowNo+2][columnNo]=='.' or is_enemy(board[rowNo+1][columnNo],turn):
            if rowNo+2<8:
                moves.append(Notation([(rowNo,columnNo),(rowNo+2,columnNo)]))
    except IndexError:
        pass
    #CHECKING - BOTTOM LEFT
    try:
        if board[rowNo+2][columnNo-1]=='.' or is_enemy(board[rowNo+1][columnNo-1],turn):
            if columnNo>-1 and rowNo+1<8:
                moves.append(Notation([(rowNo,columnNo),(rowNo+2,columnNo-1)]))
    except IndexError:
        pass
    #CHECKING - DIRECT LEFT 
    try:
        if board[rowNo][columnNo]=='.' or is_enemy(board[rowNo][columnNo-1],turn):
            if columnNo>-1:
                moves.append(Notation([(rowNo,columnNo),(rowNo,columnNo)]))
    except IndexError:
        pass

    return moves

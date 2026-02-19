from Helper import *
from Notations import *

def generateRookMoves(board,rowNo,columnNo,turn):
    moves = []
    #CHECKING - ALL SQUARES FROM THE CURRENT ROOK POSITION TO THE TOP OF THE BOARD
    for hcoord in range(rowNo-1,-1,-1):
        if board[hcoord][columnNo]!='.':#if the box is NOT empty
            if not is_enemy(board[hcoord][columnNo],turn):#if it is not enemy piece, that move is not valid and hence break
                break
        moves.append(Notation([(rowNo,columnNo),(hcoord,columnNo)]))#adding the move
        if board[hcoord][columnNo]!='.' and is_enemy(board[hcoord][columnNo],turn):#if the destination of the added move was an enemy piece, the rook can't move any further, and hence thats the furthest end in that direction
            break

    #CHECKING - ALL SQUARES FROM THE CURRENT ROOK POSITION TO THE BOTTOM OF THE BOARD
    for hcoord in range(rowNo+1,8): 
        if board[hcoord][columnNo]!='.':
            if not is_enemy(board[hcoord][columnNo],turn):
                break
        moves.append(Notation([(rowNo,columnNo),(hcoord,columnNo)]))
        if board[hcoord][columnNo]!='.' and is_enemy(board[hcoord][columnNo],turn):
            break

    #CHECKING - ALL SQUARES FROM THE CURRENT ROOK POSITION TO THE LEFT OF THE BOARD
    for vcoord in range(columnNo-1,-1,-1):
        if board[rowNo][vcoord]!='.':
            if not is_enemy(board[rowNo][vcoord],turn):
                break
        moves.append(Notation([(rowNo,columnNo),(rowNo,vcoord)]))
        if board[rowNo][vcoord]!='.' and is_enemy(board[rowNo][vcoord],turn):
            break

    #CHECKING - ALL SQUARES FROM THE CURRENT ROOK POSITION TO THE RIGHT OF THE BOARD
    for vcoord in range(columnNo+1,8):
        if board[rowNo][vcoord]!='.':
            if not is_enemy(board[rowNo][vcoord],turn):
                break
        moves.append(Notation([(rowNo,columnNo),(rowNo,vcoord)]))
        if board[rowNo][vcoord]!=' ' and is_enemy(board[rowNo][vcoord],turn):
            break

    return moves 


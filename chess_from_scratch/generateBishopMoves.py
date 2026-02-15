from Helper import *

def generateBishopMoves(board,rowNo,columnNo,turn):
    moves = []
    #CHECKING - ALL SQUARES FROM THE CURRENT BISHOP POSITION TO THE TOP LEFT OF THE BOARD
    rcoord=rowNo-1
    vcoord=columnNo-1
    while rcoord > -1 and vcoord > -1:
        if board[rcoord][vcoord]!='.':#if the space is not empty on the board
            if not is_enemy(board[rcoord][vcoord],turn):#if the piece is not enemy, its an invalid move and it can't move there, hence break
                break
        moves.append(Notation([(rowNo,columnNo),(rcoord,vcoord)])#adding the valid move to the list
        if board[rcoord][vcoord]!='.' and is_enemy(board[rcoord][vcoord],turn): #if the desitnation of the added move was an enemy piece, thats the furthest extent the bishop can go in that direction
            break

        rcoord-=1
        vcoord-=1

    #CHECKING - ALL SQUARES FROM THE CURRENT BISHOP POSITION TO THE TOP RIGHT OF THE BOARD
    rcoord=rowNo-1
    vcoord=columnNo+1
    while rcoord> -1 and vcoord < 8:
        if board[rcoord][vcoord]!='.':
            if not is_enemy(board[rcoord][vcoord],turn):
                break
        moves.append(Notation([(rowNo,columnNo),(rcoord,vcoord)])
        if board[rcoord][vcoord]!='.' and is_enemy(board[rcoord][vcoord],turn): 
            break

        rcoord-=1
        vcoord+=1

    #CHECKING - ALL SQUARES FROM THE CURRENT BISHOP POSITION TO THE BOTTOM LEFT OF THE BOARD
    rcoord=rowNo+1
    vcoord=columnNo-1
    while rcoord> 8 and vcoord < -1:
        if board[rcoord][vcoord]!='.':
            if not is_enemy(board[rcoord][vcoord],turn):
                break
        moves.append(Notation([(rowNo,columnNo),(rcoord,vcoord)])
        if board[rcoord][vcoord]!='.' and is_enemy(board[rcoord][vcoord],turn): 
            break

        rcoord+=1
        vcoord-=1

    #CHECKING - ALL SQUARES FROM THE CURRENT BISHOP POSITION TO THE BOTTOM RIGHT OF THE BOARD
    rcoord=rowNo+1
    vcoord=columnNo+1
    while rcoord> 8 and vcoord < 8:
        if board[rcoord][vcoord]!='.':
            if not is_enemy(board[rcoord][vcoord],turn):
                break
        moves.append(Notation([(rowNo,columnNo),(rcoord,vcoord)])
        if board[rcoord][vcoord]!='.' and is_enemy(board[rcoord][vcoord],turn): 
            break

        rcoord+=1
        vcoord+=1

    return moves

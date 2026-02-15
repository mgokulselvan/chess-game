from Helper import *

def generateQueenMoves(board,rowNo,columnNo,turn):
    moves = []
    #CHECKING - ALL SQUARES FROM THE CURRENT QUEEN POSITION TO THE TOP OF THE BOARD
    #CHECKING - ALL SQUARES FROM THE CURRENT QUEEN POSITION TO THE BOTTOM OF THE BOARD
    #CHECKING - ALL SQUARES FROM THE CURRENT QUEEN POSITION TO THE LEFT OF THE BOARD
    #CHECKING - ALL SQUARES FROM THE CURRENT QUEEN POSITION TO THE RIGHT OF THE BOARD
    #CHECKING - ALL SQUARES FROM THE CURRENT QUEEN POSITION TO THE TOP LEFT OF THE BOARD
    #CHECKING - ALL SQUARES FROM THE CURRENT QUEEN POSITION TO THE TOP RIGHT OF THE BOARD
    #CHECKING - ALL SQUARES FROM THE CURRENT QUEEN POSITION TO THE BOTTOM LEFT OF THE BOARD
    #CHECKING - ALL SQUARES FROM THE CURRENT QUEEN POSITION TO THE BOTTOM RIGHT OF THE BOARD

                    if board[rowNo][columnNo]=='q':#checking if it is a black queen
                        #Adding Vertical and Horizontal Moves
                        for hcoord in range(rowNo+1,8): 
                            if board[hcoord][columnNo]!=' ':
                                if board[hcoord][columnNo].islower():
                                    break
                            moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+columnNo)}{8-hcoord}")
                            if board[hcoord][columnNo]!=' ':#if the added move had a destination of the opposite colour piece, then the path for the rook is blocked and it cant go further
                                if board[hcoord][columnNo].isupper():
                                    break
                        for hcoord in range(rowNo-1,-1,-1):
                            if board[hcoord][columnNo]!=' ':
                                if board[hcoord][columnNo].islower():
                                    break
                            moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+columnNo)}{8-hcoord}")
                            if board[hcoord][columnNo]!=' ':#if the added move had a destination of the opposite colour piece, then the path for the rook is blocked and it cant go further
                                if board[hcoord][columnNo].isupper():
                                    break
                        #calculating all the moves in horizontal line
                        for vcoord in range(columnNo+1,8):
                            if board[rowNo][vcoord]!=' ':
                                if board[rowNo][vcoord].islower():
                                    break
                            moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+vcoord)}{8-rowNo}")
                            if board[rowNo][vcoord]!=' ':#if the added move had a destination of the opposite colour piece, then the path for the rook is blocked and it cant go further
                                if board[rowNo][columnNo].isupper():
                                    break
                        for vcoord in range(columnNo-1,-1,-1):
                            if board[rowNo][vcoord]!=' ':
                                if board[rowNo][vcoord].islower():
                                    break
                            moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+vcoord)}{8-rowNo}")
                            if board[rowNo][vcoord]!=' ':#if the added move had a destination of the opposite colour piece, then the path for the rook is blocked and it cant go further
                                if board[rowNo][vcoord].isupper():
                                    break

                        #Adding Diagonal Moves
                        rcoord=rowNo
                        vcoord=columnNo
                        while True:
                            rcoord-=1
                            vcoord+=1
                            if rcoord>-1 and vcoord<8:
                                if board[rcoord][vcoord]!=' ':
                                    if board[rcoord][vcoord].islower():
                                        break
                                moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(vcoord))}{8-rcoord}")
                                if board[rcoord][vcoord]!=' ':
                                    if board[rcoord][vcoord].isupper():#stop after hitting an opposite piece and adding it to the moves once
                                        break
                            else:
                                break
                        #checking top left
                        rcoord=rowNo
                        vcoord=columnNo
                        while True:
                            rcoord-=1
                            vcoord-=1
                            if rcoord>-1 and vcoord>-1:
                                if board[rcoord][vcoord]!=' ':
                                    if board[rcoord][vcoord].islower():
                                        break
                                moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(vcoord))}{8-rcoord}")
                                if board[rcoord][vcoord]!=' ':
                                    if board[rcoord][vcoord].isupper():#stop after hitting an opposite piece and adding it to the moves once
                                        break
                            else:
                                break
                        #checking bottom right
                        rcoord=rowNo
                        vcoord=columnNo
                        while True:
                            rcoord+=1
                            vcoord+=1
                            if rcoord<8 and vcoord<8:
                                if board[rcoord][vcoord]!=' ':
                                    if board[rcoord][vcoord].islower():
                                        break
                                moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(vcoord))}{8-rcoord}")
                                if board[rcoord][vcoord]!=' ':
                                    if board[rcoord][vcoord].isupper():#stop after hitting an opposite piece and adding it to the moves once
                                        break
                            else:
                                break
                        #checking bottom left
                        rcoord=rowNo
                        vcoord=columnNo
                        while True:
                            rcoord+=1
                            vcoord-=1
                            if rcoord<8 and vcoord>-1:
                                if board[rcoord][vcoord]!=' ':
                                    if board[rcoord][vcoord].islower():
                                        break
                                moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(vcoord))}{8-rcoord}")
                                if board[rcoord][vcoord]!=' ':
                                    if board[rcoord][vcoord].isupper():#stop after hitting an opposite piece and adding it to the moves once
                                        break
                            else:
                                break
                    else:#Checking for White Queen
                        #Adding Veritcal and horizontal Moves
                        for hcoord in range(rowNo+1,8): 
                            if board[hcoord][columnNo]!=' ':
                                if board[hcoord][columnNo].isupper():
                                    break
                            moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+columnNo)}{8-hcoord}")
                            if board[hcoord][columnNo]!=' ':#if the added move had a destination of the opposite colour piece, then the path for the rook is blocked and it cant go further
                                if board[hcoord][columnNo].islower():
                                    break
                        for hcoord in range(rowNo-1,-1,-1):
                            if board[hcoord][columnNo]!=' ':
                                if board[hcoord][columnNo].isupper():
                                    break
                            moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+columnNo)}{8-hcoord}")
                            if board[hcoord][columnNo]!=' ':#if the added move had a destination of the opposite colour piece, then the path for the rook is blocked and it cant go further
                                if board[hcoord][columnNo].islower():
                                    break
                        #calculating all the moves in horizontal line
                        for vcoord in range(columnNo+1,8):
                            if board[rowNo][vcoord]!=' ':
                                if board[rowNo][vcoord].isupper():
                                    break
                            moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+vcoord)}{8-rowNo}")
                            if board[rowNo][vcoord]!=' ':#if the added move had a destination of the opposite colour piece, then the path for the rook is blocked and it cant go further
                                if board[rowNo][vcoord].islower():
                                    break
                        for vcoord in range(columnNo-1,-1,-1):
                            if board[rowNo][vcoord]!=' ':
                                if board[rowNo][vcoord].isupper():
                                    break
                            moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+vcoord)}{8-rowNo}")
                            if board[rowNo][vcoord]!=' ':#if the added move had a destination of the opposite colour piece, then the path for the rook is blocked and it cant go further
                                if board[rowNo][vcoord].islower():
                                    break
                        #Adding Diagonal Moves
                        rcoord=rowNo
                        vcoord=columnNo
                        while True:
                            rcoord-=1
                            vcoord+=1
                            if rcoord>-1 and vcoord<8:
                                if board[rcoord][vcoord]!=' ':
                                    if board[rcoord][vcoord].isupper():
                                        break
                                moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(vcoord))}{8-rcoord}")
                                if board[rcoord][vcoord]!=' ':
                                    if board[rcoord][vcoord].islower():#stop after hitting an opposite piece and adding it to the moves once
                                        break
                            else:
                                break
                        #checking top left
                        rcoord=rowNo
                        vcoord=columnNo
                        while True:
                            rcoord-=1
                            vcoord-=1
                            if rcoord>-1 and vcoord>-1:
                                if board[rcoord][vcoord]!=' ':
                                    if board[rcoord][vcoord].isupper():
                                        break
                                moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(vcoord))}{8-rcoord}")
                                if board[rcoord][vcoord]!=' ':
                                    if board[rcoord][vcoord].islower():#stop after hitting an opposite piece and adding it to the moves once
                                        break
                            else:
                                break
                        #checking bottom right
                        rcoord=rowNo
                        vcoord=columnNo
                        while True:
                            rcoord+=1
                            vcoord+=1
                            if rcoord<8 and vcoord<8:
                                if board[rcoord][vcoord]!=' ':
                                    if board[rcoord][vcoord].isupper():
                                        break
                                moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(vcoord))}{8-rcoord}")
                                if board[rcoord][vcoord]!=' ':
                                    if board[rcoord][vcoord].islower():#stop after hitting an opposite piece and adding it to the moves once
                                        break
                            else:
                                break
                        #checking bottom left
                        rcoord=rowNo
                        vcoord=columnNo
                        while True:
                            rcoord+=1
                            vcoord-=1
                            if rcoord<8 and vcoord>-1:
                                if board[rcoord][vcoord]!=' ':
                                    if board[rcoord][vcoord].isupper():
                                        break
                                moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(vcoord))}{8-rcoord}")
                                if board[rcoord][vcoord]!=' ':
                                    if board[rcoord][vcoord].islower():#stop after hitting an opposite piece and adding it to the moves once
                                        break
                            else:
                                break

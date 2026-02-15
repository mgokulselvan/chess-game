from Helper import *

def generateBishopMoves(board,rowNo,columnNo,turn):
    moves = []
    #CHECKING - ALL SQUARES FROM THE CURRENT BISHOP POSITION TO THE TOP LEFT OF THE BOARD
    #CHECKING - ALL SQUARES FROM THE CURRENT BISHOP POSITION TO THE TOP RIGHT OF THE BOARD
    #CHECKING - ALL SQUARES FROM THE CURRENT BISHOP POSITION TO THE BOTTOM LEFT OF THE BOARD
    #CHECKING - ALL SQUARES FROM THE CURRENT BISHOP POSITION TO THE BOTTOM RIGHT OF THE BOARD
                    if board[rowNo][columnNo]=='b':#checking if it is a black bishop    
                        #checking top right
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
                    else:#Checking for white bishop
                        #checking top right
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

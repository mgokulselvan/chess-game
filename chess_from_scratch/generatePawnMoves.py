from Helper import *

def generateQueenMoves(board,rowNo,columnNo,turn):
    moves = []
    #CHECKING - FORWARD
    #CHECKING - FORWARD LEFT
    #CHECKING - FORWARD RIGHT 
    #CHECKING - PROMOTION
    #EN PASSANT
                    if board[rowNo][columnNo]=='p':#checking if the pawn isblack 
                        try:
                            if board[rowNo+1][columnNo]==' ':#checking if the square beneath is available or not
                                if rowNo==6:#check if we have to promote the pawn to another piece
                                    for piece in ['r','n','b','q']:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+columnNo)}{8-(rowNo+1)}{piece}")
                                else:#moves for pawn when we dont have to promote it to another piece
                                    moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+columnNo)}{8-(rowNo+1)}")
                                if rowNo==1:#checking if the pawn is in its starting position
                                    if board[rowNo+2][columnNo]==' ':#checking 2 squares below the pawn if its in its starting position
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+columnNo)}{8-(rowNo+2)}")
                        except IndexError:
                            print("have to promote")
                        try:#Attacking
                            if board[rowNo+1][columnNo+1] !=" " and board[rowNo+1][columnNo+1].isupper():#checking if something is in the attacking range of the pawn and if it is a white piece
                                if rowNo==6:#if we have to promote the pawn
                                    for piece in ['r','n','b','q']:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo+1))}{8-(rowNo+1)}{piece}")
                                else:#no promotion of the pawn
                                    moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo+1))}{8-(rowNo+1)}")
                        except IndexError:
                            pass
                        try:
                            if board[rowNo+1][columnNo-1] !=" " and board[rowNo+1][columnNo-1].isupper():
                                if columnNo-1>-1:#to negate negative indexing
                                    if rowNo==6:#if we have to promote the pawn
                                        for piece in ['r','n','b','q']:
                                            moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo-1))}{8-(rowNo+1)}{piece}")
                                    else:#no promotion of the pawn
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo-1))}{8-(rowNo+1)}")
                        except IndexError:
                            pass
                        try:#En Passant
                            if rowNo==4:
                                if board[rowNo][columnNo+1]=='P' and self.moveHistory[-1]==f"{chr(97+(columnNo+1))}2{chr(97+(columnNo+1))}4":
                                    moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo+1))}{8-(rowNo+1)}")
                                elif board[rowNo][columnNo-1]=='P' and self.moveHistory[-1]==f"{chr(97+(columnNo-1))}2{chr(97+(columnNo-1))}4":
                                    moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo-1))}{8-(rowNo+1)}")
                        except IndexError:
                            pass
                    else:#The pawn is white('P') 
                        try:
                            if board[rowNo-1][columnNo]==' ':#checking if the square above is available or not
                                if rowNo-1>-1:
                                    if rowNo==1:#checking if we have to promote the pawn
                                        for piece in ['r','n','b','q']:
                                            moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+columnNo)}{8-(rowNo-1)}{piece}")
                                    else:#no promotion of the pawn
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+columnNo)}{8-(rowNo-1)}")
                                    if rowNo==6:#checking if the pawn is in its starting position
                                        if board[rowNo-2][columnNo]==' ':#checking 2 squares below the pawn if its in its starting position
                                            moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+columnNo)}{8-(rowNo-2)}")
                        except IndexError:
                            pass
                        try:#Attacking
                            if board[rowNo-1][columnNo-1] !=" " and board[rowNo-1][columnNo-1].islower():#checking if something is in the attacking range of the pawn and if it is a white piece
                                if rowNo-1>-1 and columnNo-1>-1:
                                    if rowNo==1:#checking if we have to promote the pawn
                                        for piece in ['r','n','b','q']:
                                            moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo-1))}{8-(rowNo-1)}{piece}")
                                    else:#no promotion of the pawn
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo-1))}{8-(rowNo-1)}")
                        except IndexError:
                            pass
                        try:
                            if board[rowNo-1][columnNo+1] !=" " and board[rowNo-1][columnNo+1].islower():
                                if rowNo-1>-1:
                                    if rowNo==1:#checking if we have to promote the pawn
                                        for piece in ['r','n','b','q']:
                                            moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo+1))}{8-(rowNo-1)}{piece}")
                                    else:#no promotion of the pawn
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo+1))}{8-(rowNo-1)}")
                        except IndexError:
                            pass
                        try:#En Passant
                            if rowNo==3:
                                if board[rowNo][columnNo+1]=='p' and self.moveHistory[-1]==f"{chr(97+(columnNo+1))}7{chr(97+(columnNo+1))}5":
                                    moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo+1))}{8-(rowNo-1)}")
                                elif board[rowNo][columnNo-1]=='p' and self.moveHistory[-1]==f"{chr(97+(columnNo-1))}7{chr(97+(columnNo-1))}5":
                                    moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo-1))}{8-(rowNo-1)}")
                        except IndexError:
                            pass

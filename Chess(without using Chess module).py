import re,copy
#Making a custom Error
class InvalidMoveError(Exception):
    def __init__(self,message):
        self.message=message

    def __str__(self):
        return self.message
    
class Chess:
    def __init__(self):
        self.Board=[
            ['r','n','b','q','k','b','n','r'],#0
            ['p','p','p','p','p','p','p','p'],#1
            [' ',' ',' ',' ',' ',' ',' ',' '],#2
            [' ',' ',' ',' ',' ',' ',' ',' '],#3
            [' ',' ',' ',' ',' ',' ',' ',' '],#4
            [' ',' ',' ',' ',' ',' ',' ',' '],#5
            ['P','P','P','P','P','P','P','P'],#6
            ['R','N','B','Q','K','B','N','R']#7
        ]    #0   1   2   3   4   5   6   7

        self.whiteMove=True
        self.whiteCheckMated=False
        self.blackCheckMated=False
        self.pastBlackChecked=False
        self.pastWhiteChecked=False
        self.presentBlackChecked=False
        self.presentWhiteChecked=False
        self.calculateMoves()
        self.moveHistory=[]

    def playboard(self,guide=True):
        boardString=[]
        for i in range(8):
            if guide:
                guideBorder=f"\033[1m{str(ord(chr(8-i)))}\033[0m"
            else:
                guideBorder=""
            boardString.append(f"{guideBorder} {" ".join(self.Board[i])}")
        if guide:
            boardString.append("\033[1m\u2580"+" A B C D E F G H\033[0m") 
        return '\n'.join(boardString)
    def calculateMoves(self):
        moves=[]
        board=self.Board
        for rowNo in range(8):
            for columnNo in range(8):
                match(board[rowNo][columnNo].lower()):
                    case 'p':#calculating moves for a pawn
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
                    case 'r':#calculating moves for a rook
                        if board[rowNo][columnNo]=='r':#checking moves for black rook
                            #calculating all the moves in the vertical line
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
                                    if board[rowNo][vcoord].isupper():
                                        break
                            for vcoord in range(columnNo-1,-1,-1):
                                if board[rowNo][vcoord]!=' ':
                                    if board[rowNo][vcoord].islower():
                                        break
                                moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+vcoord)}{8-rowNo}")
                                if board[rowNo][vcoord]!=' ':#if the added move had a destination of the opposite colour piece, then the path for the rook is blocked and it cant go further
                                    if board[rowNo][vcoord].isupper():
                                        break
                        else:
                            #checking moves for white rook
                            #calculating all the moves in the vertical line
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
                    case 'n':#calculating moves for a knight
                        if board[rowNo][columnNo]=='n':#Checking if the piece is a black knight
                            try:
                                if board[rowNo-2][columnNo-1]==' ' or board[rowNo-2][columnNo-1].isupper():
                                    if rowNo-2>-1 and columnNo-1>-1:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo-1))}{8-(rowNo-2)}")
                            except IndexError:
                                pass
                            try:
                                if board[rowNo-2][columnNo+1]==' ' or board[rowNo-2][columnNo+1].isupper():
                                    if rowNo-2>-1:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo+1))}{8-(rowNo-2)}")
                            except IndexError:
                                pass
                            try:
                                if board[rowNo+2][columnNo-1]==' ' or board[rowNo+2][columnNo-1].isupper():
                                    if columnNo-1>-1:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo-1))}{8-(rowNo+2)}")
                            except IndexError:
                                pass
                            try:
                                if board[rowNo+2][columnNo+1]==' ' or board[rowNo+2][columnNo+1].isupper():
                                    moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo+1))}{8-(rowNo+2)}")
                            except IndexError:
                                pass
                            try:
                                if board[rowNo-1][columnNo+2]==' ' or board[rowNo-1][columnNo+2].isupper():
                                    if rowNo-1>-1:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo+2))}{8-(rowNo-1)}")
                            except IndexError:
                                pass
                            try:
                                if board[rowNo+1][columnNo+2]==' ' or board[rowNo+1][columnNo+2].isupper():
                                    moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo+2))}{8-(rowNo+1)}")
                            except IndexError:
                                pass
                            try:
                                if board[rowNo-1][columnNo-2]==' ' or board[rowNo-1][columnNo-2].isupper():
                                    if rowNo-1>-1 and columnNo-2>-1:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo-2))}{8-(rowNo-1)}")
                            except IndexError:
                                pass
                            try:
                                if board[rowNo+1][columnNo-2]==' ' or board[rowNo+1][columnNo-2].isupper():
                                    if columnNo-2>-1:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo-2))}{8-(rowNo+1)}")
                            except IndexError:
                                pass
                        else:#checking for white knights
                            try:
                                if board[rowNo-2][columnNo-1]==' ' or board[rowNo-2][columnNo-1].islower():
                                    if rowNo-2>-1 and columnNo-1>-1:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo-1))}{8-(rowNo-2)}")
                            except IndexError:
                                pass
                            try:
                                if board[rowNo-2][columnNo+1]==' ' or board[rowNo-2][columnNo+1].islower():
                                    if rowNo-2>-1:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo+1))}{8-(rowNo-2)}")
                            except IndexError:
                                pass
                            try:
                                if board[rowNo+2][columnNo-1]==' ' or board[rowNo+2][columnNo-1].islower():
                                    if columnNo-1>-1:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo-1))}{8-(rowNo+2)}")
                            except IndexError:
                                pass
                            try:
                                if board[rowNo+2][columnNo+1]==' ' or board[rowNo+2][columnNo+1].islower():
                                    moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo+1))}{8-(rowNo+2)}")
                            except IndexError:
                                pass
                            try:
                                if board[rowNo-1][columnNo+2]==' ' or board[rowNo-1][columnNo+2].islower():
                                    if rowNo-1>-1:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo+2))}{8-(rowNo-1)}")
                            except IndexError:
                                pass
                            try:
                                if board[rowNo+1][columnNo+2]==' ' or board[rowNo+1][columnNo+2].islower():
                                    moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo+2))}{8-(rowNo+1)}")
                            except IndexError:
                                pass
                            try:
                                if board[rowNo-1][columnNo-2]==' ' or board[rowNo-1][columnNo-2].islower():
                                    if rowNo-1>-1 and columnNo-2>-1:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo-2))}{8-(rowNo-1)}")
                            except IndexError:
                                pass
                            try:
                                if board[rowNo+1][columnNo-2]==' ' or board[rowNo+1][columnNo-2].islower():
                                    if columnNo-2>-1:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo-2))}{8-(rowNo+1)}")
                            except IndexError:
                                pass 
                    case 'b':#calculating moves for a bishop
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
                    case 'q':#calculating moves for a queen
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
                    case 'k':#calculating moves for a king
                        if board[rowNo][columnNo]=='k':
                            #top left
                            try:
                                if board[rowNo-1][columnNo-1]==' ' or board[rowNo-1][columnNo-1].isupper():
                                    if rowNo-1>-1 and columnNo-1>-1:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo-1))}{8-(rowNo-1)}")
                            except IndexError:
                                pass
                            #top
                            try:
                                if board[rowNo-1][columnNo]==' ' or board[rowNo-1][columnNo].isupper():
                                    if rowNo-1>-1:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo))}{8-(rowNo-1)}")
                            except IndexError:
                                pass
                            #top right
                            try:
                                if board[rowNo-1][columnNo+1]==' ' or board[rowNo-1][columnNo+1].isupper():
                                    if rowNo-1>-1 and columnNo+1<8:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo+1))}{8-(rowNo-1)}")
                            except IndexError:
                                pass
                            #right
                            try:
                                if board[rowNo][columnNo+1]==' ' or board[rowNo][columnNo+1].isupper():
                                    if columnNo+1<8:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo+1))}{8-(rowNo)}")
                            except IndexError:
                                pass
                            #bottom right
                            try:
                                if board[rowNo+1][columnNo+1]==' ' or board[rowNo+1][columnNo+1].isupper():
                                    if rowNo+1<8 and columnNo+1<8:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo+1))}{8-(rowNo+1)}")
                            except IndexError:
                                pass
                            #bottom
                            try:
                                if board[rowNo+1][columnNo]==' ' or board[rowNo+1][columnNo].isupper():
                                    if rowNo+1<8:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo))}{8-(rowNo+1)}")
                            except IndexError:
                                pass
                            #bottom left
                            try:
                                if board[rowNo+1][columnNo-1]==' ' or board[rowNo+1][columnNo-1].isupper():
                                    if columnNo-1>-1 and rowNo+1<8:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo-1))}{8-(rowNo+1)}")
                            except IndexError:
                                pass
                            #left
                            try:
                                if board[rowNo][columnNo-1]==' ' or board[rowNo][columnNo-1].isupper():
                                    if columnNo-1>-1:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo-1))}{8-(rowNo)}")
                            except IndexError:
                                pass
                        else:#For White King
                         #top left
                            try:
                                if board[rowNo-1][columnNo-1]==' ' or board[rowNo-1][columnNo-1].islower():
                                    if rowNo-1>-1 and columnNo-1>-1:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo-1))}{8-(rowNo-1)}")
                            except IndexError:
                                pass
                            #top
                            try:
                                if board[rowNo-1][columnNo]==' ' or board[rowNo-1][columnNo].islower():
                                    if rowNo-1>-1:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo))}{8-(rowNo-1)}")
                            except IndexError:
                                pass
                            #top right
                            try:
                                if board[rowNo-1][columnNo+1]==' ' or board[rowNo-1][columnNo+1].islower():
                                    if rowNo-1>-1 and columnNo+1<8:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo+1))}{8-(rowNo-1)}")
                            except IndexError:
                                pass
                            #right
                            try:
                                if board[rowNo][columnNo+1]==' ' or board[rowNo][columnNo+1].islower():
                                    if columnNo+1<8:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo+1))}{8-(rowNo)}")
                            except IndexError:
                                pass
                            #bottom right
                            try:
                                if board[rowNo+1][columnNo+1]==' ' or board[rowNo+1][columnNo+1].islower():
                                    if rowNo+1<8 and columnNo+1<8:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo+1))}{8-(rowNo+1)}")
                            except IndexError:
                                pass
                            #bottom
                            try:
                                if board[rowNo+1][columnNo]==' ' or board[rowNo+1][columnNo].islower():
                                    if rowNo+1<8:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo))}{8-(rowNo+1)}")
                            except IndexError:
                                pass
                            #bottom left
                            try:
                                if board[rowNo+1][columnNo-1]==' ' or board[rowNo+1][columnNo-1].islower():
                                    if columnNo-1>-1 and rowNo+1<8:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo-1))}{8-(rowNo+1)}")
                            except IndexError:
                                pass
                            #left
                            try:
                                if board[rowNo][columnNo-1]==' ' or board[rowNo][columnNo-1].islower():
                                    if columnNo-1>-1:
                                        moves.append(f"{chr(97+columnNo)}{8-rowNo}{chr(97+(columnNo-1))}{8-(rowNo)}")
                            except IndexError:
                                pass
        self.moves=moves
        return moves
    def makeAMove(self,move):#Takes a move, checks if it is valid or invalid and moves if it is a valid move
        #Keeping a backup to rollback to
        previousBoard=Chess()
        previousBoard.Board=copy.deepcopy(self.Board)

        movePattern=re.search(r"^(?P<from_columnNo>[a-h]{1})(?P<from_rowNo>[1-8]{1})(?P<to_columnNo>[a-h]{1})(?P<to_rowNo>[1-8]{1})(?P<promotion_to>[rnbq]?)$",move)
        if movePattern:
            fromColumnNo=ord(movePattern.group('from_columnNo'))-97
            fromRowNo=8-int(movePattern.group('from_rowNo'))
            toColumnNo=ord(movePattern.group('to_columnNo'))-97
            toRowNo=8-int(movePattern.group('to_rowNo'))
            promotionTo=movePattern.group('promotion_to')
            #Checking if the move made is by the right color piece
            if self.Board[fromRowNo][fromColumnNo].isupper() and not self.whiteMove:
                raise InvalidMoveError("Black to move,not White")
            if self.Board[fromRowNo][fromColumnNo].islower() and self.whiteMove:
                raise InvalidMoveError("White to move,not Black")
            
            #Castling
            if move in ['e1g1','e1c1','e8g8','e8c8']:
                castelingPermission=True
                if self.whiteMove:
                    if not self.presentWhiteChecked:
                        if move=='e1g1':
                            for move in self.moveHistory:
                                if move.startswith('e1') or move.startswith('h1'):
                                    castelingPermission=False
                            
                            temp=Chess()
                            temp.Board=copy.deepcopy(self.Board)
                            temp.Board[7][4]=' '
                            temp.Board[7][5]='K'
                            temp.check()
                            if temp.presentWhiteChecked:
                                castelingPermission=False
                            if castelingPermission:
                                if self.Board[7][5] ==' ' and self.Board[7][6]==' ' and self.Board[7][4]=='K' and self.Board[7][7]=='R':
                                    self.Board[7][6]='K'
                                    self.Board[7][5]='R'
                                    self.Board[7][4]=' '
                                    self.Board[7][7]=' '
                        elif move=='e1c1':
                            for move in self.moveHistory:
                                if move.startswith('e1') or move.startswith('a1'):
                                    castelingPermission=False
                            
                            temp=Chess()
                            temp.Board=copy.deepcopy(self.Board)
                            temp.Board[7][4]=' '
                            temp.Board[7][3]='K'
                            temp.check()
                            if temp.presentWhiteChecked:
                                castelingPermission=False
                            
                            if castelingPermission:
                                if self.Board[7][1] ==' ' and self.Board[7][2]==' ' and self.Board[7][3]==' ' and self.Board[7][4]=='K' and self.Board[7][0]=='R':
                                        self.Board[7][2]='K'
                                        self.Board[7][3]='R'
                                        self.Board[7][4]=' '
                                        self.Board[7][0]=' '
                elif not self.whiteMove:
                    if not self.presentBlackChecked:
                        if move=='e8g8':
                            for move in self.moveHistory:
                                if move.startswith('e8') or move.startswith('h8'):
                                    castelingPermission=False
                            temp=Chess()
                            temp.Board=copy.deepcopy(self.Board)
                            temp.Board[0][4]=' '
                            temp.Board[0][5]='k'
                            temp.check()
                            if temp.presentWhiteChecked:
                                castelingPermission=False
                            if castelingPermission:
                                if self.Board[0][5] ==' ' and self.Board[0][6]==' ' and self.Board[0][4]=='k' and self.Board[0][7]=='r':
                                    self.Board[0][6]='k'
                                    self.Board[0][5]='r'
                                    self.Board[0][4]=' '
                                    self.Board[0][7]=' '
                        elif move=='e8c8':
                            for move in self.moveHistory:
                                if move.startswith('e8') or move.startswith('a8'):
                                    castelingPermission=False
                            temp=Chess()
                            temp.Board=copy.deepcopy(self.Board)
                            temp.Board[0][4]=' '
                            temp.Board[0][3]='k'
                            temp.check()
                            if temp.presentWhiteChecked:
                                castelingPermission=False

                            if castelingPermission:
                                if self.Board[0][1] ==' ' and self.Board[0][2]==' ' and self.Board[0][3]==' ' and self.Board[0][4]=='k' and self.Board[0][0]=='r':
                                    self.Board[0][2]='k'
                                    self.Board[0][3]='r'
                                    self.Board[0][4]=' '
                                    self.Board[0][0]=' '
            if move in self.moves:
                #Checking En Passant
                try:
                    if self.Board[fromRowNo][fromColumnNo]=='P' and self.Board[fromRowNo][fromColumnNo+1]=='p' and self.moveHistory[-1]==f"{chr(97+(fromColumnNo+1))}7{chr(97+(fromColumnNo+1))}5":
                        self.Board[fromRowNo][fromColumnNo]=" "
                        self.Board[fromRowNo][fromColumnNo+1]=" "
                        self.Board[toRowNo][toColumnNo]="P"
                except IndexError:
                    pass
                try:
                    if self.Board[fromRowNo][fromColumnNo]=='P' and self.Board[fromRowNo][fromColumnNo-1]=='p' and self.moveHistory[-1]==f"{chr(97+(fromColumnNo-1))}7{chr(97+(fromColumnNo-1))}5":
                        self.Board[fromRowNo][fromColumnNo]=" "
                        self.Board[fromRowNo][fromColumnNo-1]=" "
                        self.Board[toRowNo][toColumnNo]="P"
                except IndexError:
                    pass
                try:    
                    if self.Board[fromRowNo][fromColumnNo]=='p' and self.Board[fromRowNo][fromColumnNo+1]=='P' and self.moveHistory[-1]==f"{chr(97+(fromColumnNo+1))}2{chr(97+(fromColumnNo+1))}4":
                        self.Board[fromRowNo][fromColumnNo]=" "
                        self.Board[fromRowNo][fromColumnNo+1]=" "
                        self.Board[toRowNo][toColumnNo]="p"
                except IndexError:
                    pass
                try:
                    if self.Board[fromRowNo][fromColumnNo]=='p' and self.Board[fromRowNo][fromColumnNo-1]=='P' and self.moveHistory[-1]==f"{chr(97+(fromColumnNo-1))}2{chr(97+(fromColumnNo-1))}4":
                        self.Board[fromRowNo][fromColumnNo]=" "
                        self.Board[fromRowNo][fromColumnNo-1]=" "
                        self.Board[toRowNo][toColumnNo]="p"
                except IndexError:
                    pass

                #Checking for White pawn (Promotion)
                if self.Board[fromRowNo][fromColumnNo]=='P' and fromRowNo==1:
                    if not promotionTo:
                        raise InvalidMoveError("Invalid Move,include what to promote the pawn to")
                    else:
                        if move in self.moves:
                            self.Board[toRowNo][toColumnNo]=promotionTo.upper()
                            self.Board[fromRowNo][fromColumnNo]=' '
                        else:
                            raise InvalidMoveError("Not one of the Possible moves")
                #checking for black pawn(Promotion)
                elif self.Board[fromRowNo][fromColumnNo]=='p' and fromRowNo==6:
                    if not promotionTo:
                        raise InvalidMoveError("Invalid Move,include what to promote the pawn to")

                    else:
                        if move in self.moves:
                            self.Board[toRowNo][toColumnNo]=promotionTo.lower()
                            self.Board[fromRowNo][fromColumnNo]=' '
                        else:
                            raise InvalidMoveError("Not one of the Possible moves")
                elif promotionTo:
                    raise InvalidMoveError("Invalid Move,Promotion is not available")
                else:
                    if move in self.moves:
                        self.Board[toRowNo][toColumnNo]=self.Board[fromRowNo][fromColumnNo]
                        self.Board[fromRowNo][fromColumnNo]=' '
                    else:
                        raise InvalidMoveError("Not one of the Possible moves")
                #Calculating the moves for the updated board to check for checks
                self.moveHistory.append(move)#Adding the ligit(for now) move
                self.calculateMoves()#Moves updated
                self.pastWhiteChecked=self.presentWhiteChecked
                self.pastBlackChecked=self.presentBlackChecked
                self.check()
                if self.whiteMove:
                    if self.pastWhiteChecked==True:
                        if self.presentWhiteChecked==True:
                            self.Board=copy.deepcopy(previousBoard.Board)
                            self.moveHistory.pop()
                            raise InvalidMoveError("White is still Checked,make a different Move")
                        
                if not self.whiteMove:
                    if self.pastBlackChecked==True:
                        if self.presentBlackChecked==True:
                            self.Board=copy.deepcopy(previousBoard.Board)
                            self.moveHistory.pop()
                            raise InvalidMoveError("Black is still Checked,make a different Move")
                        
                #Checking if the move made leads to a check
                if self.Board[toRowNo][toColumnNo].isupper():#FOR WHITE
                    for rowNo in range(8):
                        for columnNo in range(8):
                            if self.Board[rowNo][columnNo]=='K':
                                for move in self.moves:
                                    if move.endswith(f"{chr(97+columnNo)}{8-rowNo}"):
                                        self.Board=copy.deepcopy(previousBoard.Board)
                                        self.moveHistory.pop()
                                        raise InvalidMoveError("Invalid Move,The Move leads to a check")   
                                return
                else:#FOR BLACK
                    for rowNo in range(8):
                        for columnNo in range(8):
                            if self.Board[rowNo][columnNo]=='k':
                                for move in self.moves:
                                    if move.endswith(f"{chr(97+columnNo)}{8-rowNo}"):
                                        self.Board=copy.deepcopy(previousBoard.Board)
                                        self.moveHistory.pop()
                                        raise InvalidMoveError("Invalid Move,The Move leads to a check")
                                return
            else:
                raise InvalidMoveError("Invalid Move,Move not possible")
        else:
            raise InvalidMoveError("Not in UCI format")
        

    def checkMate(self):
        # Assume player is checkmated
        if self.whiteMove:
            isCheckMate = self.presentWhiteChecked
        else:
            isCheckMate = self.presentBlackChecked
        # isCheckMate = True
        temp=Chess()
        temp=copy.deepcopy(self)

        for move in temp.moves:
            try:
                temp.makeAMove(move)
                isCheckMate=False
            except Exception as e:
                continue

        if isCheckMate and self.whiteMove:
            self.whiteCheckMated=True
            self.blackCheckMated=False

        if isCheckMate and not self.whiteMove:
            self.whiteCheckMated=False
            self.blackCheckMated=True

        return isCheckMate
    

    def staleMate(self):#Not Used
        temp=Chess()
        temp.Board=copy.deepcopy(self.Board)
        isStalemate=True
        temp.whiteMove=self.whiteMove
        temp.calculateMoves()
        for move in temp.moves:
            try:
                temp.makeAMove(move)
                isStalemate=False
            except:
                continue
        return isStalemate
    def check(self):
       self.presentWhiteChecked=False
       self.presentBlackChecked=False
       temp=Chess()
       temp.Board=copy.deepcopy(self.Board)
       temp.whiteMove= not self.whiteMove
       temp.calculateMoves()
       for rowNo in range(8):
        for columnNo in range(8):
            if self.Board[rowNo][columnNo] == 'k':
                king_square = f"{chr(97 + columnNo)}{8 - rowNo}"
                for move in temp.moves:
                    if move.endswith(king_square):
                        self.presentBlackChecked=True

            elif self.Board[rowNo][columnNo] == 'K':
                king_square = f"{chr(97 + columnNo)}{8 - rowNo}"
                for move in temp.moves:
                    if move.endswith(king_square):
                        self.presentWhiteChecked = True                      
#Game loop

chessgame=Chess()
print(chessgame.playboard())
while True:
    if not chessgame.checkMate(): #and not chessgame.staleMate():
        if chessgame.whiteMove:
            print("White's turn")
        else:
            print("Black's turn")  
        move=input("Input your move in UCI format:")
        try:
            chessgame.makeAMove(move)
            print(chessgame.playboard())
            chessgame.whiteMove=not chessgame.whiteMove
        except InvalidMoveError as x:
            print(x)
    elif chessgame.checkMate():
        print("Checkmate")
        if chessgame.blackCheckMated:
            print("White Wins")
        elif chessgame.whiteCheckMated:
            print("Black Wins")
        break

    # chessgame.whiteMove=not chessgame.whiteMove
    # elif chessgame.staleMate():
    #     print("Game draw by Stalemate")
    #     break
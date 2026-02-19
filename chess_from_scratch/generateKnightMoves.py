def generateKnightoves(board,rowNo,columnNo,turn):
    moves=[]
    if board[rowNo][columnNo]=='n':#Checking if the piece is a black knight
        try:
            if board[rowNo-2][columnNo-1]=='.' or board[rowNo-2][columnNo-1].isupper():
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

from Notations import *
from Helper import *

def generatePawnMoves(board,rowNo,columnNo,turn,history):
    moves = []
    forward = 1 if board[rowNo][columnNo] == 'p' else -1
    penultimateRow = 6 if board[rowNo][columnNo] == 'p' else 1
    startingRow = 1 if board[rowNo][columnNo] == 'p' else 6
    upgradeOptions = ['r','n','b','q'] if board[rowNo][columnNo] == 'p' else ['R','N','B','Q']

    #CHECKING - FORWARD
    try:
        if board[rowNo+forward][columnNo]=='.':
            if rowNo == penultimateRow:
                for piece in upgradeOptions:
                    moves.append(Notation([(rowNo,columnNo),(rowNo+forward,columnNo),(piece)]))
            else:
                moves.append(Notation([(rowNo,columnNo),(rowNo+forward,columnNo)]))
            if rowNo == startingRow and board[rowNo+(2*forward)][columnNo] == '.':
                moves.append(Notation([(rowNo,columnNo),(rowNo+(2*forward),columnNo)]))
    except IndexError:
        pass


    #CHECKING - FORWARD SIDE 1
    try:
        if board[rowNo+forward][columnNo+1] !='.' and is_enemy(board[rowNo+forward][columnNo+1],turn):
            if rowNo == penultimateRow:
                for piece in upgradeOptions:
                    moves.append(Notation([(rowNo,columnNo),(rowNo+forward,columnNo+1),(piece)]))
            else:
                moves.append(Notation([(rowNo,columnNo),(rowNo+forward,columnNo+1)]))
    except IndexError:
        pass
    #CHECKING - FORWARD SIDE 2
    try:
        if board[rowNo+forward][columnNo-1] !='.' and is_enemy(board[rowNo+forward][columnNo-1],turn):
            if columnNo-1>-1:#to negate negative indexing
                if rowNo == penultimateRow:
                    for piece in upgradeOptions:
                        moves.append(Notation([(rowNo,columnNo),(rowNo+forward,columnNo-1),(piece)]))
                else:
                    moves.append(Notation([(rowNo,columnNo),(rowNo+forward,columnNo-1)]))
    except IndexError:
        pass


    #EN PASSANT

    def is_enemy_pawn(self , ch , turn):
        if not is_enemy(ch , turn):
            return False
        else:
            if ch == 'p' and self =='p':
                return False
            if ch == 'P' and self =='P':
                return False
            if ch == 'p' and self =='P':
                return True
            if ch == 'P' and self =='p':
                return True

    try:
        if rowNo == penultimateRow -(2*forward):
            if is_enemy_pawn(board[rowNo][columnNo],board[rowNo][columnNo-1],turn) and (columnNo - 1 > -1) and history[-1]==Notation([(penultimateRow,columnNo-1),(rowNo,columnNo-1)]) and board[rowNo+forward][columnNo-1]=='.':
                moves.append(Notation([(rowNo,columnNo),(rowNo+forward,columnNo-1)]))
            if is_enemy_pawn(board[rowNo][columnNo],board[rowNo][columnNo+1],turn) and history[-1]==Notation([(penultimateRow,columnNo+1),(rowNo,columnNo+1)]) and board[rowNo+forward][columnNo+1]=='.' :
                moves.append(Notation([(rowNo,columnNo),(rowNo+forward,columnNo+1)]))
    except IndexError:
        pass
    return moves

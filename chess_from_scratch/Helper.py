from enum import Enum
from Notations import *
from resultsInCheck import *
from makeMove import *

#CUSTOM ERROR
class InvalidMoveError(Exception):
    def __init__(self,message):
        self.message=message

    def __str__(self):
        return self.message

#ENUM FOR MOVE STATUS
class TURN(Enum):
    WHITE = "white"
    BLACK = "black"

def is_enemy(piece,turn):
    if (turn==TURN.WHITE and piece.islower())\
            or\
        (turn==TURN.BLACK and piece.isupper()):
        return True
    else:
        return False

def makeGameStateKey(gameBoard, currentTurn, castlingRights, enPassantTarget):
    boardKey = ''.join(''.join(row) for row in gameBoard)
    castlingKey = str(castlingRights["white-kingside"])+\
                  str(castlingRights["white-queenside"])+\
                  str(castlingRights["black-kingside"])+\
                  str(castlingRights["black-queenside"])
    return (boardKey, currentTurn.value, castlingKey, enPassantTarget)


def getEnPassantTarget(board, movesHistory):
    if not movesHistory:
        return None
    lastMove = moves(movesHistory[-1])
    srcRow, srcCol = lastMove[0]
    destRow, destCol = lastMove[1]
    piece = board[destRow][destCol]
     
    if piece.lower() == 'p' and abs(destRow-srcRow)==2:
        targetRow = (srcRow + destRow) // 2
        targetCol = srcCol

        if piece == 'P':
            if destCol -1 >=0 and board[destRow][destCol - 1] == 'p':
                enemyTurn = TURN.BLACK 
                candidateMove = Notation([(destRow,destCol-1),(targetRow,targetCol)])
                if not resultsInCheck(board,enemyTurn,candidateMove,movesHistory):
                    return (targetRow, targetCol)
            if destCol +1 <8 and board[destRow][destCol + 1] == 'p':
                enemyTurn = TURN.BLACK 
                candidateMove = Notation([(destRow,destCol+1),(targetRow,targetCol)])
                if not resultsInCheck(board,enemyTurn,candidateMove,movesHistory):
                    return (targetRow, targetCol)

        if piece == 'p':
            if destCol -1 >=0 and board[destRow][destCol - 1] == 'P':
                enemyTurn = TURN.WHITE 
                candidateMove = Notation([(destRow,destCol-1),(targetRow,targetCol)])
                if not resultsInCheck(board,enemyTurn,candidateMove,movesHistory):
                    return (targetRow, targetCol)
            if destCol +1 <8 and board[destRow][destCol + 1] == 'P':
                enemyTurn = TURN.WHITE 
                candidateMove = Notation([(destRow,destCol+1),(targetRow,targetCol)])
                if not resultsInCheck(board,enemyTurn,candidateMove,movesHistory):
                    return (targetRow, targetCol)
    return None


from enum import Enum
from Notations import *

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

#to not have cyclic import
from resultsInCheck import *
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

def moveClockReset(board,move,enPassantTarget):
    move = moves(move)
    srcRow, srcCol = move[0]
    destRow, destCol = move[1]

    srcPiece = board[srcRow][srcCol]
    destPiece = board[destRow][destCol]

    if srcPiece.lower() == 'p':
        return True
    
    if destPiece != '.':
        return True

    if enPassantTarget is not None and move[1] == enPassantTarget:#redundant because en passant only works if source piece is a pawn, which is already checked ,but its also harmless
        return True
    
    return False

def isInsufficient(g1,g2):
    #king vs king
    if (
        g1["k"]==1 and g2["k"]==1 
        and len(g1["b"])+g1["n"]+g1["o"]==0
        and len(g2["b"])+g2["n"]+g2["o"]==0
            ):
        return True

    #king + bishop vs king
    if (
        g1["k"]==1 and g2["k"]==1 
        and len(g1["b"])==1 
        and g1["n"]+g1["o"]==0 
        and len(g2["b"])+g2["n"]+g2["o"]==0
            ):
        return True

    #king + knight vs king
    if (
        g1["k"]==1 and g2["k"]==1 
        and g1["n"]==1 
        and len(g1["b"])+g1["o"]==0 
        and len(g2["b"])+g2["n"]+g2["o"]==0
            ):
        return True

    #king + bishop vs king + bishop with bishop on same color square
    if (
        g1["k"]==1 and g2["k"]==1 
        and len(g1["b"])==1 
        and len(g2["b"])==1 
        and g1["o"]+g1["n"]==0 
        and g2["o"]+g2["n"]==0 
        and (g1["b"][0][0] + g1["b"][0][1]) % 2 == (g2["b"][0][0] + g2["b"][0][1]) % 2
            ):
        return True

    return False


def insufficientMaterial(board):
    g1={
            "k":0,
            "b":[],
            "n":0,
            "o":0
            }

    g2={
            "k":0,
            "b":[],
            "n":0,
            "o":0
            }
    for rowno,row in enumerate(board):
        for colno,square in enumerate(row):
            if square == '.':
                pass

            elif square.isupper():
                #white
                if square=="B":
                    g1["b"].append((colno,rowno))
                elif square=="N":
                    g1["n"]+=1
                elif square=='K':
                    g1["k"]+=1
                else:
                    g1["o"]+=1

            elif square.islower():
                #black
                if square=="b":
                    g2["b"].append((colno,rowno))
                elif square=="n":
                    g2["n"]+=1
                elif square=='k':
                    g2["k"]+=1
                else:
                    g2["o"]+=1

    if isInsufficient(g1,g2) or isInsufficient(g2,g1):
        return True
    else:
        return False

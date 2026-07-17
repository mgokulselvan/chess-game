from makeMove import makeMove
from isSquareChecked import isKingInCheck

def resultsInCheck(board,turn,move,history):
    tempBoard = makeMove(board , move)
    tempHistory = history+[move]

    return isKingInCheck(tempBoard, turn, tempHistory)

from Notations import *
from Helper import *
from makeMove import *

def resultsInCheck(board,turn,move,history,castlingRights):
    from generateAllPseudoMoves import generateAllPseudoMoves

    tempBoard = makeMove(board , move)
    tempHistory = history+[move]
    if turn ==TURN.WHITE:
        tempTurn = TURN.BLACK
    else:
        tempTurn = TURN.WHITE
    tempMoves = generateAllPseudoMoves(tempBoard,tempTurn,tempHistory,castlingRights)
    #CHECK IF THE DESTINATION IS A KING OF ENEMY KIND, IF SO RETURN TRUE AT THE END RETURN FALSE
    for move in tempMoves:
        Move = moves(move)
        (rowNo,columnNo) = Move[1] 
        if is_enemy(tempBoard[rowNo][columnNo],tempTurn) and tempBoard[rowNo][columnNo].lower() == 'k':
            return True
    return False

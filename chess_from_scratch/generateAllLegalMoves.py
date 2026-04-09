from generateAllPseudoMoves import *
from resultsInCheck import *

def generateAllLegalMoves(board,turn,history,castlingRights):
    pseudoMoves = generateAllPseudoMoves(board,turn,history,castlingRights)
    legalMoves = []
    for move in pseudoMoves:
        if not resultsInCheck(board,turn,move,history,castlingRights):
            legalMoves.append(move)
    return legalMoves

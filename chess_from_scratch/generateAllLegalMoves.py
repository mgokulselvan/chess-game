from generateAllPseudoMoves import *
from resultsInCheck import *

def generateAllLegalMoves(board,turn,history):
    pseudoMoves = generateAllPseudoMoves(board,turn,history)
    legalMoves = []
    for move in pseudoMoves:
        if not resultsInCheck(board,turn,move,history):
            legalMoves.append(move)
    return legalMoves

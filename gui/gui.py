import pygame
from moves.generateAllLegalMoves import *
from Helper import *
from makeMove import *
from gui.pieces import p
from gui.theme import *
import copy

StartingBoard = [
        ['r' , 'n' , 'b' , 'q' , 'k' , 'b' , 'n' , 'r'],#0 #8
        ['p' , 'p' , 'p' , 'p' , 'p' , 'p' , 'p' , 'p'],#1 #7
        ['.' , '.' , '.' , '.' , '.' , '.' , '.' , '.'],#2 #6
        ['.' , '.' , '.' , '.' , '.' , '.' , '.' , '.'],#3 #5
        ['.' , '.' , '.' , '.' , '.' , '.' , '.' , '.'],#4 #4
        ['.' , '.' , '.' , '.' , '.' , '.' , '.' , '.'],#5 #3
        ['P' , 'P' , 'P' , 'P' , 'P' , 'P' , 'P' , 'P'],#6 #2
        ['R' , 'N' , 'B' , 'Q' , 'K' , 'B' , 'N' , 'R'] #7 #1
    ]    #0     1     2     3     4     5     6     7
         #a     b     c     d     e     f     g     h

boxlen = 80

StartingCastlingRights = {
    "white-kingside":True,
    "white-queenside":True,
    "black-kingside":True,
    "black-queenside":True
}

#for overlaying on the piece that the player clicks on
overlay = pygame.Surface((boxlen, boxlen), pygame.SRCALPHA)
overlay.fill((255, 165, 0, 150))

#popup for when player has to promote a pawn
popup = pygame.Surface((400,200),pygame.SRCALPHA)
popup.fill((30,30,30,230))

def getBoardPos(coords):
    (x , y) = coords
    rowNo = x//80
    colNo = y//80
    return (rowNo,colNo)


def drawBoard(screen,board,piecePos,firstClickDone):
    screen.fill(bgcol)
    #Drawing the board with 8x8 boxes
    for rowno,row in enumerate(board): #rowno is y , and colno is x
        for colno,box in enumerate(row):
            color = lightsqcol if (rowno+colno)%2==0 else darksqcol
            pygame.draw.rect(screen, color, pygame.Rect(colno*boxlen, rowno*boxlen, boxlen, boxlen))

            # if there is a piece on that box
            if box !='.':
                piece=''

                if box.isupper():
                    piece=piece+'w'
                elif box.islower():
                    piece=piece+'b'

                piece=piece+box.lower()
                screen.blit(p[piece], (colno * boxlen+5, rowno * boxlen+5))

    #highlighting the piece that the mouse clicks
    if firstClickDone:
        screen.blit(overlay,(piecePos[0] * boxlen, piecePos[1] * boxlen))


def drawPromotionMenu(screen, color):
    screen.blit(popup, (120, 220))

    pieces = ["q", "r", "b", "n"]

    for i, piece in enumerate(pieces):
        screen.blit(
            p[color + piece],
            (130 + i * 90, 285)
        )


def boardPosToMove(firstPos,secPos,screen,board,firstClickDone,running,currentTurn,clock):
    move=''
    indexToAlphaMap = ["a","b","c","d","e","f","g","h"]
    indexToNumMap = ["8","7","6","5","4","3","2","1"]
    move+=(indexToAlphaMap[firstPos[0]]+indexToNumMap[firstPos[1]]+indexToAlphaMap[secPos[0]]+indexToNumMap[secPos[1]])
    #checking if the move is a pawn promotion
    if( (firstPos[1]==1 and secPos[1]==0 and board[firstPos[1]][firstPos[0]]=='P' ) or (firstPos[1]==6 and secPos[1]==7 and board[firstPos[1]][firstPos[0]]=='p') ):
        notchosen = True
        turnstr = "w" if currentTurn == TURN.WHITE else "b"
        while notchosen:
            drawBoard(screen,board,firstPos,firstClickDone)
            drawPromotionMenu(screen,turnstr)

            for event in pygame.event.get():
                if event == pygame.QUIT:
                    notchosen = False
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    chosenPiece = ""
                    mouseX, mouseY = pygame.mouse.get_pos()

                    if 285 <= mouseY <= 355:
                        if 130 <= mouseX < 200:
                            chosenPiece = "q"
                        elif 220 <= mouseX < 290:
                            chosenPiece = "r"
                        elif 310 <= mouseX < 380:
                            chosenPiece = "b"
                        elif 400 <= mouseX < 470:
                            chosenPiece = "n"
                    if chosenPiece !="":
                        notchosen = False
                        move+=chosenPiece.upper() if currentTurn == TURN.WHITE else chosenPiece

            pygame.display.flip()#to put all the drawings from above on the screen

            dt = clock.tick(60)/1000#Limit FPS to 60


    return move


def startGUI():

    pygame.init()
    screen = pygame.display.set_mode((640,640))
    clock = pygame.time.Clock()
    running = True


    piecePos=(0,0)
    firstClickDone=False

    enPassantTarget=None
    halfmoveClock = 0
    gameBoard = copy.deepcopy(StartingBoard)
    movesHistory = []
    currentTurn = TURN.WHITE
    castlingRights = copy.deepcopy(StartingCastlingRights)
    initialGameState= makeGameStateKey(gameBoard,currentTurn,castlingRights,None)
    gameStateCounts = {initialGameState: 1}


    #-----------------------------GAME LOOP----------------------------------
    while(running):

        legalMoves = generateAllLegalMoves(gameBoard , currentTurn , movesHistory,castlingRights)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:#quitting graciously without any error on clicking "x" 
                running = False

            #MOUSE CLICK AKA MOVING A PIECE
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not firstClickDone:
                    piecePos = getBoardPos(pygame.mouse.get_pos()) 
                    firstClickDone = True
                else:
                    firstClickDone = False
                    destPos = getBoardPos(pygame.mouse.get_pos())
                    move = boardPosToMove(piecePos,destPos,screen,gameBoard,firstClickDone,running,currentTurn,clock)
                    print(move)
                    if move in legalMoves:
                        gameBoard = makeMove(gameBoard , move)
                        currentTurn = TURN.BLACK if currentTurn == TURN.WHITE else TURN.WHITE
                        movesHistory.append(move)

        #-----------------------drawing----------------------------
        drawBoard(screen,gameBoard,piecePos,firstClickDone)
        pygame.display.flip()#to put all the drawings from above on the screen
        #----------------------end of drawing-----------------------


        dt = clock.tick(60)/1000#Limit FPS to 60

    pygame.quit()






if __name__ == "__main__":
    startGUI()

import pygame
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

def getBoardPos(coords):
    (x , y) = coords
    rowNo = x//80
    colNo = y//80
    return (rowNo,colNo)

def boardPosToMove(firstPos,secPos):
    move=''
    indexToAlphaMap = ["a","b","c","d","e","f","g","h"]
    indexToNumMap = ["8","7","6","5","4","3","2","1"]
    move+=(indexToAlphaMap[firstPos[0]]+indexToNumMap[firstPos[1]]+indexToAlphaMap[secPos[0]]+indexToNumMap[secPos[1]])
    return move


def startGUI():

    pygame.init()
    screen = pygame.display.set_mode((640,640))
    clock = pygame.time.Clock()
    running = True
    boxlen = 80

    #for overlaying on the piece that the player clicks on
    overlay = pygame.Surface((boxlen, boxlen), pygame.SRCALPHA)
    overlay.fill((255, 165, 0, 150))

    piecePos=(0,0)
    firstClickDone=False

    gameBoard = copy.deepcopy(StartingBoard)


    #-----------------------------GAME LOOP----------------------------------
    while(running):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:#quitting graciously without any error on clicking "x" 
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not firstClickDone:
                    piecePos = getBoardPos(pygame.mouse.get_pos()) 
                    firstClickDone = True
                else:
                    firstClickDone = False
                    destPos = getBoardPos(pygame.mouse.get_pos())
                    move = boardPosToMove(piecePos,destPos)
                    gameBoard = makeMove(gameBoard , move)



        screen.fill(bgcol)

        #Drawing the board with 8x8 boxes
        for rowno,row in enumerate(gameBoard): #rowno is y , and colno is x
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

        pygame.display.flip()#to put all the drawings from above on the screen

        dt = clock.tick(60)/1000#Limit FPS to 60

    pygame.quit()






if __name__ == "__main__":
    startGUI()

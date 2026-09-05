import pygame
from theme import *
def startGUI():

    pygame.init()
    screen = pygame.display.set_mode((640,640))
    clock = pygame.time.Clock()
    running = True

    while(running):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        gameBoard = [
                ['r' , 'n' , 'b' , 'q' , 'k' , 'b' , 'n' , 'r'],#0 #8
                ['p' , 'p' , 'p' , 'p' , 'p' , 'p' , 'p' , 'p'],#1 #7
                ['.' , '.' , '.' , '.' , '.' , '.' , '.' , '.'],#2 #6
                ['.' , '.' , '.' , '.' , '.' , '.' , '.' , '.'],#3 #5
                ['.' , '.' , '.' , '.' , '.' , '.' , '.' , '.'],#4 #4
                ['.' , '.' , '.' , '.' , '.' , '.' , '.' , '.'],#5 #3
                ['P' , 'P' , 'P' , 'P' , 'P' , 'P' , 'P' , 'P'],#6 #2
                ['R' , 'N' , 'B' , 'Q' , 'K' , 'B' , 'N' , 'R'] #7 #1
            ]

        screen.fill(bgcol)

        #Drawing the board with 8x8 boxes
        boxlen = 80


        for rowno,row in enumerate(gameBoard): #rowno is y , and colno is x
            for colno,box in enumerate(row):
                color = lightsqcol if (rowno+colno)%2==0 else darksqcol
                pygame.draw.rect(screen, color, pygame.Rect(colno*boxlen, rowno*boxlen, boxlen, boxlen))

                # if there is a piece on that box
                if box !='.':
                    if box.isupper():
                        pygame.draw.rect(screen, "#FFFFFF", pygame.Rect(colno*boxlen, rowno*boxlen, boxlen, boxlen))
                    elif box.islower():
                        pygame.draw.rect(screen, "#000000", pygame.Rect(colno*boxlen, rowno*boxlen, boxlen, boxlen))


        pygame.display.flip()#to put all the drawings from above on the screen

        dt = clock.tick(60)/1000#Limit FPS to 60

    pygame.quit()

if __name__ == "__main__":
    startGUI()

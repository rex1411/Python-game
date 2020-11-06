#SETUP
import pygame
import random
import sys
pygame.init()

moveLeft = pygame.image.load('8.png')
moveRight = pygame.image.load('1.png')
moveUp = pygame.image.load('4.png')
moveDown = pygame.image.load('3.png')
back = pygame.image.load('background2.png')
spaceship = pygame.image.load('6.png')
enemy1 = pygame.image.load('enemy1.png')
bullet = pygame.image.load('bullet.png')


clock = pygame.time.Clock()
Up = False
Down = False
Right = False
Left = False
width = 1200
height = 900
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
playerSize = 125
PlayerPos = [width/2,height-2*playerSize]
backgroundColour = (0,0,0)
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game')



def redrawWindow():
    gameDisplay.blit(back, (0,0))
    if Left:
        gameDisplay.blit(moveLeft, (PlayerPos[0],PlayerPos[1]))
    if Right:
        gameDisplay.blit(moveRight, (PlayerPos[0],PlayerPos[1]))
    if Up:
        gameDisplay.blit(moveUp, (PlayerPos[0],PlayerPos[1]))
    if Down:
        gameDisplay.blit(moveDown, (PlayerPos[0],PlayerPos[1]))
    else:
        gameDisplay.blit(spaceship, (PlayerPos[0],PlayerPos[1]))
    
    pygame.display.update()


#THE USER DOES SOMETHING TO START THE GAME.
gameRunning = True

#THE GAME LOOP.
while gameRunning:
    clock.tick(60)
  
    #HANDLE EVENTS
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
          sys.exit()
          gameRunning = False


        if event.type == pygame.KEYDOWN:
            x = PlayerPos[0]
            y = PlayerPos[1]

            if event.key == pygame.K_LEFT:
                x-=playerSize
                Left = True
                Right = False
                Down = False
                Up = False

            if event.key == pygame.K_RIGHT:
                x += playerSize
                Right = True
                Left = False
                Down = False
                Up = False

            if event.key == pygame.K_UP:
                y -=playerSize
                Right = False
                Left = False
                Down = False
                Up = True

            elif event.key == pygame.K_DOWN:
                y += playerSize
                Right = False
                Left = False
                Down = True
                Up = False
            else:
                Right = False
                Left = False
                Down = False
                Up = False
                WalkAmount = 0
            PlayerPos = [x,y]

            redrawWindow()
  
    
            




    
'''
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                gameRunning = False

 gameDisplay.fill((255, 255 ,255))
 pygame.display.update()
        

#CLEAN UP WHEN FINISHED.
pygame.quit()
quit()

'''

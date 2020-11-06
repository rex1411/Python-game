#SETUP
import pygame
import sys
pygame.init()
width = 800
height = 600
red = (255,0,0)
playerSize = 50
PlayerPos = [width/2,height-2*playerSize]
velocity = 6


gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game')

#THE USER DOES SOMETHING TO START THE GAME.
gameRunning = True

#THE GAME LOOP.
while gameRunning:
  
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

            if event.key == pygame.K_RIGHT:
                x += playerSize

            if event.key == pygame.K_UP:
                y -=playerSize

            if event.key == pygame.K_DOWN:
                y += playerSize

            PlayerPos = [x,y]

            
    pygame.draw.rect(gameDisplay, red, (PlayerPos[0], PlayerPos[1], playerSize, playerSize))
    pygame.display.update()




    
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

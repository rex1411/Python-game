#SETUP
import pygame
import sys
pygame.init()
width = 800
height = 600
red = (255,0,0)
player_pos = [400,300]
player_size = 50


gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('My Game...')

#THE USER DOES SOMETHING TO START THE GAME.
gameRunning = True

#THE GAME LOOP.
while gameRunning:
  
    #HANDLE EVENTS
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
          sys.exit()
          gameRunning = False
    pygame.draw.rect(gameDisplay, red, (player_pos[0], player_pos[1], player_size, player_size))
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

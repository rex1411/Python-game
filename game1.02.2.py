#SETUP
import pygame
import random
import sys
pygame.init()
width = 800
height = 600

red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
backgroundColour = (0,0,0)

playerSize = 50
playerPos = [width/2,height-2*playerSize]

enemySize = 50
enemyPos = [random.randint(0,width-enemySize),0]
enemyList = [enemyPos]

speed = 10


gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('My Game...')

score = 0
clock = pygame.time.Clock()

myfont = pygame.font.SysFont("monospace", 35)

def setLevel(score, speed):
    if score < 20:
        speed = 3
    elif score < 40:
        speed = 4
    elif score < 60:
        speed = 5
    else:
        speed = 15
    return speed




def dropEnemies(enemyList):
    delay = random.random()
    if len(enemyList) < 10 and delay <0.1:
        xPos = random.randint(0, width-enemySize)
        yPos = 0
        enemyList.append([xPos, yPos])

def drawEnemies(enemyList):
    for enemyPos in enemyList:
        pygame.draw.rect(gameDisplay, blue, (enemyPos[0], enemyPos[1], enemySize, enemySize))

def updateEnemyPos(enemyList, score):
    for idx, enemyPos in enumerate (enemyList):
        if enemyPos[1] >= 0 and enemyPos[1] < height:
            enemyPos[1] += speed
        else:
            enemyList.pop(idx)
            score += 1
    return score
    
def collisionCheck(enemyList, playerPos):
    for enemyPos in enemyList:
        if detectCollision(enemyPos, playerPos):
            return True
    return False

def detectCollision(playerPos, enemyPos):
    p_x = playerPos[0]
    p_y = playerPos[1]
    
    e_x = enemyPos[0]
    e_y = enemyPos[1]

    if (e_x >= p_x and e_x < (p_x + playerSize)) or (p_x >= e_x and p_x < (e_x + enemySize)):
            if (e_y >= p_y and e_y < (p_y + playerSize)) or (p_y >= e_y and p_y < (e_y + enemySize)):
                return True
    return False
        

#THE USER DOES SOMETHING TO START THE GAME.
gameRunning = True

#THE GAME LOOP.
while gameRunning:
  
    #HANDLE EVENTS
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
          sys.exit()
         # gameRunning = False


        if event.type == pygame.KEYDOWN:
      
            x = playerPos[0]
            y = playerPos[1]
        
            if event.key == pygame.K_LEFT:
                x -= playerSize
                
            if event.key == pygame.K_RIGHT:
                x += playerSize
                
            if event.key == pygame.K_UP:
                y -=playerSize

            if event.key == pygame.K_DOWN:
                y += playerSize
            
            playerPos = [x,y]
          
    gameDisplay.fill(backgroundColour)

    #updating enemyPos

 #   if enemyPos[1] >= 0 and enemyPos[1] < height:
#        enemyPos[1] += speed[0]
#    else:
#        enemyPos[0] = random.randint(0, width-enemySize)
#        enemyPos[1] = 0

#    if detectCollision(playerPos, enemyPos):
#       gameRunning = False
#    break

    dropEnemies(enemyList)
    score = updateEnemyPos(enemyList, score)
    speed = setLevel(score,speed)


    
    text = "score:" + str(score)
    label = myfont.render(text, 1, yellow)
    gameDisplay.blit(label, (width-200, height-40))
    
    if collisionCheck(enemyList, playerPos):
        gameRunning = False
        break
    
    drawEnemies(enemyList)
    
    pygame.draw.rect(gameDisplay, red, (playerPos[0], playerPos[1], playerSize, playerSize))

    clock.tick(60)


    pygame.display.update()


    
'''
          if event.key == pygame.K_q:
              gameRunning = False
              
 gameDisplay.fill((255, 255 ,255))
 pygame.display.update()
  

#CLEAN UP WHEN FINISHED.
pygame.quit()
quit()
'''

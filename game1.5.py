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
Standing = True
width = 1200
height = 900
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
playerSize = 125
PlayerPos = [width/2,height-2*playerSize]
backgroundColour = (0,0,0)


bullets = []

enemySize = 50
enemyPos = [random.randint(0,width-enemySize),0]
enemyList = [enemyPos]

bulletSpeed = 5
score = 0
speed = 10

gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game')

myfont = pygame.font.SysFont("monospace", 35)

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setY(self, pos):
        self.y = pos

    def getY(self):
        return self.y

    def getX(self):
        return self.x

def setLevel(score, speed):
    if score < 20:
        speed = 5
    elif score < 40:
        speed = 7
    elif score < 60:
        speed = 8
    else:
        speed = 10
    return speed

def dropEnemies(enemyList):
    delay = random.random()
    if len(enemyList) < 5 and delay <0.1:
        xPos = random.randint(0, width-enemySize)
        yPos = 0
        enemyList.append([xPos, yPos])

def drawEnemies(enemyList):
    for enemyPos in enemyList:
         gameDisplay.blit(enemy1, (enemyPos[0],enemyPos[1]))

def updateEnemyPos(enemyList, score):
    for idx, enemyPos in enumerate (enemyList):
        if enemyPos[1] >= 0 and enemyPos[1] < height:
            enemyPos[1] += speed
        else:
            enemyList.pop(idx)
            score += 1
    return score
    
def collisionCheck(enemyList, PlayerPos):
    for enemyPos in enemyList:
        if detectCollision(enemyPos, PlayerPos):
            return True
    return False

def detectCollision(PlayerPos, enemyPos):
    p_x = PlayerPos[0]
    p_y = PlayerPos[1]
    
    e_x = enemyPos[0]
    e_y = enemyPos[1]

    if (e_x >= p_x and e_x < (p_x + playerSize)) or (p_x >= e_x and p_x < (e_x + enemySize)):
            if (e_y >= p_y and e_y < (p_y + playerSize)) or (p_y >= e_y and p_y < (e_y + enemySize)):
                return True
    return False




def redrawWindow():
    gameDisplay.blit(back, (0,0))
    if not (Standing):
        if Left:
            gameDisplay.blit(moveLeft, (PlayerPos[0],PlayerPos[1]))
        if Right:
            gameDisplay.blit(moveRight, (PlayerPos[0],PlayerPos[1]))
        if Up:
            gameDisplay.blit(moveUp, (PlayerPos[0],PlayerPos[1]))
        elif Down:
            gameDisplay.blit(moveDown, (PlayerPos[0],PlayerPos[1]))
    else:
        gameDisplay.blit(spaceship, (PlayerPos[0],PlayerPos[1]))

    for b in bullets:
        if b.getY() <=0:
            bullets.remove(b)
        gameDisplay.blit(bullet, (b.getX(), b.getY()))
        b.setY(b.getY() -5)
    
    pygame.display.update()


#THE USER DOES SOMETHING TO START THE GAME.
gameRunning = True

#THE GAME LOOP.
while gameRunning:
    clock.tick(30)
    

  
    #HANDLE EVENTS
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
          sys.exit()
          gameRunning = False

        if event.type == pygame.KEYDOWN:
            x = PlayerPos[0]
            y = PlayerPos[1]

            if event.key == pygame.K_SPACE:
                b = Bullet(PlayerPos[0] + 90, PlayerPos[1] - 5)
                bullets.append(b)



            if event.key == pygame.K_LEFT:
                x-=playerSize
                Left = True
                Right = False
                Down = False
                Up = False
                Standing = False

            if event.key == pygame.K_RIGHT:
                x += playerSize
                Right = True
                Left = False
                Down = False
                Up = False
                Standing = False

            if event.key == pygame.K_UP:
                y -=playerSize
                Right = False
                Left = False
                Down = False
                Up = True
                Standing = False

            elif event.key == pygame.K_DOWN:
                y += playerSize
                Right = False
                Left = False
                Down = True
                Up = False
                Standing = False
            else:
                Right = False
                Left = False
                Down = False
                Up = False
                Standing = True
                WalkAmount = 0
            PlayerPos = [x,y]

    

    redrawWindow()
    dropEnemies(enemyList)
    score = updateEnemyPos(enemyList, score)
    speed = setLevel(score,speed)


    
    text = "score:" + str(score)
    label = myfont.render(text, 1, red)
    gameDisplay.blit(label, (width-200, height-40))
    
    if collisionCheck(enemyList, PlayerPos):
        gameRunning = False
        break
    
    drawEnemies(enemyList)
    #clock.tick(60)


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

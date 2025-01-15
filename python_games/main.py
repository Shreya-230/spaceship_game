import pygame
import random
import math
#Initialize the pygame
pygame.init()

#Create the screen
screen=pygame.display.set_mode((800,600))

#Background
background=pygame.image.load('background.png')

#Title and Icon
pygame.display.set_caption("SPACE INVADERS")
icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#PLAYER
playerImg=pygame.image.load("aircraft.png")
#see screen ka size is defined as X=800 and Y=600 and playerX is half of screen i.e. 370 and along y coordinate it is almost at the bottom at location 480...
playerX = 370
playerY = 480
playerX_change=0

#ENEMY
#Trying to make multiple enemeies
enemyImg=[]
#Enemy is getting located randomly
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("alien4.png"))
    enemyX.append(random.randint(0,800))
    enemyY.append(random.randint(50,150))#4,40
    enemyX_change.append(2)
    enemyY_change.append(35)


#BULLET
#Ready - You can't see the bullet on screen
#Fire= The bullet is currently moving
bulletImg=pygame.image.load("bullet.png")
bulletX=0
bulletY=480
bulletX_change=4
bulletY_change=40
bullet_state="ready"

# score=0 
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)

textX=10
textY=10

def show_score(x,y):
    score=font.render("Score :"+ str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def player(x,y):
    screen.blit(playerImg,(x,y))#now these values of x and y will be used

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))

#Collison Detection
def isCollison(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt((math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2)))
    if distance<27:
        return True
    else:
        return False
    
#Game Loop
running =True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quit event trigerred!")
            running=False
#If keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            print("A Keystroke is pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -5
                print("Left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
                print("Right arrow is pressed")
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
#Get the current x coordinate of spaceship
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)     
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Keystroke has been released")
                playerX_change = 0
#KEYUP -> means releasing of key
#KEYDOWN -> means pressing of key
#pressing of close button is also ans event in pygame , therefore due to absence of quit functionality the system was hanging

#****RGB => red green blue*****
    screen.fill((0,0,0))
#******BACKGROUND IMAGE********
#Due to addition of heavy background image of 248kb the aircraft and enemy are moving slowly as it is taking time to load the background image thus causing while loop to run slowly
    screen.blit(background,(0,0))

#*********MOVEMENT MECHANISM*********
    # playerX+=0.1#oh cool this is showing aircraft movement in x-axis
    # '+' is showing movement in right dir
    # playerX-=0.1# '-' is showing movement in left direction
    # playerY-=0.1 #shows movement in upwards direction
    # playerY+=0.1 #shows movement in down dir
#***** We need to add keyboard control to our game so that it works according to keyboard input controls and key pressed events*******
#***** Any kind of keyboard pressing or keystroke event is also considered as an event ******


#****DECISION BOUNDARY FOR PLAYER******
    playerX+=playerX_change
    if playerX<0:
        playerX=0
    elif playerX>=736:
        playerX=736
#*****DECISION BOUNDARY FOR ENEMY
#checking for boundaries so that doesn't goes out of bound****** 
    for i in range(num_of_enemies):
        enemyX[i]+=enemyX_change[i]
        if enemyX[i]<=0:
            enemyX[i]=4
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i]>=736:
            enemyX_change[i]=-4
            enemyY[i]+=enemyY_change[i]
        #********COLLISON*********
        collison=isCollison(enemyX[i],enemyY[i],bulletX,bulletY)
        if collison:
            bulletY=480
            bullet_state="ready"
            score_value+=1
            print("Score is",score_value)
            enemyX[i]=random.randint(0,735)
            enemyY[i]=random.randint(50,150)
        enemy(enemyX[i],enemyY[i],i)

    # print(playerX)

#BULLET  MOVEMENT
    if bulletY<0:
        bulletY=480
        bullet_state="ready"
#Due to this statement the bullet was fired continuosly
    
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change

     
    player(playerX,playerY)
    show_score(textX,textY)
#Player should be called after screen function ,this is because initially screen should be made then players come
    pygame.display.update()
#Display means game window on which you are working on..

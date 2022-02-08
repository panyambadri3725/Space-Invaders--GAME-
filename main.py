import pygame
import random
import math
pygame.init()
screen=pygame.display.set_mode((800,600))
run=True
pygame.display.set_caption("badris 1st game")
icon=pygame.image.load("alien.png")
backimg=pygame.image.load("backimage.png")
pygame.display.set_icon(icon)
playerimg=pygame.image.load("spaceship.png")

bulletimg=pygame.image.load("bullet.png")
playerx=370
playery=520
pxchange=0
#pychange=0
bulletx=0
bullety=480
bcx=0
bcy=10
bulletstate="ready"
score=0
def bullet(x,y):
    global bulletstate
    bulletstate="fire"
    screen.blit(bulletimg, (x, y+10))
enemyimg=[]
enemyx=[]
enemyy=[]
ecx=[]
ecy=[]
n=6
for i in range(n):
    enemyimg .append(pygame.image.load("enemy.png"))
    enemyx.append(random.randint(0,736))
    enemyy.append(random.randint(50,150))
    ecx.append(3)
    ecy.append(0)
font=pygame.font.Font("freesansbold.ttf",26)
gameoverfont=pygame.font.Font("freesansbold.ttf",64)
def gameovertext():
    game= gameoverfont.render("GAME OVER ", True, (255, 0, 0))
    screen.blit(game,(200,200))

textx=10
texty=10
def showscore(x,y):
     scor=font.render("The Score is "+str(score),True,(255,255,255))
     screen.blit(scor,(x,y))
def player(x,y):
    screen.blit(playerimg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x, y))
def iscollision(enemyx,enemyy,bulletx,bullety):
    dist=math.sqrt(pow(enemyx-bulletx,2)+pow(enemyy-bullety,2))
    if dist < 27:
        return True

while run:
    screen.fill((0, 0, 0))
    screen.blit(backimg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                pxchange=-2
                #print("LEFT")
            if event.key == pygame.K_RIGHT:
                pxchange=2
            bulletx=playerx
            if event.key == pygame.K_SPACE:
                bullet(bulletx,bullety)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT:
                pxchange=0
    if bullety<=0:
        bullety=480
        bulletstate="ready"
    if bulletstate=="fire":
        bullet(bulletx,bullety)
        bullety-=bcy
    for i in range(n):
        if enemyy[i] > 400:

            for j in range(n):

                enemyy[j]=4000
                print(j)
                gameovertext()
                showscore(260,300 )
            break
        enemyx[i] += ecx[i]

        if enemyx[i] >=734:
            #enemyx[i]=734
            ecx[i]=-3
            enemyy[i]+=30
        if enemyx[i]<=0:
            #enemyx=0
            ecx[i]=3
            enemyy[i]+=30
        collision=iscollision(enemyx[i],enemyy[i],bulletx,bullety)
        if collision:
            bullety=480
            bulletstate="ready"
            score +=1
            enemyx[i]=random.randint(0,736)
            enemyy[i]=random.randint(50,150)
        enemy(enemyx[i],enemyy[i],i)

    if playerx<=0:
        playerx=0
    if playerx>=734:
        playerx=734

    showscore(textx,texty)
    playerx+=pxchange
    player(playerx, playery)


    pygame.display.update()


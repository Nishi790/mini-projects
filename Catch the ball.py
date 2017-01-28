import pygame, sys, random

from pygame.locals import *

pygame.init()

    
screen=pygame.display.set_mode((640,640))
pygame.display.set_caption('Trap the Balls')
ball1x=random.randint(0,640)
ball1y=random.randint(0,640)
speedx1=1
speedy1=1
draw1=True

ball2x=random.randint(0,640)
ball2y=random.randint(0,640)
speedx2=1
speedy2=1
draw2=True

while True:
    screen.fill((0,0,0))

    ball1x=ball1x+speedx1
    if ball1x>=640:
       speedx1=-speedx1
       ball1x=615
    elif ball1x<=0:
        speedx1=-speedx1
        ball1x=25
    ball1y=ball1y+speedy1
    if ball1y>=640:
        speedy1=-speedy1
        ball1y=615
    elif ball1y<=0:
        speedy1=-speedy1
        ball1y=25

    ball2x=ball2x+speedx2
    if ball2x>=640:
       speedx2=-speedx2
       ball2x=615
    elif ball2x<=0:
        speedx2=-speedx2
        ball2x=25
    ball2y=ball2y+speedy2
    if ball2y>=640:
        speedy2=-speedy2
        ball12=615
    elif ball2y<=0:
        speedy2=-speedy2
        ball2y=25

    if draw1:
        rect1=pygame.draw.circle(screen,(0,255,0),[ball1x,ball1y],25)
    if draw2:
        rect2=pygame.draw.circle(screen,(255,0,0),[ball2x,ball2y],50)

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==MOUSEBUTTONDOWN:
            if rect1.collidepoint(event.pos):
                draw1=False
            if rect2.collidepoint(event.pos):
                draw2=False

    if (not draw1 and not draw2):
        font=pygame.font.Font(pygame.font.get_default_font(),32)
        message=font.render("You win!", False, (255,255,255))
        screen.blit(message,(320,300))
    
    pygame.display.update()

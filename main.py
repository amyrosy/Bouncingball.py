import sys
import pygame

pygame.init()
speed = [1, 1]
background = pygame.image.load('background.jpg')
scorefont=pygame.font.Font('googlebold.ttf',64)
screen = pygame.display.set_mode((800, 600))
icon = pygame.image.load('ball.png')
pygame.display.set_icon(icon)
def game_over():
    gameovervalue= scorefont.render("BOUNCING BALL", True, (235, 255, 200))
    screen.blit(gameovervalue, (140,235))


#player image positioning
line = pygame.image.load('line.png')
playerX = 370
playerY = 480
change = 0
#ball
pygame.display.set_caption("Bouncing ball")
ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
font=pygame.font.Font('googlebold.ttf',32)




#player
def player(x, y):
    screen.blit(line, (x, y))

#Screen Run
while True:
    screen.blit(background, (0, 0))
    game_over()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right >800:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom>600:
        speed[1] = -speed[1]

    #SCREEN DISPLAY
    player(playerX, playerY)
    screen.blit(ball, ballrect)
    pygame.display.flip()
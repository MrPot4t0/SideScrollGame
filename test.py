import pygame
import sys
from time import sleep

class colors():
    black = (0,0,0)
    white = (255,255,255)
    green = (0,255,0)
    red = (255,0,0)
    blue = (0,0,255)
    gray = (50,50,50)

screen_width = 800
screen_height = 600
pygame.init()
pygame.display.set_caption("PYGAME GAME :D")
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
bg = pygame.image.load("resources\\Forest.jpg").convert()
EE = pygame.image.load("resources\\personajes\\Knight.png")
ancho = 70
alto = 80
player = pygame.transform.scale(EE, (ancho,alto))


player_x_position = 50
player_y_position = 450
cord_x = 50
cord_y = 50
speed = 5

isjump = False
JumpCount = 10

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(True)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_x_position > speed:
        player_x_position -= speed
    if keys[pygame.K_RIGHT] and player_x_position < screen_width - speed - ancho:
        player_x_position += speed
    if not(isjump):
        if keys[pygame.K_UP] and player_y_position > speed:
            pass
        if keys[pygame.K_DOWN] and player_y_position < screen_height - alto * 2:
            pass
        if keys[pygame.K_SPACE]:
            isjump = True
    else:
        if JumpCount >= -10:
            player_y_position -= (JumpCount * abs(JumpCount)) * 0.5
            JumpCount -= 1
        else:
            JumpCount = 10
            isjump = False

    screen.blit(bg, [0,0])

    #pygame.draw.rect(screen,colors.white,(cord_x,cord_y,20,20))
    screen.blit(player, [player_x_position,player_y_position])
    pygame.display.flip()



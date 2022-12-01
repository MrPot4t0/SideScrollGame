import pygame
import random

width = 800
heigth = 600
done = False
pygame.init()
pygame.display.set_caption("Monteando")
screen = pygame.display.set_mode((width,heigth))
bg_load = pygame.image.load("resources\\Forest.jpg")
bg = pygame.transform.scale(bg_load,(width,heigth))
coin_image = pygame.transform.scale(pygame.image.load("resources\\coin.png").convert(),(40,45))
JumpCount = 7
isjump = False
speed = 5
score = 0

coin_list = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        brute_load = pygame.image.load("resources\\coin.png").convert()
        self.image = pygame.transform.scale(brute_load,(25,30))
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        brute_load = pygame.image.load("resources\\personajes\\knight.png").convert()
        self.image = pygame.transform.scale(brute_load,(70,80))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()

class colors():
    black = (0,0,0)
    white = (255,255,255)
    green = (0,255,0)
    red = (255,0,0)
    blue = (0,0,255)
    gray = (50,50,50)

for i in range(10):
    coin = Coin()
    coin.rect.x = random.randrange(100,800)
    coin.rect.y = 487

    coin_list.add(coin)
    all_sprites.add(coin)

for p in range(1):
    player = Player()
    player.rect.x = 0
    player.rect.y = 440
    all_sprites.add(player)

while not done:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.rect.x > speed:
        player.rect.x -= speed
    if keys[pygame.K_RIGHT] and player.rect.x < width - speed - 70:
        player.rect.x += speed
    if not(isjump):
        if keys[pygame.K_UP] and player.rect.y > speed:
            pass
        if keys[pygame.K_DOWN] and player.rect.y < heigth - 80 * 2:
            pass
        if keys[pygame.K_SPACE]:
            isjump = True
    else:
        if JumpCount >= -7:
            player.rect.y -= (JumpCount * abs(JumpCount)) * 1
            JumpCount -= 1
        else:
            JumpCount = 7
            isjump = False

    coin_hit_list = pygame.sprite.spritecollide(player, coin_list, True)
    for item in coin_hit_list:
        score += 1

    screen.blit(bg,[0,0])
    screen.blit(coin_image, [10 , 10])
    all_sprites.draw(screen)
    font = pygame.font.Font("resources\\Fuentes\\Deutsch.ttf", 45)
    text = font.render(str(score), 1, colors.white)
    text2 = font.render('x',1, colors.white)
    screen.blit(text2, (53,9))
    screen.blit(text, (85,9))

    pygame.display.flip()
    


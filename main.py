import pygame

pygame.init()

screen_width = 800
screen_height = int(screen_width * 0.8)

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("monteando")

moving_left = False
moving_right = False
isjump = False
JumpCount = 4

#colors in RGB
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
gray = (50,50,50)

def draw_background():
    screen.fill(gray)

class Player(pygame.sprite.Sprite):
    def __init__(self, char_type , x, y,speed,):
        super().__init__()
        self.speed = speed
        self.direction = 1
        self.flip = False
        load = pygame.image.load('resources\entities\player\Knight.png')
        self.img = pygame.transform.scale(load, (70,80))
        self.rect = self.img.get_rect()
        self.rect.center = (x,y)
    
    def move(self, moving_left,moving_right):
        dx = 0
        dy = 0
        if moving_left:
            dx = -self.speed
            self.flip = False
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = True
            self.direction = 1
        
        self.rect.x += dx
        self.rect.y += dy
    def draw(self):
        screen.blit(pygame.transform.flip(self.img, self.flip ,False), self.rect)

player = Player('player',200,200,3)

x = 200
y = 200

Playing = True
while Playing:
    pygame.time.Clock().tick(60)
    draw_background()

    player.move(moving_left,moving_right)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Playing = False
        #if player plays key this happens
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_ESCAPE:
                Playing = False
        #if player stops pressing key this happen
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
    
    #keyboars events
    keys = pygame.key.get_pressed()

    if not(isjump):
        if keys[pygame.K_UP]:
            pass
        if keys[pygame.K_DOWN]:
            pass
        if keys[pygame.K_SPACE]:
            isjump = True
    else:
        if JumpCount >= -4:
            player.rect.y -= (JumpCount * abs(JumpCount)) * 3
            JumpCount -= 0.4
        else:
            JumpCount = 4
            isjump = False
    
    
    player.draw()

    pygame.display.update()
pygame.quit()
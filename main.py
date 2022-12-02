import pygame

pygame.init()

screen_width = 800
screen_height = int(screen_width * 0.8)
mc_width = 150
mc_heigth = 150
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
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        temp_list = []

        for i in range(12):
            load = pygame.image.load(f'resources\entities\{self.char_type}\\walking{i}.png')
            img = pygame.transform.scale(load, (mc_width,mc_heigth))
            temp_list.append(img)

        self.animation_list.append(temp_list)
        temp_list = []

        for i in range(1):
            load = pygame.image.load(f'resources\entities\{self.char_type}\\static.png')
            img = pygame.transform.scale(load, (mc_width,mc_heigth))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        self.img = self.animation_list[self.action][self.frame_index]
        self.rect = self.img.get_rect()
        self.rect.center = (x,y)
    
    def move(self, moving_left,moving_right):
        dx = 0
        dy = 0
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1
        
        self.rect.x += dx
        self.rect.y += dy

    def update_animation(self):
        ANIMATION_COOLDOWN = 120
        self.img = self.animation_list[self.action][self.frame_index]
        
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def update_action(self,new_action):
        #checks for action change
        if new_action != self.action:
            self.action = new_action
            #update de animation setting
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(pygame.transform.flip(self.img, self.flip ,False), self.rect)

player = Player('player',200,200,5)

x = 200
y = 200

Playing = True
while Playing:
    pygame.time.Clock().tick(60)
    
    #backgroud
    draw_background()
    #loads the animation images
    player.update_animation()
    #sets the player movement
    player.move(moving_left,moving_right)
    #display everything
    player.draw()

    #update player action
    if moving_left or moving_right:
        player.update_action(0)
    else:
        player.update_action(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Playing = False
        #if player press key this happens
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
    
    pygame.display.update()
pygame.quit()
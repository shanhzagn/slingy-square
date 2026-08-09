import pygame
from sys import exit

def position():
    player_rect = player.get_rect(center=(PX-CAMX,PY-CAMY))

def changexby(x):
    for i in range(abs(x)):
        if x > 0:
            PX = PX+1
            position()
            for platforms in Platform:
                if player.rect.colliderect(platforms.rect):
                    PY = PY+1
                    position()
                    for platforms in Platform:
                        if player.rect.colliderect(platforms.rect):
                            PY = PY-1
                            PX = PX-1
                            SPEEDX = round((SPEEDX/2),0)
        if x < 0:
            PX = PX-1
            position()
            for platforms in Platform:
                if player.rect.colliderect(platforms.rect):
                    PY = PY+1
                    position()
                    for platforms in Platform:
                        if player.rect.colliderect(platforms.rect):
                            PY = PY-1
                            PX = PX+1
                            SPEEDX = round((SPEEDX/2),0)
        position()

def changeyby(y):
    print("a")

def frame():
    if SPEEDX > 10:
        SPEEDX = SPEEDX-1
    elif SPEEDX > 5:
        SPEEDX = SPEEDX-0.5
    elif SPEEDX > 0:
        SPEEDX = SPEEDX-0.25
    if SPEEDX < -10:
        SPEEDX = SPEEDX+1
    elif SPEEDX < -5:
        SPEEDX = SPEEDX+0.5
    elif SPEEDX < 0:
        SPEEDX = SPEEDX+0.25
    if SPEEDY >= -12:
        SPEEDY = SPEEDY-1
    changexby(SPEEDX)
    changeyby(SPEEDY)
    CAMX = PX
    CAMY = PY

#variables
PX = -600
PY = 0
SPEEDY = 0
SPEEDX = 0
AIRTIME = 0
CAMX = 0
CAMY = 0
Time = 0
Timer = 0
xpos = 0
ypos = 0

ARC = 0

#player
player = pygame.Surface((54,54))
player.fill("blue")
player_rect = player.get_rect(center=(0,0))

pygame.init()
screen = pygame.display.set_mode((960,720))
pygame.display.set_caption("Slingy Square")
clock = pygame.time.Clock()

#platforms
class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h,colour):
        super().__init__()
        self.image = pygame.Surface((w,h))
        self.image.fill(colour)
        self.rect = self.image.get_rect(center=(x,y))

platforms = pygame.sprite.Group()

#platforms.add(Platform(()))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

pygame.display.update()
clock.tick(60)
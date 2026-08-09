import pygame
import math
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
    for i in range(abs(y)):
        if y > 0:
            PY = PY+1
            position()
            for platforms in Platform:
                if player.rect.colliderect(platforms.rect):
                    PY = PY-1
                    SPEEDY = 0
        if y < 0:
            PY = PY-1
            position()
            for platforms in Platform:
                if player.rect.colliderect(platforms.rect):
                    costume = 1
                    AIRTIME = 0
                    PY = PY-1
                    SPEEDY = 0
        position()

#def sling():
#    if costume != 3:
#        costume = costume+1
#        SPEEDX =

def frame():
    #player
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
costume = 3
distance = 0

ARC = []

pygame.init()
screen = pygame.display.set_mode((960,720))
pygame.display.set_caption("Slingy Square")
clock = pygame.time.Clock()

#player
player = pygame.Surface((54,54))
player.fill("blue")
player_rect = player.get_rect(center=(0,0))

#cursor
cursor = pygame.Surface((6,6))
cursor.fill("yellow")
cursor_rect = cursor.get_rect(center=(0,0))

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

    #background
    screen.fill("white")

    #cursor
    mouse_x, mouse_y = pygame.mouse.get_pos()
    distance = math.hypot(player_rect.centerx - mouse_x, player_rect.centery - mouse_y)

    #player
    if costume == 3:
        player.fill("red")
    elif costume == 2:
        player.fill("mediumpurple")
    elif costume == 1:
        player.fill("blue")

    ARC.clear()
    if AIRTIME > 4:
        while AIRTIME > 0:
            ARC.append(PY)

    pygame.display.update()
clock.tick(60)
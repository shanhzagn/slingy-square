import pygame
import math
from sys import exit

#variables
PX = -600
PY = 0
slingx = 0
slingy = 0
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
holding = False
slingcolour = "blue"

ARC = []

#functions
def position():
    global PX
    global PY
    global CAMX
    global CAMY
    global player_rect
    player_rect = player.get_rect(center=(PX-CAMX+480,PY-CAMY+360))

def changexby(x):
    global PX
    global PY
    global SPEEDX
    global SPEEDY
    for i in range(abs(x)):
        if x > 0:
            PX = PX+1
            position()
            for platform in p:
                if player_rect.colliderect(platform.rect):
                    PY = PY+1
                    position()
                    for platform in p:
                        if player_rect.colliderect(platform.rect):
                            PY = PY-1
                            PX = PX-1
                            SPEEDX = round((SPEEDX/2),0)
        if x < 0:
            PX = PX-1
            position()
            for platform in p:
                if player_rect.colliderect(platform.rect):
                    PY = PY+1
                    position()
                    for platform in p:
                        if player_rect.colliderect(platform.rect):
                            PY = PY-1
                            PX = PX+1
                            SPEEDX = round((SPEEDX/2),0)
        position()

def changeyby(y):
    global PY
    global costume
    global AIRTIME
    global SPEEDY
    for i in range(abs(y)):
        if y > 0:
            PY += 1
            position()
            for platform in p:
                if player_rect.colliderect(platform.rect):
                    PY -= 1
                    SPEEDY = 0
        if y < 0:
            PY -= 1
            position()
            for platform in p:
                if player_rect.colliderect(platform.rect):
                    costume = 1
                    AIRTIME = 0
                    PY -= 1
                    SPEEDY = 0
        position()

def sling():
    global costume
    global SPEEDX
    global SPEEDY
    if costume != 3:
        costume = costume+1
        SPEEDX = (round(slingx/8))*-1
        SPEEDY = (round(slingy/8))*-1
        if SPEEDX > 21:
            SPEEDX = 22
        if SPEEDY > 21:
            SPEEDY = 22
        if SPEEDX < -21:
            SPEEDX = -22
        if SPEEDY < -21:
            SPEEDY = -22

def frame():
    global SPEEDX
    global SPEEDY
    global CAMX
    global CAMY
    global PX
    global PY
    #player
    if SPEEDX > 10:
        SPEEDX -= 1
    elif SPEEDX > 5:
        SPEEDX -= 0.5
    elif SPEEDX > 0:
        SPEEDX -= 0.25
    if SPEEDX < -10:
        SPEEDX =+ 1
    elif SPEEDX < -5:
        SPEEDX += 0.5
    elif SPEEDX < 0:
        SPEEDX += 0.25
    if SPEEDY >= -12:
        SPEEDY += 1
    changexby(SPEEDX)
    changeyby(SPEEDY)
    CAMX = PX
    CAMY = PY

pygame.init()
screen = pygame.display.set_mode((960,720))
pygame.display.set_caption("Slingy Square")
clock = pygame.time.Clock()

#player
player = pygame.Surface((54,54))
player.fill("blue")
player_rect = player.get_rect(center=(0,0))

#cursor
cursor = pygame.Surface((12,12))
cursor.fill("darkorange")
cursor_rect = cursor.get_rect(center=(0,0))

#platforms
class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h,colour):
        super().__init__()
        self.image = pygame.Surface((w,h))
        self.image.fill(colour)
        self.rect = self.image.get_rect(center=(x,y))

p = pygame.sprite.Group()

p1 = Platform(100,100,100,100,"black")
p.add(p1)

while True:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            holding = True
        if event.type == pygame.MOUSEBUTTONUP:
            holding = False

        if holding:
            slingx = cursor_rect.centerx
            slingy = cursor_rect.centery
            pygame.draw.line(screen,(slingcolour),player_rect.center,cursor_rect.center,5)


     #background
     screen.fill("white")

     #cursor
     mouse_x, mouse_y = pygame.mouse.get_pos()
     distance = math.hypot(player_rect.centerx - mouse_x, player_rect.centery - mouse_y)
     cursor_rect = cursor.get_rect(center=(pygame.mouse.get_pos()))
     screen.blit(cursor,cursor_rect)

     #player
     if costume == 3:
         player.fill("red")
         slingcolour = "red"
     elif costume == 2:
         player.fill("mediumpurple")
         slingcolour = "mediumpurple"
     elif costume == 1:
         player.fill("blue")
         slingcolour = "blue"

     AIRTIME = AIRTIME+1
     frame()
     CAMX = round(PX+(SPEEDX*-1),0)
     CAMY = round(PY+(SPEEDY*-1),0)
     position()


     screen.blit(player,player_rect)

     ARC.clear()
     if AIRTIME > 4:
         while AIRTIME > 0:
             ARC.append(PY)

     pygame.display.update()
     clock.tick(60)
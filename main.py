import pygame
import math
from sys import exit

#variables
SPAWN_X = -600
SPAWN_Y = 0
PX = SPAWN_X
PY = SPAWN_Y

#playtesting
TEST_POINTS = {
    pygame.K_1: (-400,-2000),
    pygame.K_2: (200,-1900),
    #pygame.K_3: (),
    #pygame.K_4: (),
}
def teleport(x,y):
    global PX, PY, SPEEDX, SPEEDY, costume, AIRTIME
    PX,PY = x,y
    SPEEDX,SPEEDY = 0,0
    costume = 1
    AIRTIME = 0


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
costume = 1
distance = 0
draw_x = 0
draw_y = 0
holding = False
slingcolour = "blue"

#gravity tuning
GRAVITY = 1
TERMINAL_VELOCITY = 22

#functions
def position():
    global PX
    global PY
    global CAMX
    global CAMY
    global player_rect
    global world_rect
    player_rect = player.get_rect(center=(480,360))
    world_rect = player.get_rect(center=(PX,PY))

def changexby(x):
    global PX
    global PY
    global SPEEDX
    global SPEEDY
    for i in range(abs(int(x))):
        if x > 0:
            PX = PX+1
            position()
            for platform in p:
                if world_rect.colliderect(platform.rect):
                    PY = PY+1
                    position()
                    for platform in p:
                        if world_rect.colliderect(platform.rect):
                            PY = PY-1
                            PX = PX-1
                            SPEEDX = round((SPEEDX/2),0)
        if x < 0:
            PX = PX-1
            position()
            for platform in p:
                if world_rect.colliderect(platform.rect):
                    PY = PY+1
                    position()
                    for platform in p:
                        if world_rect.colliderect(platform.rect):
                            PY = PY-1
                            PX = PX+1
                            SPEEDX = round((SPEEDX/2),0)
        position()

def changeyby(y):
    global PY
    global costume
    global AIRTIME
    global SPEEDY
    for i in range(abs(int(y))):
        if y > 0:
            PY += 1
            position()
            for platform in p:
                if world_rect.colliderect(platform.rect):
                    PY -= 1
                    costume = 1
                    AIRTIME = 0
                    SPEEDY = 0
                    break
        if y < 0:
            PY -= 1
            position()
            for platform in p:
                if world_rect.colliderect(platform.rect):
                    PY += 1
                    SPEEDY = 0
                    break
        position()

def sling():
    global costume
    global SPEEDX
    global SPEEDY
    if costume != 3:
        costume = costume+1
        SPEEDX = (round((slingx/8),0))*-1
        SPEEDY = (round((slingy/8),0))*-1
        if SPEEDX > 35:
            SPEEDX = 36
        if SPEEDY > 35:
            SPEEDY = 36
        if SPEEDX < -35:
            SPEEDX = -36
        if SPEEDY < -35:
            SPEEDY = -36

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
        SPEEDX += 1
    elif SPEEDX < -5:
        SPEEDX += 0.5
    elif SPEEDX < 0:
        SPEEDX += 0.25
    if SPEEDY < -12:
        SPEEDY += 1
    SPEEDY += GRAVITY
    if SPEEDY > TERMINAL_VELOCITY:
        SPEEDY = TERMINAL_VELOCITY
    changexby(SPEEDX)
    changeyby(SPEEDY)

pygame.init()
screen = pygame.display.set_mode((960,720))
#screen = pygame.display.set_mode((1920,1440))
pygame.display.set_caption("Slingy Square")
clock = pygame.time.Clock()

#player
player = pygame.Surface((54,54))
player.fill("blue")
player_rect = player.get_rect(center=(0,0))
world_rect = player.get_rect(center=(0,0))

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

#border
p0 = Platform(0,0,700,200,"black")
p.add(p0)
p1 = Platform(-600,300,4000,500,"black")
p.add(p1)
p2 = Platform(1600,300,500,10000,"black")
p.add(p2)
p3 = Platform(-1600,300,500,10000,"black")
p.add(p3)

#level
p4 = Platform(0,0,500,500,"black")
p.add(p4)
p5 = Platform(1600,-600,700,100,"black")
p.add(p5)
p6 = Platform(1600,-1800,3000,100,"black")
p.add(p6)
p7 = Platform(0,-1100,500,100,"black")
p.add(p7)
p8 = Platform(-400,-1500,50,900,"black")
p.add(p8)
p9 = Platform(-450,-1075,100,50,"black")
p.add(p9)
p10 = Platform(-1590,300,500,3500,"black")
p.add(p10)
p11 = Platform(-330,-2100,50,100,"black")
p.add(p11)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if distance < 130:
                holding = True
        if event.type == pygame.MOUSEBUTTONUP:
            if holding:
                sling()
            holding = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                teleport(SPAWN_X,SPAWN_Y)
            elif event.key in TEST_POINTS:
                teleport(*TEST_POINTS[event.key])

    #background
    screen.fill("white")

    #player
    if costume == 3:
        player.fill("red")
        slingcolour = "orangered"
    elif costume == 2:
        player.fill("purple")
        slingcolour = "mediumpurple"
    elif costume == 1:
        player.fill("blue")
        slingcolour = "dodgerblue"

    AIRTIME += 1
    frame()
    CAMX = PX
    CAMY = PY
    position()

    #cursor
    mouse_x, mouse_y = pygame.mouse.get_pos()
    distance = math.hypot(player_rect.centerx - mouse_x, player_rect.centery - mouse_y)
    cursor_rect = cursor.get_rect(center=(pygame.mouse.get_pos()))
    screen.blit(cursor, cursor_rect)

    # blit player
    screen.blit(player, player_rect)

    #draw platforms
    for platform in p:
        draw_x = platform.rect.x - CAMX + 480
        draw_y = platform.rect.y - CAMY + 360
        screen.blit(platform.image,(draw_x,draw_y))

    # sling
    if holding:
        slingx = cursor_rect.centerx + CAMX - 480 - PX
        slingy = cursor_rect.centery + CAMY - 360 - PY
        pygame.draw.line(screen, (slingcolour), player_rect.center, cursor_rect.center, 20)

    pygame.display.update()
    clock.tick(60)
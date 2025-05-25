# do not put x,y coordinate on image load func
# put x,y coordinate on blit function instead to locate the pic

import pygame, random
pygame.font.init()
pygame.mixer.init() #allowing to load sounds
pygame.init()
WIDTH, HEIGHT=1024, 500
RW, RH = 200,200

screen=pygame.display.set_mode((WIDTH, HEIGHT))
title=pygame.display.set_caption("Paintball")
text=pygame.font.SysFont("ComicSans", 30)
background=pygame.image.load("checkerbg.png")
gun=pygame.image.load("revolver.png")
wall=pygame.image.load("wall.png")

background=pygame.transform.scale(background, (WIDTH, HEIGHT))
gun=pygame.transform.scale(gun, (RW, RH))

redhit=pygame.USEREVENT+1

speed=5

border=pygame.Rect(WIDTH/2-5, 0, 10, HEIGHT)
def handlegun(key_pressed, rev):
    if key_pressed [pygame.K_LEFT] and rev.x>0:
        rev.x-=speed
    if key_pressed [pygame.K_UP] and rev.y>0:
        rev.y-=speed
    if key_pressed [pygame.K_RIGHT] and rev.x<WIDTH-rev.width:
        rev.x+=speed
    if key_pressed [pygame.K_DOWN] and rev.y<HEIGHT-rev.height:
        rev.y+=speed

def handlebullets(bubbles, gun):
    for bubble in bubbles:
        bubble.x+=3
        if wall.colliderect(bubble):
            bubbles.remove(bubble)
            pygame.events.post(pygame.eventsEvent(redhit))
        elif bubble.x>WIDTH:
            bubbles.remove(bubble)

def displaywinner(winner):
    announce=text.render(winner,0, "green")
    screen.blit(announce, (WIDTH/2-announce.get_width()/2), HEIGHT/2)
    pygame.display.update()
    pygame.time.delay(2000) #Pause for 2 secs b4 closing window.
    
    
def draw(rev, wall, bullets):
    screen.blit(background, (0,0))
    pygame.draw.rect(screen, "pink", rev)
    screen.blit(gun, (rev.x, rev.y))
    pygame.draw.rect(screen, "black", border)
    screen.blit(wall, (WIDTH-400, HEIGHT/14))
    for i in bullets:
        pygame.draw.rect(screen, "white", i)
    pygame.display.update()

def play():
    rev=pygame.Rect(WIDTH/9, HEIGHT/2-60, 40, 10)
    run = True
    bullets=[]
    while run:
        for events in pygame.event.get():
            if events.type==pygame.QUIT:        #Close the window
                pygame.quit()
                break
            if events.type==pygame.KEYDOWN:
                if events.key==pygame.K_SPACE:
                    bullet=pygame.Rect(rev.x+rev.width, rev.y+rev.height, 10,5)
                    bullets.append(bullet)
        key_pressed=pygame.key.get_pressed()
        handlegun(key_pressed, rev)
        draw(rev, wall, bullets)
play()
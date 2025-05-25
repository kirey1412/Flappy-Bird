import pygame

from pygame.locals import *
pygame.init()

WIDTH, HEIGHT = 800, 900
ground_scroll=0
scroll_speed=2
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
background_img=pygame.image.load("bg.png")
ground_img=pygame.image.load("ground.png")
run = True
while run:
    screen.blit(background_img, (0,0))
    screen.blit(ground_img, (ground_scroll, 700))
    ground_scroll-=scroll_speed

    if ground_scroll<-100:
        ground_scroll=0
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
            run = False
    pygame.display.update()
pygame.quit()
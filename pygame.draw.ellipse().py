# Draw Ellipse

import pygame

pygame.init()
screen=pygame.display.set_mode((400,400))
pygame.display.set_caption("pygame draw()")
red = (255,0,0)

run = True 
while run:
    pygame.draw.ellipse(screen,red,(50,50,300,200))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
pygame.quit()
quit()

------------------------------------------------------------------------

import pygame

pygame.init()
screen=pygame.display.set_mode((400,400))
pygame.display.set_caption("pygame draw()")
red = (255,0,0)

run = True 
while run:
    pygame.draw.ellipse(screen,red,(50,50,300,200),50)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
pygame.quit()
quit()


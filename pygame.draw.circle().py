# Draw Circle

import pygame

pygame.init()
screen=pygame.display.set_mode((400,400))
pygame.display.set_caption("pygame draw()")
red = (255,0,0)

run = True 
while run:
    pygame.draw.circle(screen,red,(200,200),100)                          # draw.circle
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
pygame.quit()
quit()
 
#--------------------------------------------------------------------------------------

import pygame

pygame.init()
screen=pygame.display.set_mode((400,400))
pygame.display.set_caption("pygame draw()")
red = (255,0,0)

run = True 
while run:
    pygame.draw.circle(screen,red,(200,200),100,50)                      # draw.circle
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
pygame.quit()
quit()


# Draw Polygon

import pygame

pygame.init()
screen=pygame.display.set_mode((400,400))
pygame.display.set_caption("pygame draw()")
red = (255,0,0)

run = True 
while run:
    pygame.draw.polygon(screen,red,[(200,50),(300,100),(300,300),(200,350),(100,300),(100,100)])      # Draw Polygon
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
pygame.quit()
quit()


#----------------------------------------------------------------------------


import pygame

pygame.init()
screen=pygame.display.set_mode((400,400))
pygame.display.set_caption("pygame draw()")
red = (255,0,0)

run = True 
while run:
    pygame.draw.polygon(screen,red,[(200,50),(300,100),(300,300),(200,350),(100,300),(100,100)],20)    # Draw Polygon
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
pygame.quit()
quit()


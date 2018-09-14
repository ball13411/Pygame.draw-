# Draw Lines

import pygame

pygame.init()
screen=pygame.display.set_mode((400,400))
pygame.display.set_caption("pygame draw()")
red = (255,0,0)

run = True 
while run:
    pygame.draw.lines(screen, red, True, [(100,200), (300,200)])
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
pygame.quit()
quit()

#-----------------------------------------------------------------------------

import pygame

pygame.init()
screen=pygame.display.set_mode((400,400))
pygame.display.set_caption("pygame draw()")
red = (255,0,0)

run = True 
while run:
    pygame.draw.lines(screen, red, True, [(100,300), (300,300),(200,100)],5)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
quit()


#---------------------------------------------------------------------------------------


import pygame

pygame.init()
screen=pygame.display.set_mode((400,400))
pygame.display.set_caption("pygame draw()")
red = (255,0,0)

run = True 
while run:
    pygame.draw.lines(screen, red, True, [(100,300), (300,300),(100,100),(300,100)],5)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
pygame.quit()
quit()


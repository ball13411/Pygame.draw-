
# coding: utf-8

# In[1]:


import pygame

pygame.init()
screen=pygame.display.set_mode((400,400))
pygame.display.set_caption("pygame draw()")
red = (255,0,0)
pygame.draw.rect(screen,red,(100,100,200,200))
pygame.display.update()
run = True 
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
pygame.quit()
quit()


# In[ ]:


import pygame

pygame.init()
screen=pygame.display.set_mode((400,400))
pygame.display.set_caption("pygame draw()")
red = (255,0,0)
pygame.draw.rect(screen,red,(100,100,200,200),20)
pygame.display.update()
run = True 
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
pygame.quit()
quit()


# In[ ]:


import pygame

pygame.init()
screen=pygame.display.set_mode((400,400))
pygame.display.set_caption("pygame draw()")
red = (255,0,0)
pygame.draw.rect(screen,red,(100,100,200,200),200)
pygame.display.update()
run = True 
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
pygame.quit()
quit()


import pygame, sys

width = 640
height = 480

screen = pygame.display.set_mode((width, height))
screen.fill((255,0,0))
pygame.display.set_caption("Ciclo básico de pygame")

pygame.init()


gameOver = False
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            gameOver = True
            
    #tambien puede ser pygame.display.update()
    pygame.display.flip()
    
pygame.quit()
sys.quit()
            













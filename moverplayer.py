import pygame, sys
import random
from pygame.locals import *

class Runner():
    __customes = ('runner','runner2','runner3','runner4')
    
    
    def __init__(self, x=0, y=0):
        ixCustome = random.randint(0, 3)
        
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome]))
        #self.custome = pygame.image.load("images/runner.png")
        self.position = [x, y]
        self.name = ""
        
class Game():
   
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,480))
        pygame.display.set_caption("Carrera de bichos")
        self.background = pygame.image.load("images/background.png")
        
        self.runner = Runner(320, 240)

    def start(self):
        
        gameOver = False

        while not gameOver:
            #comprobación de los eventos.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        #Mover hacia arriba
                        self.runner.position[1] -= 10
                    elif event.key == K_DOWN:
                        #Mover hacia abajo
                        self.runner.position[1] += 10
                    elif event.key == K_LEFT:
                        #Mover hacia izquierda
                        self.runner.position[0] -= 10
                    elif event.key == K_RIGHT:
                        #Mover hacia derecha
                        self.runner.position[0] += 10
                    else:
                        pass

            #Refrescar y renderizar la pantalla
                        
            self.__screen.blit(self.background, (0,0))
            
            
            self.__screen.blit(self.runner.custome, self.runner.position)

            pygame.display.flip()
            

if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.start()










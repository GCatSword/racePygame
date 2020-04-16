import pygame
import sys
import random

class Runner():
    __customes = ('runner','runner2','runner3','runner4')
    
    
    def __init__(self, x=0, y=0):
        ixCustome = random.randint(0, 3)
        
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome]))
        #self.custome = pygame.image.load("images/runner.png")
        self.position = [x, y]
        self.name = ""
        
    def advance(self):
        self.position[0] += random.randint(1,6)
    
class Game():
    runners = []
    __posY = (160, 200, 240, 280)
    __names = ("Speedy", "Mia", "Rock", "Trek")
    
    __starLine = 5
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,480))
        pygame.display.set_caption("Carrera de bichos")
        self.background = pygame.image.load("images/background.png")
        
             
        for i in range(4):     
            theRunner = Runner(self.__starLine, self.__posY[i])
            theRunner.name = self.__names[i]
            self.runners.append(theRunner)
    
    def close(self):
        pygame.quit()
        sys.exit()
    
    def race(self):
        
        winner = False

        while not winner:
            #comprobación de los eventos.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #Refrescar y renderizar la pantalla
            for runner in self.runners:
                runner.advance()
                if runner.position[0] >= self.__finishLine:
                    print("The winner is {}".format(runner.name))
                    winner = True
            
            self.__screen.blit(self.background, (0,0))
            
            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)

            pygame.display.flip()
            
        while True:    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()

if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.race()









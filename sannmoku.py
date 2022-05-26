import pygame
from pygame.locals import *
import sys


def main():
    pygame.init()                                               
    screen = pygame.display.set_mode((300, 300))                
    pygame.display.set_caption("GAME")                          

    while (1):
        screen.fill((255,0,0))
        
        pygame.draw.line(screen, (0,95,0), (0,100), (300,100), 5) 
        pygame.draw.line(screen, (0,95,0), (0,200), (300,200), 5)
        pygame.draw.line(screen, (0,95,0), (100,0), (100,300), 5)
        pygame.draw.line(screen, (0,95,0), (200,0), (200,300), 5)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()

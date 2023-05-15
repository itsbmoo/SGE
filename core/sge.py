import pygame
import math
import numpy as np


class SimpleGraphicEngine:
    def __init__(self) -> None:
        self.window = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
    
    
    def plot(self) -> None:
        pass
    
    
if __name__ == '__main__':
    sge = SimpleGraphicEngine()
    while True:
        sge.clock.tick(60)
        sge.window.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()

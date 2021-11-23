import random

import pygame
from pygame.math import Vector2

class planetes:
    def __init__(self):
        self.rayon = 20
        self.couleur = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.position =(Vector2(random.randint(0,100),random.randint(0,100))*self.position
        self.masse = (random.randint(0,10))

    def draw(self, screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)


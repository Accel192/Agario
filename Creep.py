import random

import pygame
from pygame.math import Vector2

class Creep:
    def __init__(self):
        self.rayon = 10
        self.couleur = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.position = Vector2(random.randint(0,1000),random.randint(0,1000))

        self.nom = "creep1"

    def dead(self):
        self.nom
        pass

    def draw(self,screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)



import random

import pygame
from pygame.math import Vector2

class ennemie:
    def __init__(self):
        self.rayon = 50
        self.couleur = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.position = Vector2(random.randint(0,1500),random.randint(0,1500))
        self.nom = "ennemie"
        self.masse = 10
        self.gravity_X = 2
        self.gravity_Y = 2

    def dead(self):
        self.nom
        pass




    def draw(self,screen):
        self.position(self.position.x + self.gravity_X, self.position.y + self.gravity_Y)
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)


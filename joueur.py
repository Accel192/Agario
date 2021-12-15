import random

import pygame
from pygame.math import Vector2

class joueur :
    def __init__(self):
        self.rayon = 150
        self.couleur = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.position = Vector2(random.randint(0,1000),random.randint(0,1000))
        self.vitesse = Vector2()
        self.nom = "joueur"
        self.masse = 10

    def move
       if core.getMouseLeftClick():
            core.memory("click")core.getMouseLeftClick())

    pass

    def draw(self,screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)


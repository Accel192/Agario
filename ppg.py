from pygame.math import Vector2

import core
import pygame
import random
import math

#Variable Globale
from Creep import Creep


def setup():
    print("Setup START---------")

    core.fps = 30
    core.WINDOW_SIZE = [1000, 1000]

    core.memory("centredecercle", pygame.Vector2(200, 200))
    core.memory("rayonducercle", 10)
    core.memory("couleurducercle", (255, 255, 255))
    core.memory("vitesse",  pygame.Vector2(0, 0))
    core.memory("PS", pygame.Vector2(0, 0))
    core.memory("k", 0.01)
    core.memory("l0", 1)
    core.memory("gravity_x", 0)
    core.memory("gravity_y", 0)
    core.memory("pos_souris",pygame.Vector2(0, 0))
    core.memory("creep",100)
    core.memory("tablecreep", [])
    core.memory("ennemie", [])


    for i in range(1000):
        core.memory("tablecreep").append(Creep())

    print("Setup END-----------")

def run():

    core.cleanScreen()

    for c in core.memory("tablecreep"):
        c.draw(core.screen)





core.main(setup, run)


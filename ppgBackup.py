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
    core.WINDOW_SIZE = [400, 400]

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
    core.memory("ennemie")
    core.memory("tablecreep", [])

    for i in range(100):
        core.memory("tablecreep").append(Creep())

    print("Setup END-----------")

def run():

    core.cleanScreen()

    #core.memory("couleurducercle", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    pygame.draw.circle(core.screen, core.memory("couleurducercle"), core.memory("centredecercle"), core.memory("rayonducercle"))
    core.memory("centredecercle", pygame.Vector2(core.memory("centredecercle").x + core.memory("gravity_x"), core.memory("centredecercle").y + core.memory("gravity_y")))

#Souris
    if core.getMouseLeftClick() is not None:

        core.memory("pos_souris", pygame.Vector2(core.getMouseLeftClick()[0], core.getMouseLeftClick()[1]))

        core.memory("PS", pygame.Vector2(core.memory("pos_souris").x - core.memory("centredecercle").x, core.memory("pos_souris").y - core.memory("centredecercle").y))

        core.memory("l", core.memory("PS").length())
        core.memory("u", core.memory("PS").normalize())

        core.memory("Fr", core.memory("k") * abs(core.memory("l") - core.memory("l0")) * core.memory("u"))
        print("Fr", core.memory("Fr"))
        core.memory("vitesse",core.memory("vitesse")+core.memory("Fr"))

    core.memory("centredecercle", core.memory("centredecercle") + core.memory("vitesse"))

    print(core.getkeyPressValue())





#Hors limite Y
    if core.memory("centredecercle").y > core.WINDOW_SIZE[1] - core.memory("rayonducercle"):
        core.memory("gravity_y", -5)
        core.memory("vitesse", core.memory("vitesse") - core.memory("vitesse"))

        core.memory("couleurducercle", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    if core.memory("centredecercle").y < core.WINDOW_SIZE[0] - core.WINDOW_SIZE[0] + core.memory("rayonducercle"):
       core.memory("gravity_y", 5)
       core.memory("vitesse", core.memory("vitesse") - core.memory("vitesse"))
       core.memory("couleurducercle", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

# Hors limite X
    if core.memory("centredecercle").x > core.WINDOW_SIZE[0] - core.memory("rayonducercle"):
        core.memory("gravity_x", -5)
        core.memory("vitesse", core.memory("vitesse") - core.memory("vitesse"))
        core.memory("couleurducercle", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    if core.memory("centredecercle").x < core.WINDOW_SIZE[0] - core.WINDOW_SIZE[0] + core.memory("rayonducercle"):
        core.memory("gravity_x", 5)
        core.memory("vitesse", core.memory("vitesse") - core.memory("vitesse"))
        core.memory("couleurducercle", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

#Reset
    if core.getKeyPressList(pygame.K_r) :
        core.memory("centredecercle", pygame.Vector2(200, 200))
        core.memory("gravity_x", 0)
        core.memory("gravity_y", 0)
        core.memory("vitesse", Vector2(0, 0))
        print("reset")

#Up
    if core.getKeyPressList(pygame.K_z):
        core.memory("gravity_y", -5)
        print("up")
#Down
    if core.getKeyPressList(pygame.K_s):
        core.memory("gravity_y", 5)
        print("down")

# Right
    if core.getKeyPressList(pygame.K_d):
        core.memory("gravity_x", 5)
        print("right")

# Left
    if core.getKeyPressList(pygame.K_q):
        core.memory("gravity_x", -5)
        print("left")

#Creep
    for i in range (100):
        draw.circle


core.main(setup, run)


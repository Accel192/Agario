
#Variable Globale
import pygame
from pygame.math import Vector2

import core
from Creep import Creep
from ennemie import ennemie


def setup():
    print("Setup START---------")

    core.fps = 30
    core.WINDOW_SIZE = [1500, 800]



    core.memory("centredecercle", pygame.Vector2(200, 200))
    core.memory("rayonducercle", 50)
    core.memory("couleurducercle", (255, 255, 255))
    core.memory("vitesse", pygame.Vector2(0, 0))
    core.memory("gravity_x", 0)
    core.memory("gravity_y", 0)
    core.memory("tablecreep", [])
    core.memory("tableennemie", [])

    # Creep
    for creep in range(100):
        core.memory("tablecreep").append(Creep())

    # ennemie
    for creep in range(10):
        core.memory("tableennemie").append(ennemie())



    print("Setup END-----------")



def run(self=None):

#Variable Local creep
    core.cleanScreen()

    for c in core.memory("tablecreep"):
        c.draw(core.screen)


#Variable Local ennemie
    core.cleanScreen()

    for c in core.memory("tableennemie"):
        c.draw(core.screen)


    core.cleanScreen()

    pygame.draw.circle(core.screen, core.memory("couleurducercle"), core.memory("centredecercle"), core.memory("rayonducercle"))

    core.memory("centredecercle", pygame.Vector2(core.memory("centredecercle").x + core.memory("gravity_x"),
    core.memory("centredecercle").y + core.memory("gravity_y")))








# Souris
    if core.getMouseLeftClick() is not None:


        core.memory("PS", pygame.Vector2(0, 0))
        core.memory("k", 0.001)
        core.memory("l0", 1)
        core.memory("u", 0)
        core.memory("pos_souris", pygame.Vector2(0, 0))

# souris
        core.memory("pos_souris", pygame.Vector2(core.getMouseLeftClick()[0], core.getMouseLeftClick()[1]))

# Vecteur pos_souris - pos_cercle
        core.memory("PS", pygame.Vector2(core.memory("pos_souris").x - core.memory("centredecercle").x,
                                         core.memory("pos_souris").y - core.memory("centredecercle").y))
# Norme vecteur PS
        core.memory("l", core.memory("PS").length())

# Longueur vecteur PS
        core.memory("u", core.memory("PS").normalize())

#Calcul Force finale
        core.memory("Fr", core.memory("k") * abs(core.memory("l") - core.memory("l0")) * core.memory("u"))
        print("Fr", core.memory("Fr"))

#Vitesse = vitesse + force
        core.memory("vitesse", core.memory("vitesse") + core.memory("Fr"))

#pos_cercle = pos_cercle + vitesse
    core.memory("centredecercle", core.memory("centredecercle") + core.memory("vitesse"))

    print(core.getkeyPressValue())



    # Haut
    if core.getKeyPressList(pygame.K_z):
        core.memory("gravity_y", -5)
        print("up")
    # Bas
    if core.getKeyPressList(pygame.K_s):
        core.memory("gravity_y", 5)
        print("down")

    # Droite
    if core.getKeyPressList(pygame.K_d):
        core.memory("gravity_x", 5)
        print("right")

    # Gauche
    if core.getKeyPressList(pygame.K_q):
        core.memory("gravity_x", -5)
        print("left")


# Limite Y
    if core.memory("centredecercle").y > core.WINDOW_SIZE[1] - core.memory("rayonducercle"):
        core.memory("gravity_y", -5)
        core.memory("vitesse", core.memory("vitesse") - core.memory("vitesse"))


    if core.memory("centredecercle").y < core.WINDOW_SIZE[0] - core.WINDOW_SIZE[0] + core.memory("rayonducercle"):
        core.memory("gravity_y", 5)
        core.memory("vitesse", core.memory("vitesse") - core.memory("vitesse"))


# Limite X
    if core.memory("centredecercle").x > core.WINDOW_SIZE[0] - core.memory("rayonducercle"):
        core.memory("gravity_x", -5)
        core.memory("vitesse", core.memory("vitesse") - core.memory("vitesse"))


    if core.memory("centredecercle").x < core.WINDOW_SIZE[0] - core.WINDOW_SIZE[0] + core.memory("rayonducercle"):
        core.memory("gravity_x", 5)
        core.memory("vitesse", core.memory("vitesse") - core.memory("vitesse"))








core.main(setup, run)
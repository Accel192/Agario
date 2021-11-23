import random
import pygame
from pygame.math import Vector2
import core

from Planètes import planetes

def setup():

    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [1000, 1000]

    core.memory("couleursoleil",(240, 146, 0))
    core.memory("centredusoleil", (500,500))
    core.memory("rayondusoleil", 50)
    core.memory("tableplanetes", [])
    core.memory("gravity", 9.81)
    core.memory("massedusoleil", 30)

    for i in range(8):
        core.memory("tableplanetes").append(Planètes())

print("Setup END-----------")

def run ():

    core.cleanScreen()

    pygame.draw.circle(core.screen, core.memory("couleursoleil"), core.memory("centredusoleil"),core.memory("rayondusoleil"))


        for c in core.memory("tableplanetes"):
        c.draw(core.screen)

    core.memory("positionplanetes",)

    core.memory("attraction", core.memory("gravity")* (core.memory("massedusole")*))



core.main(setup, run)
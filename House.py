import pygame 

from PickableItems import CrimeEvidence
from Barriers import Furniture

class House:
    def __init__(self):
        self.floor = Floor()
        self.door = Door()
        self.crimeEvidence = CrimeEvidence()
        self.furniture = Furniture()

class Floor(pygame.sprite.Sprite):
    def __init__(self):
        pass

class Door(pygame.sprite.Sprite):
    def __init__(self):
        pass
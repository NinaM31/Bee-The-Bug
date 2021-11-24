import pygame 

from Furniture.PickableItems import CrimeEvidence
from Furniture.Barriers import Furniture

class House:
    def __init__(self, house_map):
        self.house_map = house_map
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
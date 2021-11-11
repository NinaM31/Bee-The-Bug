import pygame
from Objects import Objects

class Furniture(pygame.sprite.Sprite, Interactable):
    def __init__(self, passable):
        self.passable = passable

    def __passable(self):
        return self.passable
    
    def interact(self):
        pass

class Door(Furniture):
    def __init__(self):
        super().__init__(False)


class Light(Furniture):
    def __init__(self):
        super().__init__(True)
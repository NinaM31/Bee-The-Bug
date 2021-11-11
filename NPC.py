import pygame

class NPC(pygame.sprite.Sprite, Interactable):
    def __init__(self):
        pass

    def __passable(self):
        return False
    
    def interact(self):
        pass
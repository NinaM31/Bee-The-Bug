from abc import ABC, abstractmethod
import pygame

from Interactable import Interactable


class CrimeEvidence(pygame.sprite.Sprite, Interactable):
    def __init__(self):
        pass
    
    def __passable(self):
        return True
    
    def interact(self):
        pass

class Paper(ABC):
    def __init__(self):
        pass

class Book(Paper, CrimeEvidence):
    def __init__(self):
        pass

class Mail(Paper, CrimeEvidence):
    def __init__(self):
        pass

class Photo(CrimeEvidence):
    def __init__(self):
        pass
from abc import ABC, abstractmethod
import pygame


class Interactable(ABC):
    def __init__(self):
        pass

    def is_passable(self, obj):
        return obj.__passable()

    @abstractmethod
    def __passable(self):
        pass

    @abstractmethod
    def interact(self):
        pass
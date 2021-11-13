import pygame

from Components.Config import *
from Components.Menu import StartMenu, EndMenu, SettingsMenu

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIN_WIDTH, WIN_HEIGHT) )
        self.clock = pygame.time.Clock()
        self.running = True

        self.startMenue = StartMenu(self)
        self.endMenue = EndMenu(self)
        self.settingsMenue = SettingsMenu(self)

    def game_intro(self):
        self.startMenue.display()
    
    def new(self):
        pass

    def show_settings(self):
        self.settingsMenue.display()

    def start(self):
        pass

    def game_over(self):
        self.endMenue.display()
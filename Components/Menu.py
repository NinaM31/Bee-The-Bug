from abc import ABC, abstractmethod
import pygame

from Components.Config import *
from Components.Input import Button
from Components.Styles import draw_text

class Menu(ABC):
    def __init__(self, game, HEADER='', HOWTO='', CAPTION=''):
        self.HEADER = HEADER
        self.HOWTO = HOWTO
        self.game = game
        pygame.display.set_caption(CAPTION)
    
    def prompt(self, color):
        screen = self.game.screen
        screen.fill(color)

        w = screen.get_width()
        h = screen.get_height()

        draw_text(screen, TITLE, self.HEADER, w/2, h/4, WHITE)
        draw_text(screen, BODY, self.HOWTO, w/2, h/2, WHITE)

    def display(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.game.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_buttons()
                    
            self.prompt(DARKBLUE)
            self.animation()
            self.game.clock.tick(LOWFPS)
            pygame.display.update()

    @abstractmethod
    def check_buttons(self):
        pass

    @abstractmethod
    def animation(self):
        pass

class StartMenu(Menu):
    def __init__(self, game):
        super().__init__(
            game,
            'Bee The Bug', 
            'Arrows to move, Space to interact',
            'Introduction')
        
        self.PLAY = Button('Play', WHITE, BLACK, 10, 10)

    def check_buttons(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if self.PLAY.pressed(mouse_pos, mouse_pressed):
            pass

    def animation(self):
        pass

class EndMenu(Menu):
    def __init__(self, game):
        super().__init__(
            game,
            'FIN', 
            'Tell me detective, do you believe in luck?',
            'Nice Game')
        self.BACK = Button('Back', WHITE, BLACK, 10, 10)

    def check_buttons(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if self.BACK.pressed(mouse_pos, mouse_pressed):
            pass

    def animation(self):
        pass

class SettingsMenu(Menu):
    def __init__(self, game):
        super().__init__(game, 'Settings', CAPTION='Settings')

        self.SOUND = Button('Sound', WHITE, BLACK, 10, 10)
        self.CONTINUE = Button('Continue', WHITE, BLACK, 10, 10)
        self.BACK = Button('Back', WHITE, BLACK, 10, 10)

    def check_buttons(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if self.SOUND.pressed(mouse_pos, mouse_pressed):
            pass
        if self.CONTINUE.pressed(mouse_pos, mouse_pressed):
            pass
        if self.BACK.pressed(mouse_pos, mouse_pressed):
            pass

    def animation(self):
        pass

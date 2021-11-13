from abc import ABC, abstractmethod
import pygame

from Components.Config import LOWFPS, WHITE, DARKBLUE, TITLE, BODY
from Components.Input import Button
from Components.Styles import draw_text

class Menu(ABC):
    def __init__(self, game, HEADER='', HOWTO='', CAPTION=''):
        self.HEADER = HEADER
        self.HOWTO = HOWTO
        self.game = game
        self.screen = game.screen
        self.w = game.screen.get_width()
        self.h = game.screen.get_height()

        pygame.display.set_caption(CAPTION)
    
    def prompt(self, color):
        self.screen.fill(color)

        draw_text(self.screen, TITLE, self.HEADER, self.w/2, self.h/4, WHITE)
        draw_text(self.screen, BODY, self.HOWTO, self.w/2, self.h/2, WHITE)

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
            self.draw(self.screen)
            self.animation()
            self.game.clock.tick(LOWFPS)
            pygame.display.update()

    @abstractmethod
    def check_buttons(self):
        pass

    @abstractmethod
    def animation(self):
        pass
    
    @abstractmethod
    def draw(self, screen):
        pass

class StartMenu(Menu):
    def __init__(self, game):
        super().__init__(
            game,
            'Bee The Bug', 
            'Arrows to move, Space to interact',
            'Introduction')

        self.PLAY = Button('Play', 100, 50, c_mid=True)

    def check_buttons(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        
        self.PLAY.hovered(mouse_pos)
        if self.PLAY.pressed(mouse_pos, mouse_pressed):
            print('pressed')
    
    def draw(self, screen):
        self.PLAY.draw_button(screen)

        mouse_pos = pygame.mouse.get_pos()
        self.PLAY.hovered(mouse_pos)

    def animation(self):
        pass

class EndMenu(Menu):
    def __init__(self, game):
        super().__init__(
            game,
            'FIN', 
            'Tell me detective, do you believe in luck?',
            'Nice Game')
        self.BACK = Button('Back', 100, 50, c_mid=True)

    def check_buttons(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if self.BACK.pressed(mouse_pos, mouse_pressed):
            print('pressed')
    
    def draw(self, screen):
        self.BACK.draw_button(screen)
        mouse_pos = pygame.mouse.get_pos()
        self.BACK.hovered(mouse_pos)

    def animation(self):
        pass

class SettingsMenu(Menu):
    def __init__(self, game):
        super().__init__(game, 'Settings', CAPTION='Settings')

        self.SOUND = Button('Sound', 100, 50, c_right=True)
        self.CONTINUE = Button('Continue', 100, 50, c_mid=True)
        self.BACK = Button('Back', 100, 50, c_left=True)

    def check_buttons(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if self.SOUND.pressed(mouse_pos, mouse_pressed):
            pass
        if self.CONTINUE.pressed(mouse_pos, mouse_pressed):
            pass
        if self.BACK.pressed(mouse_pos, mouse_pressed):
            pass
    
    def draw(self, screen):
        self.BACK.draw_button(screen)
        self.CONTINUE.draw_button(screen)
        self.SOUND.draw_button(screen)

        mouse_pos = pygame.mouse.get_pos()
        self.SOUND.hovered(mouse_pos)
        self.CONTINUE.hovered(mouse_pos)
        self.BACK.hovered(mouse_pos)

    def animation(self):
        pass

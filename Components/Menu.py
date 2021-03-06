from abc import ABC, abstractmethod
import pygame

from Components.Config import LOWFPS, PINK, BLACK, WHITE, TITLE, BODY
from Components.Input import Button
from Components.Styles import draw_text
from helper import resource_path

class Menu(ABC):
    def __init__(self, game, HEADER='', HOWTO='', CAPTION=''):
        self.HEADER = HEADER
        self.HOWTO = HOWTO
        
        self.game = game
        self.screen = game.screen
        self.w = game.screen.get_width()
        self.h = game.screen.get_height()

        pygame.display.set_caption(CAPTION)

    def load_audio(self):
        pygame.mixer.music.load(resource_path(self._audio))

    def start_sound(self):
        pygame.mixer.music.play(-1)

    def stop_audio(self):
        pygame.mixer.music.stop()

    def prompt(self):
        draw_text(self.screen, TITLE, self.HEADER, self.w/2, self.h/6, self.fg_color)
        draw_text(self.screen, BODY, self.HOWTO, self.w/2, self.h/2, self.fg_color)

    def display(self):
        self.waiting = True
        while self.waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.waiting = False
                    self.game.close_game()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_buttons()

            self.animation() 
            self.prompt()
            self.draw(self.screen)
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
    
    @abstractmethod
    def load_assets(self):
        pass

class StartMenu(Menu):
    def __init__(self, game):
        super().__init__(
            game,
            'Bee The Bug', 
            'Arrows to move, Space to interact',
            'Introduction')

        self.PLAY = Button('Play', 100, 50, c_m=True)
        self.fg_color = BLACK

        self.background = pygame.image.load(resource_path('assets/intro.png')).convert()
        self._audio = "assets/audio/intro.mp3"

    def check_buttons(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        
        if self.PLAY.pressed(mouse_pos, mouse_pressed):
            self.stop_audio()
            self.waiting = False
    
    def draw(self, screen):
        self.PLAY.draw_button(screen)
        mouse_pos = pygame.mouse.get_pos()
        self.PLAY.hovered(mouse_pos)

    def animation(self):
        self.game.screen.blit(self.background, (0,0))

    def load_assets(self):
        self.load_audio()
        self.start_sound()
        
class EndMenu(Menu):
    def __init__(self, game):
        super().__init__(
            game,
            'FIN', 
            'Tell me detective, do you believe in luck?',
            'Nice Game')

        self.END = Button('Back to Start', 170, 50, c_m=True)
        self.fg_color = WHITE

        self.background = pygame.image.load(resource_path('assets/end.png')).convert()
        self._audio = "assets/audio/end.mp3"

    def check_buttons(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if self.END.pressed(mouse_pos, mouse_pressed):
            pygame.mixer.music.stop()
            self.waiting = False
    
    def draw(self, screen):
        self.END.draw_button(screen)

        mouse_pos = pygame.mouse.get_pos()
        self.END.hovered(mouse_pos)

    def animation(self):
        self.game.screen.blit(self.background, (0,0))

    def load_assets(self):
        self.load_audio()
        self.start_sound()
import random
import pygame 

from Components.Config import WHITE, BERRY, GOLD, DARKBLUE, BODY, WIN_WIDTH, WIN_HEIGHT
from Components.Styles import Spritesheet


class Button:
    def __init__(self, txt, w, h, x=0, y=0, c_l=False, c_m=False, c_r=False, fg=WHITE, bg=BERRY, bg_hvr=GOLD):
        self.txt = txt
        self.bg = bg
        self.bg_hvr = bg_hvr
        self.fg = fg

        self.font = pygame.font.Font(None, BODY)

        self.image = pygame.Surface( (w, h), pygame.SRCALPHA)
        self.image.fill(self.bg)
        self.image_rect = self.image.get_rect()

        if not self.center(c_l, c_m, c_r):
            self.image_rect.x = x
            self.image_rect.y = y

        self.text  = self.font.render(txt, True, fg)
        self.text_rect = self.text.get_rect(center=(w/2, h/2) )
        
        self.image.blit(self.text, self.text_rect)
        self.click_audio = pygame.mixer.Sound("assets/audio/click.mp3")
        self.click_audio.set_volume(0.1)
    
    def center(self, c_l, c_m, c_r):
        if c_l: self.center_left()
        elif c_m: self.center_mid()
        elif c_r: self.center_right()

        return c_l or c_m or c_r
        
    def center_mid(self):
        x = WIN_WIDTH/2
        y = WIN_HEIGHT - WIN_HEIGHT/3
        self.image_rect.center = (x, y)
    
    def center_left(self):
        x = WIN_WIDTH/6
        y = WIN_HEIGHT - WIN_HEIGHT/3
        self.image_rect.midleft = (x, y)

    def center_right(self):
        x = WIN_WIDTH - WIN_WIDTH/6
        y = WIN_HEIGHT - WIN_HEIGHT/3
        self.image_rect.midright = (x, y)

    def hovered(self, mouse_pos):
        if self.image_rect.collidepoint(mouse_pos):
            self.image.fill(self.bg_hvr)
        else:
            self.image.fill(self.bg)
        self.image.blit(self.text, self.text_rect)

    def pressed(self, mouse_pos, mouse_pressed):
        if self.image_rect.collidepoint(mouse_pos):
            if mouse_pressed[0]: 
                self.click_audio.play(maxtime=500)
                return True
        return False

    def draw_button(self, screen):
        screen.blit(self.image, self.image_rect)

class Feedback(pygame.sprite.Sprite):
    def __init__(self, game, sprite, x, y):
        self.game = game
        self._layer = 10
        self.groups = sprite.groups
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.font = pygame.font.SysFont(None, 32)

        if isinstance(sprite.text, list):
            r = random.randint(0, len(sprite.text)-1)
            text = sprite.text[r]
        else:
            text = sprite.text

        self.textSurf = self.font.render(text, 1, DARKBLUE)
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()

        self.image = game.feedback_sprite.get_sprite(0, 0, WIN_WIDTH, 150)
        self.image.blit(self.textSurf, [WIN_WIDTH/2 - W/2, 150/2 - H/2])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
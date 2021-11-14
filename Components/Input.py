import pygame 

from Components.Config import WHITE, BERRY, PINK, BODY, WIN_WIDTH, WIN_HEIGHT
from Components.Styles import Spritesheet


class Button:
    def __init__(self, txt, w, h, x=0, y=0, c_l=False, c_m=False, c_r=False, fg=WHITE, bg=BERRY, bg_hvr=PINK):
        self.txt = txt
        self.bg = bg
        self.bg_hvr = bg_hvr
        self.fg = fg

        self.font = pygame.font.Font(None, BODY)

        self.image = pygame.Surface( (w, h) )
        self.image.fill(self.bg)
        self.image_rect = self.image.get_rect()

        if not self.center(c_l, c_m, c_r):
            self.image_rect.x = x
            self.image_rect.y = y

        self.text  = self.font.render(txt, True, fg)
        self.text_rect = self.text.get_rect(center=(w/2, h/2) )
        
        self.image.blit(self.text, self.text_rect)
    
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
            if mouse_pressed[0]: return True
            
        return False

    def draw_button(self, screen):
        screen.blit(self.image, self.image_rect)

class Text_input:
    def __init__(self):
        pass
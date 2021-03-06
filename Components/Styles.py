import pygame

from Components.Config import BLACK, WHITE
from helper import resource_path

class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(resource_path(file)).convert()

    def get_sprite(self, loc_x, loc_y, width, height):
        sprite = pygame.Surface( [width, height] )
        sprite.set_colorkey(BLACK)
        sprite.blit( self.sheet, (0,0), (loc_x, loc_y, width, height) )
        return sprite

def draw_text(screen, size, text, x, y, color=WHITE):
    font = pygame.font.Font(resource_path('assets/fonts/Arial.ttf'), size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()

    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

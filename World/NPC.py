import math
import pygame

from Components.Config import STORYSIZE, NPC_LAYER

class NPC(pygame.sprite.Sprite):
    def __init__(self, game, sheet, x, y):
        self._layer = NPC_LAYER
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = sheet.get_sprite(0, 0, STORYSIZE, STORYSIZE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.idle_animations = [
           sheet.get_sprite(0, 0, STORYSIZE, STORYSIZE),
           sheet.get_sprite(STORYSIZE, 0, STORYSIZE, STORYSIZE),
           sheet.get_sprite(STORYSIZE*2, 0, STORYSIZE, STORYSIZE),
        ]

        self.animation_loop = 0

    def animate(self):
        self.image = self.idle_animations[math.floor(self.animation_loop)]
        self.animation_loop += 0.05

        if self.animation_loop > 3:
            self.animation_loop = 1

    def __passable(self):
        return False
    
    def interact(self):
        pass

    def remove(self):
        self.kill()
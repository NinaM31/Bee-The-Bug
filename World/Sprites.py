import pygame

from Components.Config import *


class Water(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h, loc_x, loc_y, t):
        self._layer = WATER_LAYER
        self.groups = game.all_sprites, game.obstacle_sprites

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = game.water_spritesheet.get_sprite(loc_x, loc_y, w, h)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h, loc_x, loc_y):
        self._layer = GROUND_LAYER
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = game.world_spritesheet.get_sprite(loc_x, loc_y, w, h)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Plant(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h, loc_x, loc_y, t):
        if t == 'T':
            self._layer = TREE_LAYER
        else:
            self._layer = PLANT_LAYER

        # if t == 'T':
        #     self.groups = game.all_sprites, game.obstacle_sprites
        # else:
        self.groups = game.all_sprites
            
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = game.world_spritesheet.get_sprite(loc_x, loc_y, w, h)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class OnRoad(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h, loc_x, loc_y, t):
        self._layer = OBJECT_LAYER
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = game.world_spritesheet.get_sprite(loc_x, loc_y, w, h)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Accesories(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h, loc_x, loc_y, t):
        self._layer = OBJECT_LAYER
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = game.world_spritesheet.get_sprite(loc_x, loc_y, w, h)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Bridge(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h, loc_x, loc_y, t):
        self._layer = BRIDGE_LAYER
        self.groups = game.all_sprites, game.bridge_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = game.world_spritesheet.get_sprite(loc_x, loc_y, w, h)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class House(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h, loc_x, loc_y, t):
        self._layer = OBJECT_LAYER
        self.groups = game.all_sprites, game.obstacle_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = game.world_spritesheet.get_sprite(loc_x, loc_y, w, h)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
import pygame

from Components.Config import *

from World.Sprite_locations import interactable


class Water(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h, loc_x, loc_y, t):
        self._layer = WATER_LAYER
        self.groups = game.all_sprites, game.obstacle_sprites

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = game.water_spritesheet.get_sprite(loc_x, loc_y, w, h)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Border(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h, loc_x, loc_y):
        self._layer = BORDER_LAYER
        self.groups = game.all_sprites, game.obstacle_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = game.world_spritesheet.get_sprite(loc_x, loc_y, w, h)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

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

        self.groups = game.all_sprites
            
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = game.world_spritesheet.get_sprite(loc_x, loc_y, w, h)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class OnRoad(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h, loc_x, loc_y, t):
        self.game = game
        self._layer = OBJECT_LAYER
        self.t = t

        if t in interactable.keys():
            self.groups = game.all_sprites, game.interact_sprites
            ix, iy, (iw, ih), text = interactable[self.t]
            self.text = text
            self.interactable = game.interactable.get_sprite(ix, iy, iw, ih)
        else:
            self.groups = game.all_sprites

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = game.world_spritesheet.get_sprite(loc_x, loc_y, w, h)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.loc_x = loc_x
        self.loc_y = loc_y
        self.w = w
        self.h = h

    def interact(self):
        x, y = self.rect.x, self.rect.y
        self.image = self.interactable
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def uninteract(self):
        x, y = self.rect.x, self.rect.y

        self.image = self.game.world_spritesheet.get_sprite(self.loc_x, self.loc_y, self.w, self.h)
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y

class Accesories(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h, loc_x, loc_y, t):
        self.game = game
        self.t = t
        self._layer = OBJECT_LAYER

        if t in interactable.keys():
            self.groups = game.all_sprites, game.interact_sprites
            ix, iy, (iw, ih), text = interactable[self.t]
            self.text = text
            self.interactable = game.interactable.get_sprite(ix, iy, iw, ih)
        else:
            self.groups = game.all_sprites

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = game.world_spritesheet.get_sprite(loc_x, loc_y, w, h)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.loc_x = loc_x
        self.loc_y = loc_y
        self.w = w
        self.h = h

    def interact(self):
        x, y = self.rect.x, self.rect.y
        self.image = self.interactable
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def uninteract(self):
        x, y = self.rect.x, self.rect.y

        self.image = self.game.world_spritesheet.get_sprite(self.loc_x, self.loc_y, self.w, self.h)
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
    def __init__(self, game, x, y, w, h, loc_x, loc_y, t, house):
        self.game = game
        self.t = t
        self.interacted = False
        self._layer = OBJECT_LAYER
        self.house = house

        if t in ['D', 'GA']:
            self.groups = game.all_sprites, game.interact_sprites
            ix, iy, (iw, ih), text = interactable[self.t]
            self.text = text
            self.interactable = game.interactable.get_sprite(ix, iy, iw, ih)
        else:
            self.groups = game.all_sprites, game.obstacle_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.original = game.world_spritesheet.get_sprite(loc_x, loc_y, w, h)

        self.image = game.world_spritesheet.get_sprite(loc_x, loc_y, w, h)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.loc_x = loc_x
        self.loc_y = loc_y
        self.w = w
        self.h = h

    def interact(self):
        x, y = self.rect.x, self.rect.y

        self.image = self.interactable
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def uninteract(self):
        x, y = self.rect.x, self.rect.y

        self.image = self.original
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
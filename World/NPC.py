import math
import pygame

from Components.Config import STORYSIZE, NPC_LAYER, TILESIZE

from World.Sprite_locations import interactable

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
            self.animation_loop = 0

    def interact(self):
        pass

class NPC_world(pygame.sprite.Sprite):
    def __init__(self, game, x, y, loc_x, loc_y, t):
        self.t = t
        self.game = game
        self._layer = NPC_LAYER
        self.groups = game.all_sprites, game.interact_sprites

        ix, iy, (iw, ih), text = interactable[self.t]
        self.text = text
        self.interactable = game.interactable.get_sprite(ix, iy, iw, ih) 
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = game.npc_spritesheet.get_sprite(loc_x, loc_y, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.loc_x = loc_x
        self.loc_y = loc_y
        self.w = TILESIZE
        self.h = TILESIZE
    
    def interact(self):
        x, y = self.rect.x, self.rect.y
        self.image = self.interactable
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def uninteract(self):
        x, y = self.rect.x, self.rect.y

        self.image = self.game.npc_spritesheet.get_sprite(self.loc_x, self.loc_y, self.w, self.h)
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
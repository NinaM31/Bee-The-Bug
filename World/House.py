import pygame 

from Components.Config import BLACK, FURNITURE_LAYER, GROUND_LAYER, TILESIZE
from GameLogic.Player import Player
from World.Sprite_locations import house_1, interactable

class NPC_House:
    def __init__(self, game, house_data):
        self.game = game
        self.inside = True

        self.house_data = house_data
        self.player = Player(self.game, 9, 11)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.inside = False
                self.game.close_game()

    def generate_house(self):
        coordinates= house_1
        for data in self.house_data:
            t = data[0]
            x, y, w, h = data[1]

            loc_x, loc_y = coordinates[t]
            Furniture(self.game, x+160, y+160, w, h, loc_x, loc_y, t)

    def generate_floor(self):
        for i in range(13):
            for j in range(11):
                Floor(self.game, i+5, j+5, TILESIZE, TILESIZE, 96, 1183)

    def generate_border(self):
        for i in range(1):
            for j in range(12):
                Wall(self.game, i+4, j+4, 32, 32,  0, 2688)

        for i in range(14):
            for j in range(1):
                if i != 0:
                    Wall(self.game, i+4, j+4, 32, 32, 96, 2720)

        for i in range(14):
            for j in range(12):
                if i == 13:
                    Wall(self.game, i+5, j+4, 32, 32, 0, 2688)

        for i in range(15):
            for j in range(14):
                if j == 13:
                    Wall(self.game, i+4, j+3, 32, 32, 0, 2688)

    def inside_house(self):
        self.generate_house()
        self.generate_floor()
        self.generate_border()

        while self.inside:
            self.event()
            self.game.draw()

            if self.player.entered_house:
                print('entered')
                self.destroy_current()
                self.inside = False

    def destroy_current(self):
        for sprite in self.game.all_sprites:
            sprite.kill()

class Furniture(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h, loc_x, loc_y, t):
        self.game = game
        self.t = t
        self._layer = FURNITURE_LAYER

        if t in ['V', 'H']:
            self.groups = game.all_sprites, game.obstacle_sprites
        elif t in interactable.keys():
            self.groups = game.all_sprites, game.interact_sprites
            ix, iy, (iw, ih), text = interactable[self.t]
            self.text = text
            self.interactable = game.interactable.get_sprite(ix, iy, iw, ih)   
        else:
            self.groups = game.all_sprites, 

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

class Floor(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h, loc_x, loc_y):
        self._layer = GROUND_LAYER
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = game.world_spritesheet.get_sprite(loc_x, loc_y, w, h)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h, loc_x, loc_y):
        self._layer = 0
        self.groups = game.all_sprites, game.obstacle_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = game.world_spritesheet.get_sprite(loc_x, loc_y, w, h)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
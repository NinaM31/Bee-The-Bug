import pygame 

from Components.Config import BLACK, FURNITURE_LAYER, GROUND_LAYER, TILESIZE
from World.Sprite_locations import house_1

class NPC_House:
    def __init__(self, game, house_data, player):
        self.game = game
        self.inside = True
        self.house_data = house_data
        self.player = player

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.inside = False
                self.game.close_game()

    def animate(self):
        self.game.screen.fill(BLACK)
        pygame.display.update()

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

    def inside_house(self):
        self.generate_house()
        self.generate_floor()
        
        while self.inside:
            self.event()
            self.game.show_house()


class Furniture(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h, loc_x, loc_y, t):
        self._layer = FURNITURE_LAYER
        self.groups = game.house_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = game.world_spritesheet.get_sprite(loc_x, loc_y, w, h)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Floor(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h, loc_x, loc_y):
        self._layer = GROUND_LAYER
        self.groups = game.house_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = game.world_spritesheet.get_sprite(loc_x, loc_y, w, h)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

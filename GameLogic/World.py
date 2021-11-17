import pygame

from GameLogic.data import  *
from GameLogic.Player import Player
from World.Water import *
from World.Sprite_locations import *


class World():
    def __init__(self, game):
        self.world_map = world_map[:][:]
        self.game = game

    def read_data(self, file):
        with open(file) as f:
            lines = f.readlines() 
            data = []
        
            for i, l in enumerate(lines):
                items = l.split(' ') 
                t = items[0]
                x = int(items[1])
                y = int(items[2])
                w = int(items[3])
                h = int(items[4])

                data.append( (t, (x, y, w, h)) )

            return data
        
    def __generate(self, generation_data, coordinates, class_name):
        for data in generation_data:
            t = data[0]
            x, y, w, h = data[1]

            loc_x, loc_y = coordinates[t]
            globals()[class_name](self.game, x, y, w, h, loc_x, loc_y)

    def generate_water(self):
        water_data = self.read_data('data/water.txt')
        self.__generate(water_data, Water_coordinates, 'Water')

    def generate_land(self):
        pass

    def Home_accessories(self):
        home_accessories_data = self.read_data('data/homeAccessories.txt')
        self.__generate(home_accessories_data, Home_accessories_coordinates, 'Accesories')

    def generate_plants(self):
        plant_data = self.read_data('data/plants.txt')
        self.__generate(plant_data, Plant_coordinates, 'Plant')
    
    def generate_bridges(self):
        pass

    def generate_onRoad(self):
        onRoad_data = self.read_data('data/onRoad.txt')
        self.__generate(onRoad_data, OnRoad_coordinates, 'OnRoad')

    def generate_world(self):
        
        
        self.generate_water()
        self.generate_plants()
        self.generate_onRoad()
        self.Home_accessories()
        Player(self.game, 32, 32)
        
        














































#         for i, row in enumerate(world_map):
#             for j, col in enumerate(row):
#                 if col not in ('W', 'WF', 'WU', 'LT.', 'RT.'):
#                     Terrian(self.game, j, i).basic()

#                 if col == 'P':
#                     self.player = Player(self.game, j, i)

#                 if col == 'L.':
#                     Terrian(self.game, j, i).left()
#                 if col == 'R.':
#                     Terrian(self.game, j, i).right()
#                 if col == 'T.':
#                     Terrian(self.game, j, i).top()
#                 if col == 'B.':
#                     Terrian(self.game, j, i).bottom()
#                 if col == 'LB.':
#                     Terrian(self.game, j, i).left_bottom()
#                 if col == 'RB.':
#                     Terrian(self.game, j, i).right_bottom()
#                 if col == 'RT.':
#                     Lake(self.game, j, i).water()
#                     Terrian(self.game, j, i).right_top()
#                 if col == 'LT.':
#                     Lake(self.game, j, i).water()
#                     Terrian(self.game, j, i).left_top()

#                 if col == 'FB':
#                     Terrian(self.game, j, i).bottom()
#                     Bridge(self.game, j, i).front()
#                 if col == 'SB':
#                     Bridge(self.game, j, i).side()

#                 if col == 'W':
#                     Lake(self.game, j, i).water()
#                 if col == 'WF':
#                     Lake(self.game, j, i).water_fall_d()
#                 if col == 'WU':
#                     Lake(self.game, j, i).water_fall_u()

#                 if col == 'F':
#                     Fence(self.game, j, i).fence()
#                 if col == 'LTE':
#                     Fence(self.game, j, i).lt_edge()
#                 if col == 'LBE':
#                     Fence(self.game, j, i).lb_edge()
#                 if col == 'RTE':
#                     Fence(self.game, j, i).rt_edge()
#                 if col == 'RBE':
#                     Fence(self.game, j, i).rb_edge()
#                 if col == 'VE':
#                     Fence(self.game, j, i).v_edge()
                
#                 if col == 'T':
#                     Tree(self.game, j, i).tree()
#                 if col == 'ST':
#                     Tree(self.game, j, i).s_trunk()
#                 if col == 'FT':
#                     Tree(self.game, j, i).f_trunk()

#                 if col == 'FW':
#                     Flower(self.game, j, i).white_flower()
#                 if col == 'FM':
#                     Flower(self.game, j, i).mashroom_flower()

# class Lake(pygame.sprite.Sprite):
#     def __init__(self, game, x, y):
#         self._layer = WATER_LAYER
#         self.groups = game.all_sprites
#         pygame.sprite.Sprite.__init__(self, self.groups)

#         self.game = game
#         self.x = x * TILESIZE
#         self.y = y * TILESIZE

#     def water(self):
#         self.image = self.game.water_spritesheet.get_sprite(450, 1370, TILESIZE, TILESIZE)
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y

#     def water_fall_d(self):
#         self.image = self.game.water_fall_spritesheet.get_sprite(164, 254, TILESIZE, TILESIZE)
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y
    
#     def water_fall_u(self):
#         self.image = self.game.water_fall_spritesheet.get_sprite(164, 208, TILESIZE, TILESIZE)
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y
    
# class Flower(pygame.sprite.Sprite): 
#     def __init__(self, game, x, y):
#         self._layer = FLOWER_LAYER
#         self.groups = game.all_sprites, game.obstacles
#         pygame.sprite.Sprite.__init__(self, self.groups)

#         self.game = game
#         self.x = x * TILESIZE
#         self.y = y * TILESIZE

#     def white_flower(self):
#         self.image = self.game.world_spritesheet.get_sprite(130, 190, TILESIZE, TILESIZE)
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y

#     def mashroom_flower(self):
#         self.image = self.game.world_spritesheet.get_sprite(34, 228, TILESIZE, TILESIZE)
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y

# class Fence(pygame.sprite.Sprite):                    
#     def __init__(self, game, x, y):
#         self._layer = TREE_LAYER
#         self.groups = game.all_sprites, game.obstacles
#         pygame.sprite.Sprite.__init__(self, self.groups)

#         self.game = game
#         self.x = x * TILESIZE
#         self.y = y * TILESIZE

#     def fence(self):
#         self.image = self.game.world_spritesheet.get_sprite(0, 736, TILESIZE, TILESIZE)
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y

#     def v_edge(self):
#         self.image = self.game.world_spritesheet.get_sprite(10, 704, TILESIZE, TILESIZE)
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y

#     def lt_edge(self):
#         self.image = self.game.world_spritesheet.get_sprite(74, 704, TILESIZE, TILESIZE)
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y

#     def lb_edge(self):
#         self.image = self.game.world_spritesheet.get_sprite(74, 736, TILESIZE, TILESIZE)
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y

#     def rt_edge(self):
#         self.image = self.game.world_spritesheet.get_sprite(106, 704, TILESIZE/2, TILESIZE)
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y
    
#     def rb_edge(self):
#         self.image = self.game.world_spritesheet.get_sprite(106, 736, TILESIZE, TILESIZE)
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y
         
# class Terrian(pygame.sprite.Sprite):
#     def __init__(self, game, x, y):
#         self._layer = GROUND_LAYER
#         self.groups = game.all_sprites
#         pygame.sprite.Sprite.__init__(self, self.groups)

#         self.game = game
#         self.x = x * TILESIZE
#         self.y = y * TILESIZE

#     def basic(self):
#         self.image = self.game.world_spritesheet.get_sprite(0, 0, TILESIZE, TILESIZE)
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y

#     def left(self):
#         self.image = self.game.world_spritesheet.get_sprite(64, 320, TILESIZE, TILESIZE)
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y

#     def right(self):
#         self.image = self.game.world_spritesheet.get_sprite(0, 320, TILESIZE, TILESIZE)
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y

#     def top(self):
#         self.image = self.game.world_spritesheet.get_sprite(32, 288, TILESIZE, TILESIZE)
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y

#     def bottom(self):
#         self.image = self.game.world_spritesheet.get_sprite(32, 352, TILESIZE, TILESIZE*3)
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y

#     def left_bottom(self):
#         self.image = self.game.world_spritesheet.get_sprite(64, 352, TILESIZE, TILESIZE*3)
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y

#     def right_bottom(self):
#         self.image = self.game.world_spritesheet.get_sprite(0, 352, TILESIZE, TILESIZE*3)
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y

#     def left_top(self):
#         self.image = self.game.world_spritesheet.get_sprite(64, 288, TILESIZE, TILESIZE*3)
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y

#     def right_top(self):
#         self.image = self.game.world_spritesheet.get_sprite(0, 288, TILESIZE, TILESIZE*3)
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y

# class Bridge(pygame.sprite.Sprite):
#     def __init__(self, game, x, y):
#         self._layer = BRIDGE_LAYER
#         self.groups = game.all_sprites
#         pygame.sprite.Sprite.__init__(self, self.groups)

#         self.game = game
#         self.x = x * TILESIZE
#         self.y = y * TILESIZE

#     def front(self):
#         self.image = self.game.world_spritesheet.get_sprite(94, 1056, TILESIZE*3, TILESIZE*3)
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y

#     def side(self):
#         self.image = self.game.world_spritesheet.get_sprite(0, 1056, TILESIZE*3, TILESIZE*3)
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y

# class Tree(pygame.sprite.Sprite):
#     def __init__(self, game, x, y):
#         self._layer = TREE_LAYER
#         self.groups = game.all_sprites, game.obstacles
#         pygame.sprite.Sprite.__init__(self, self.groups)

#         self.game = game
#         self.x = x * TILESIZE
#         self.y = y * TILESIZE

#     def tree(self):
#         self.image = self.game.world_spritesheet.get_sprite(64, 32, TILESIZE*2, TILESIZE*2)
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x 
#         self.rect.y = self.y 

#     def f_trunk(self):
#         self.image = self.game.world_spritesheet.get_sprite(227, 227, TILESIZE, TILESIZE*2)
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x 
#         self.rect.y = self.y 

#     def s_trunk(self):
#         self.image = self.game.world_spritesheet.get_sprite(192, 160, TILESIZE*2, TILESIZE)
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x 
#         self.rect.y = self.y
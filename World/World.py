import pygame

from GameLogic.data import  *
from GameLogic.Player import Player
from World.House import NPC_House
from World.Sprites import *
from World.Sprite_locations import *


class World():
    def __init__(self, game):
        self.world_map = world_map[:][:]
        self.game = game
        self.outside_audio = "assets/audio/background.mp3"
        
    def load_assets(self, audio=None):
        if not audio:
            audio = self.outside_audio
        pygame.mixer.music.load(audio)

    def start_sound(self, volume):
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(volume)

    def stop_audio(self):
         pygame.mixer.music.stop()

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
        
    def __generate(self, generation_data, coordinates, class_name, extras=None):
        for data in generation_data:
            t = data[0]
            x, y, w, h = data[1]

            loc_x, loc_y = coordinates[t]

            if extras:
                globals()[class_name](self.game, x, y, w, h, loc_x, loc_y, t, extras)
            else:
                globals()[class_name](self.game, x, y, w, h, loc_x, loc_y, t)
                
    def generate_water(self):
        water_data = self.read_data('data/water.txt')
        self.__generate(water_data, Water_coordinates, 'Water')

    def generate_land(self):
        for i in range(51):
            for j in range(40):
                Ground(self.game, i, j, TILESIZE, TILESIZE, 0, 0)

    def Home_accessories(self):
        home_accessories_data = self.read_data('data/homeAccessories.txt')
        self.__generate(home_accessories_data, Home_accessories_coordinates, 'Accesories')

    def generate_plants(self):
        plant_data = self.read_data('data/plants.txt')
        self.__generate(plant_data, Plant_coordinates, 'Plant')
    
    def generate_bridges(self):
        bridge_data = self.read_data('data/bridge.txt')
        self.__generate(bridge_data, Bridge_coordinates, 'Bridge')

    def generate_onRoad(self):
        onRoad_data = self.read_data('data/onRoad.txt')
        self.__generate(onRoad_data, OnRoad_coordinates, 'OnRoad')

    def generate_houses(self):
        for i in range(5):
            house_data= self.read_data(f'data/house{i+1}.txt')
            coordinates= eval(f'H{i+1}_coordinates')
            house= self.read_data(f'data/house_{i+1}.txt')
            self.__generate(house_data, coordinates, 'House', house)

    def generate_borders(self):
        for i in range(1):
            for j in range(40):
                Border(self.game, i, j, 10, 32, 32, 0)
        
        for i in range(51):
            for j in range(1):
                Border(self.game, i, j, 32, 10, 32, 0)

        for i in range(51):
            for j in range(40):
                if i == 50:
                    Border(self.game, i, j, 10, 32, 32, 0)

        for i in range(51):
            for j in range(40):
                if j == 39:
                    Border(self.game, i, j+1, 32, 10, 32, 0)

    def check_inside_house(self):
        if self.player.entered_house:
            x, y = self.player.rect.x, self.player.rect.y
            self.destroy()
            self.player.entered_house = False

            self.house = NPC_House(self.game, self.player.current_house)
            self.house.inside_house()
            self.create(x, y)  

    def create(self, x, y):
        self.player = None
        self.generate_world()

    def destroy(self):
        for sprite in self.game.all_sprites:
            sprite.kill() 

    def interact(self):
        self.player.interact()

    def update(self):
        self.check_inside_house()

    def generate_world(self, x=7, y=9):
        self.generate_borders()
        self.generate_land()
        self.generate_water()
        self.generate_plants()
        
        self.generate_houses()
        self.generate_onRoad()
        self.Home_accessories()
        self.generate_bridges()

        self.player = Player(self.game, x, y)
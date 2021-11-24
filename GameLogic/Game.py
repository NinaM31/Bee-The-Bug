import pygame

from Components.Config import WIN_WIDTH, WIN_HEIGHT, FPS, BLACK
from Components.Menu import StartMenu, EndMenu, SettingsMenu
from Components.Styles import Spritesheet
from GameLogic.World import World

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIN_WIDTH, WIN_HEIGHT) )
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = False

        self.startMenue = StartMenu(self)
        self.endMenue = EndMenu(self)
        self.settingsMenue = SettingsMenu(self)
        
        self.world_spritesheet = Spritesheet('assets/all.png')
        self.water_spritesheet = Spritesheet('assets/water.png')
        self.character_spritesheet = Spritesheet('assets/bee.png')

    def game_intro(self):
        self.startMenue.display()

    def show_settings(self):
        self.settingsMenue.display()

    def game_over(self):
        self.endMenue.display()
    
    def new(self):
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.obstacle_sprites = pygame.sprite.LayeredUpdates()
        self.bridge_sprites = pygame.sprite.LayeredUpdates()

        self.world = World(self)
        self.world.generate_world()

    def update(self):
        self.all_sprites.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False

    def draw(self): 
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def play(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
import pygame

from Components.Config import WIN_WIDTH, WIN_HEIGHT, FPS, BLACK, BKGAUDIO
from Components.Menu import StartMenu, EndMenu, SettingsMenu
from Components.Styles import Spritesheet
from Components.Stories import Stories
from World.World import World

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode( (WIN_WIDTH, WIN_HEIGHT) )
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = False

        self.startMenue = StartMenu(self)
        self.endMenue = EndMenu(self)
        self.settingsMenue = SettingsMenu(self)

        self.stories = Stories(self)

        self.world_spritesheet = Spritesheet('assets/all.png')
        self.water_spritesheet = Spritesheet('assets/water.png')
        self.character_spritesheet = Spritesheet('assets/bee.png')

    def close_game(self):
        self.playing = False
        self.running = False

    def game_intro(self):
        self.startMenue.load_assets()
        self.startMenue.display()
        # self.stories.beggining()

    def show_settings(self):
        self.settingsMenue.display()

    def game_over(self):
        self.endMenue.load_assets()
        self.endMenue.display()
    
    def new(self):
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.obstacle_sprites = pygame.sprite.LayeredUpdates()
        self.bridge_sprites = pygame.sprite.LayeredUpdates()

        self.world = World(self)

        self.world.load_assets()
        self.world.start_sound(BKGAUDIO)
        self.world.generate_world()

    def update(self):
        self.all_sprites.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close_game()

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
import sys
import pygame

from Components.Config import WIN_WIDTH, WIN_HEIGHT, FPS, BLACK, BKGAUDIO, WHITE
from Components.Menu import StartMenu, EndMenu, SettingsMenu
from Components.Styles import Spritesheet
from Components.Stories import Stories

from GameLogic.Timer import Timer

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

        self.timer = Timer()

        self.world_spritesheet = Spritesheet('assets/all.png')
        self.water_spritesheet = Spritesheet('assets/water.png')
        self.character_spritesheet = Spritesheet('assets/bee.png')

        self.interactable = Spritesheet('assets/interactable.png')
        self.feedback_sprite = Spritesheet('assets/feedback.png')

    def close_game(self):
        self.playing = False
        self.running = False
        pygame.quit()
        sys.exit()

    def game_intro(self):
        self.startMenue.load_assets()
        self.startMenue.display()

        self.init_sprites()
        self.stories = Stories(self)
        self.stories.beggining()

    def show_settings(self):
        self.settingsMenue.display()

    def game_over(self):
        self.endMenue.load_assets()
        self.endMenue.display()

    def init_sprites(self):
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.obstacle_sprites = pygame.sprite.LayeredUpdates()
        self.interact_sprites = pygame.sprite.LayeredUpdates()
        self.bridge_sprites = pygame.sprite.LayeredUpdates()

    def new(self):
        self.world = World(self)

        self.world.load_assets()
        self.world.start_sound(BKGAUDIO)
        self.timer.start()
        self.world.generate_world()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close_game()
    
    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.update() 
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        self.timer.tick(self.screen)
        pygame.display.update()

    def play(self):
        while self.playing:
            self.events()
            self.draw()
            self.world.update()
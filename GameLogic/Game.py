import sys
import pygame

from Components.Config import WIN_WIDTH, WIN_HEIGHT, FPS, BLACK, BKGAUDIO, WHITE
from Components.Menu import StartMenu, EndMenu
from Components.Styles import Spritesheet
from Components.Stories import Stories

from GameLogic.Timer import Timer

from World.World import World
from helper import resource_path

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

        self.world_spritesheet = Spritesheet(resource_path('assets/all.png'))
        self.water_spritesheet = Spritesheet(resource_path('assets/water.png'))
        self.character_spritesheet = Spritesheet(resource_path('assets/bee.png'))
        self.npc_spritesheet = Spritesheet(resource_path('assets/NPC.png'))

        self.interactable = Spritesheet(resource_path('assets/interactable.png'))
        self.feedback_sprite = Spritesheet(resource_path('assets/feedback.png'))

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
        self.stories.load_assets() 
        self.stories.start_sound(BKGAUDIO)
        self.stories.beginning()
        self.new()
        self.playing = True

    def game_over(self):
        self.timer = None
        self.world = None
        self.stories = None

        self.endMenue.load_assets()
        self.endMenue.display()

    def init_sprites(self):
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.obstacle_sprites = pygame.sprite.LayeredUpdates()
        self.interact_sprites = pygame.sprite.LayeredUpdates()
        self.bridge_sprites = pygame.sprite.LayeredUpdates()

    def new(self):
        self.world = World(self)
        self.timer = Timer()
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

        if self.timer.time_end() or self.world.ended:
            self.world.destroy()
            self.timer.alert_user = False
            self.world.stop_audio()

            self.stories.start_sound(BKGAUDIO)
            self.stories.ending()
            self.stories.stop_audio()
            self.playing = False

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
import pygame

from Components.Styles import Spritesheet, draw_text
from Components.Input import Button
from Components.Config import TILESIZE, FPS, WIN_WIDTH, STORYSIZE, PINK, YELLOW, RED, DARKBLUE, BERRY
from World.NPC import *

class Stories:
    def __init__(self, game):
        self.game = game
        
        self.next = Button('Next', 150, 50, 340 , 550, bg=DARKBLUE, bg_hvr=BERRY)
        self.back = Button('Menu', 150, 50, 0, 0, bg=DARKBLUE, bg_hvr=PINK)
        self.skip = Button('Skip', 150, 50, WIN_WIDTH-150, 0, bg=DARKBLUE)

        self.ladybug_story = Spritesheet('assets/stories/lady.png')
        self.bee_story = Spritesheet('assets/stories/bee.png')
        self.prison_audio = "assets/audio/prison.mp3"

        self.ladyBug = NPC(game, self.ladybug_story, 450, 350)
        self.bee = NPC(game, self.bee_story, 120, 300)

        self.current_page = 0
        self.dialog_1 = [
                ('Sup', (110, 520), YELLOW),
                ('uh well..', (610, 520), RED),
                ("I am going to jail :(", (610, 520), RED),
                ("What for?", (110, 520), YELLOW),
                ('Robbing the bank', (610, 520), RED),
                ('...', (110, 520), YELLOW),
                ("I didn't do it, I was framed!", (600, 520), RED),
                ('Interesting..', (110, 520), YELLOW),
                ("In 10 min they'll make it official", (560, 520), RED),
                ('Can you help me detective?', (600, 520), RED),
                ('...', (110, 520), YELLOW),
                ('I am truly innocent', (610, 520), RED),
                ('Bad luck you know', (610, 520), RED),
                ('..I dont know', (110, 520), YELLOW),
            ]

    def load_assets(self, audio=None):
        if not audio:
            audio = self.prison_audio
        self.prison_audio = pygame.mixer.Sound(audio)

    def start_sound(self, volume):
        self.prison_audio.play(-1)
        self.prison_audio.set_volume(volume)

    def stop_audio(self):
        self.prison_audio.stop()

    def check_buttons(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if self.next.pressed(mouse_pos, mouse_pressed):
            self.current_page += 1

        if self.back.pressed(mouse_pos, mouse_pressed):
            self.current_page = -1

        if self.skip.pressed(mouse_pos, mouse_pressed):
            self.current_page = 50

    def back_to_main(self):
        self.end_story()
        self.game.game_intro()
        self.stop_audio()

    def end_story(self):
        self.ladyBug.remove()
        self.bee.remove()
        self.waiting = False
        self.current_page = 0

    def story_one(self):
        if self.current_page <= -1:
            self.back_to_main()

        if self.current_page >= len(self.dialog_1):
            self.end_story()
            self.game.playing = True
            self.game.new()
            return

        self.ladyBug.animate()
        self.bee.animate()

        text, (x, y), color = self.dialog_1[self.current_page]
        draw_text(self.game.screen, 40, text, x, y, color)

    def draw_buttons(self):
        self.back.draw_button(self.game.screen)
        self.next.draw_button(self.game.screen)
        self.skip.draw_button(self.game.screen)
        

        mouse_pos = pygame.mouse.get_pos()
        self.next.hovered(mouse_pos)
        self.back.hovered(mouse_pos)
        self.skip.hovered(mouse_pos)

    def beggining(self):
        self.waiting = True
        self.background = pygame.image.load('assets/prison.png').convert()

        while self.waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.waiting = False
                    self.game.close_game()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_buttons()

            self.game.screen.blit(self.background, (0,0), pygame.Rect(100, 300, 800, 900))
            self.draw_buttons()
            self.game.all_sprites.draw(self.game.screen)
            self.game.clock.tick(FPS)
            self.story_one()
            pygame.display.update()
        self.stop_audio()

    def ending(self):
        self.waiting = True
        self.background = pygame.image.load('assets/prison.png').convert()

        while self.waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.waiting = False
                    self.game.close_game()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_buttons()

            self.game.screen.fill(PINK)
            # self.game.screen.blit(self.background, (0,0), pygame.Rect(100, 300, 800, 900))
            # self.draw_buttons()
            # self.game.all_sprites.draw(self.game.screen)
            self.game.clock.tick(FPS)
            # self.story_one()
            pygame.display.update()
        self.stop_audio()
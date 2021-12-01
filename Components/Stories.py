import pygame

from Components.Styles import Spritesheet, draw_text
from Components.Input import Button
from Components.Config import TILESIZE, BODY, FPS, WIN_WIDTH, STORYSIZE, PINK, YELLOW, RED, DARKBLUE, BERRY, BLACK

from World.NPC import *

from helper import resource_path


class Stories:
    def __init__(self, game):
        self.game = game
        
        self.next = Button('Next', 150, 50, 340 , 550, bg=DARKBLUE, bg_hvr=BERRY)
        self.back = Button('Menu', 150, 50, 0, 0, bg=DARKBLUE, bg_hvr=PINK)
        self.skip = Button('Skip', 150, 50, WIN_WIDTH-150, 0, bg=DARKBLUE)

        self.ladybug_story = Spritesheet(resource_path('assets/stories/lady.png'))
        self.bee_story = Spritesheet(resource_path('assets/stories/bee.png'))
        self.ant_story = Spritesheet(resource_path('assets/stories/ant.png'))
        self.hopper_story = Spritesheet(resource_path('assets/stories/hopper.png'))
        self.fly_story = Spritesheet(resource_path('assets/stories/fly.png'))

        self.prison_audio = "assets/audio/prison.mp3"
        self.boo_audio = "assets/audio/boo.mp3"
        self.yay_audio = "assets/audio/yay.mp3"

        self.current_page = 0
        self.picked = False
        
        self.suspects = {
            'a': self.play_ant,
            'l': self.play_lady,
            'b': self.play_bee,
            'h': self.play_hopper,
            'f': self.play_fly
        }

        self.dialog_1 = [
                ('Sup', (110, 520), YELLOW),
                ('uh well..', (610, 520), RED),
                ("I am going to jail :(", (610, 520), RED),
                ("What for?", (110, 520), YELLOW),
                ('Robbing the bank', (610, 520), RED),
                ('...', (110, 520), YELLOW),
                ("I didn't do it, I was framed!", (600, 520), RED),
                ('Interesting..', (110, 520), YELLOW),
                ("In 5 min they'll make it official", (560, 520), RED),
                ('Can you help me detective?', (600, 520), RED),
                ('...', (110, 520), YELLOW),
                ('I am truly innocent', (610, 520), RED),
                ('Why do they suspect you ?', (200, 520), YELLOW),
                ("My finger prints are at the bank", (500, 520), RED),
                ("Ooh...", (110, 520), YELLOW),
                ("Cause I'm the only employee at the bank T_T", (500, 520), RED),
                ('And.. Bad luck you know', (610, 520), RED),
                ('..I dont know', (110, 520), YELLOW),
            ]

        self.bee_dialog = [
            ('You are now a prime suspect', (400, 50), YELLOW),
            ("No one suspected you until", (400, 100), YELLOW),
            ("you jokefuly decided to say it's you -_-", (400, 150), YELLOW),
            ("Only criminals confess to their crimes.", (400, 200), YELLOW),
            ("now you're sentenced to 5 years in prison. ", (400, 250) , YELLOW),
            ("On the bright side Ladybug can take care of her kids", (400, 300), YELLOW),
            ("You're still someone's hero", (500, 350), YELLOW)
        ]

        self.fly_dialog = [
            ('You were wrong detective', (400, 50), YELLOW),
            ("Fly is only a jealous bug", (400, 100), YELLOW),
            ("There is not enough evidence to put him to jail", (400, 150), YELLOW),
            ("... Fly is a heartbroken bug", (400, 200), YELLOW),
            ("His wife left him for an Ant. ", (400, 250) , YELLOW),
            ("She replaced his old ring for a fresh apple ", (400, 300) , YELLOW),
        ]

        self.lady_dialog = [
            ('Sorry detective but you missed', (400, 50), YELLOW),
            ("Now lady will be sentenced to 5 years in prison", (400, 100), YELLOW),
            ("And no one will take care of her children", (400, 150), YELLOW),
            ("... Uhm hmm on the bright side", (400, 200) , YELLOW),
            ("Fly is happy. Maybe you ..", (400, 250) , YELLOW),
            (" could suggest him to take care", (400, 300) , YELLOW),
            ("of his OWN children ._.!", (500, 350) , YELLOW),
        ]

        self.hopper_dialog = [
            ('Nah you are wrong Detective', (400, 50), YELLOW),
            ("Hopper is innocent", (400, 100), YELLOW),
            ("Now lady will be sentenced to 5 years in prison", (400, 150), YELLOW),
            ("Because you failed to bring strong evidence", (400, 200), YELLOW),
            ("... I think it was obvious he is innocent", (400, 250) , YELLOW),
            ("I try not to judge...", (400, 300) , YELLOW),
        ]

        self.ant_dialog = [
            ('"Poor ladybug" said Mr Ant', (400, 50), YELLOW),
            ('But ladybug said "In 5 min theyll make it official" ', (400, 100), YELLOW),
            ('implying that no one knew who robbed the bank back then', (400, 150), YELLOW),
            ("Shovel in his house and holes all over the ground", (400, 200), YELLOW),
            ("His company is going banckrupt", (400, 250), YELLOW),
            ("Missed Ladybugs birthday, cause he was planing his crime", (400, 300), YELLOW),
            ("Nice catch detective", (400, 350) , YELLOW),
        ]

    def load_assets(self, audio=None):
        if not audio:
            audio = self.prison_audio
        self.prison_audio = pygame.mixer.Sound(resource_path(audio))

    def start_sound(self, volume, repeat=-1):
        self.prison_audio.play(repeat)
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
        for sprite in self.game.all_sprites:
            sprite.kill()

        self.waiting = False
        self.current_page = 0
        self.stop_audio()

    def choose(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if self.l.pressed(mouse_pos, mouse_pressed):
            self.picked = True
            self.key = 'l'
            self.ladyBug = NPC(self.game, self.ladybug_story, 480, 350)
            pygame.mixer.Sound(resource_path(self.boo_audio)).play()

        if self.a.pressed(mouse_pos, mouse_pressed):
            self.picked = True
            self.key = 'a'
            self.ant = NPC(self.game, self.ant_story, 480, 300)
            pygame.mixer.Sound(resource_path(self.yay_audio)).play()

        if self.b.pressed(mouse_pos, mouse_pressed):
            self.picked = True
            self.key = 'b'
            pygame.mixer.Sound(resource_path(self.boo_audio)).play()

        if self.h.pressed(mouse_pos, mouse_pressed):
            self.picked = True
            self.key = 'h'
            self.hopper = NPC(self.game, self.hopper_story, 480, 300)
            pygame.mixer.Sound(resource_path(self.boo_audio)).play()

        if self.f.pressed(mouse_pos, mouse_pressed):
            self.picked = True
            self.key = 'f'
            self.fly = NPC(self.game, self.fly_story, 480, 300)
            pygame.mixer.Sound(resource_path(self.boo_audio)).play()

    def play_story(self):
        self.suspects[self.key]()

    def play_lady(self):
        self.ladyBug.animate()
        self.bee.animate()

        for dialog in self.lady_dialog:
            text, (x, y), color = dialog
            draw_text(self.game.screen, BODY, text, x, y, color)

    def play_ant(self):
        self.ant.animate()
        self.bee.animate()

        for dialog in self.ant_dialog:
            text, (x, y), color = dialog
            draw_text(self.game.screen, BODY, text, x, y, color)

    def play_hopper(self):
        self.hopper.animate()
        self.bee.animate() 

        for dialog in self.hopper_dialog:
            text, (x, y), color = dialog
            draw_text(self.game.screen, BODY, text, x, y, color)

    def play_bee(self):
        self.bee.animate()
        
        for dialog in self.bee_dialog:
            text, (x, y), color = dialog
            draw_text(self.game.screen, BODY, text, x, y, color)

    def play_fly(self):
        self.fly.animate()
        self.bee.animate() 

        for dialog in self.fly_dialog:
            text, (x, y), color = dialog
            draw_text(self.game.screen, BODY, text, x, y, color)

    def pick_criminal(self):
        self.l.draw_button(self.game.screen)
        self.a.draw_button(self.game.screen)
        self.b.draw_button(self.game.screen)
        self.h.draw_button(self.game.screen)
        self.f.draw_button(self.game.screen)
        
        mouse_pos = pygame.mouse.get_pos()
        self.l.hovered(mouse_pos)
        self.a.hovered(mouse_pos)
        self.b.hovered(mouse_pos)
        self.h.hovered(mouse_pos)
        self.f.hovered(mouse_pos)

    def story_one(self):
        if self.current_page <= -1:
            self.back_to_main()

        if self.current_page >= len(self.dialog_1):
            self.end_story()
            return

        self.ladyBug.animate()
        self.bee.animate()

        text, (x, y), color = self.dialog_1[self.current_page]
        draw_text(self.game.screen, BODY, text, x, y, color)

    def draw_buttons(self):
        self.back.draw_button(self.game.screen)
        self.next.draw_button(self.game.screen)
        self.skip.draw_button(self.game.screen)
        
        mouse_pos = pygame.mouse.get_pos()
        self.next.hovered(mouse_pos)
        self.back.hovered(mouse_pos)
        self.skip.hovered(mouse_pos)

    def beginning(self):
        self.waiting = True
        self.background = pygame.image.load(resource_path('assets/prison.png')).convert()

        self.ladyBug = NPC(self.game, self.ladybug_story, 450, 350)
        self.bee = NPC(self.game, self.bee_story, 120, 300)

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

    def ending(self):
        self.waiting = True
        self.background = pygame.image.load(resource_path('assets/prison.png')).convert()

        self.l = Button('Lady bug', 200, 50, 300 , 50)
        self.a = Button('Mr. Ant', 200, 50, 300, 150)
        self.b = Button('Detective Bee', 200, 50, 300, 250)
        self.h = Button('Sir Hopper', 200, 50, 300, 350)
        self.f = Button('Mr. Fly', 200, 50, 300, 450)

        self.next = Button('Next', 150, 50, 340 , 550, bg=DARKBLUE, bg_hvr=BERRY)
        self.bee = NPC(self.game, self.bee_story, 100, 320)

        while self.waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.waiting = False
                    self.game.close_game()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.choose()

            if not self.picked:
                self.game.screen.blit(self.background, (0,0), pygame.Rect(100, 300, 800, 900))
                self.pick_criminal()
                draw_text(self.game.screen, 55, 'Pick the Criminal', WIN_WIDTH/2 , 550)
            else:
                self.game.screen.fill(BLACK)
                self.play_story()
                self.game.all_sprites.draw(self.game.screen)

                self.next.draw_button(self.game.screen)

                mouse_pos = pygame.mouse.get_pos()
                mouse_pressed = pygame.mouse.get_pressed()
                self.next.hovered(mouse_pos)

                if self.next.pressed(mouse_pos, mouse_pressed):
                    self.end_story()
                    
            self.game.clock.tick(FPS)
            pygame.display.update()
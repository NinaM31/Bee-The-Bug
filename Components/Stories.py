import pygame

from Components.Styles import Spritesheet, draw_text
from Components.Input import Button
from Components.Config import TILESIZE, FPS, WIN_WIDTH, STORYSIZE, PINK, YELLOW, RED, DARKBLUE
from World.NPC import *

class Stories:
    def __init__(self, game):
        self.game = game
        
        self.next = Button('Next', 100, 40, c_m=True)
        self.back = Button('Menu', 150, 50, 0, 0, bg=PINK, bg_hvr=DARKBLUE)
        self.skip = Button('Skip', 150, 50, WIN_WIDTH-150, 0, bg=PINK)

        self.ladybug_story = Spritesheet('assets/stories/lady.png')
        self.bee_story = Spritesheet('assets/stories/bee.png')

        self.ladyBug = NPC(game, self.ladybug_story, 450, 150)
        self.bee = NPC(game, self.bee_story, 100, 120)

        self.current_page = 0
        self.dialog_1 = [
                ('Sup', (100, 160), YELLOW),
                ('uh well..', (550, 160), RED),
                ("I am going to jail :(", (550, 160), RED),
                ("What for?", (100, 160), YELLOW),
                ('Robbing the bank', (550, 160), RED),
                ('...', (100, 160), YELLOW),
                ("I didn't do it, I was framed!", (550, 160), RED),
                ('Interesting..', (100, 160), YELLOW),
                ("In 10 min they'll take me away", (550, 160), RED),
                ('Can you help me detective?', (550, 160), RED),
                ('...', (100, 160), YELLOW),
                ('I am truly innocent', (550, 140), RED),
                ('Bad luck you know', (550, 140), RED),
                ('..I dont know', (100, 140), YELLOW),
            ]

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

    def end_story(self):
        self.ladyBug.remove()
        self.bee.remove()
        self.waiting = False

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
        draw_text(self.game.screen, 32, text, x, y, color)

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
        while self.waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.waiting = False
                    self.game.close_game()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_buttons()

            self.game.screen.fill(PINK)
            self.draw_buttons()
            self.game.all_sprites.draw(self.game.screen)
            self.game.clock.tick(FPS)
            self.story_one()
            pygame.display.update()

    def ending(self):
        pass
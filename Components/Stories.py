import pygame

class Stories:
    def __init__(self, game):
        self.game = game
        self.waiting = True

    def beggining(self):
        while self.waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.waiting = False
                    self.game.close_game()

    def ending(self):
        pass
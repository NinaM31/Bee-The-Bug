import sys
import pygame

from Game import Game

if __name__ == '__main__':

    game = Game()
    game.game_over()
    game.new()

    while game.running:
        game.start()
        game.game_over()
    
    pygame.quit()
    sys.exit()
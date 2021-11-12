import sys
import pygame

from GameLogic.Game import Game

if __name__ == '__main__':

    game = Game()
    game.game_intro()
    game.new()

    while game.running:
        game.start()
        game.game_over()
    
    pygame.quit()
    sys.exit()
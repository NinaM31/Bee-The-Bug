import sys
import pygame

from GameLogic.Game import Game

if __name__ == '__main__':
    game = Game()
    game.game_intro()
 
    while game.running:
        game.play()
    
    pygame.quit()
    sys.exit()
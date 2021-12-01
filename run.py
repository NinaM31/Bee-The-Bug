import pygame

from GameLogic.Game import Game

if __name__ == '__main__':
    game = Game()
    
    while game.running:
        game.game_intro()
        game.play()
        game.game_over()
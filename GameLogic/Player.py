import math
import pygame

from Components.Config import PLAYER_LAYER, TILESIZE, PLAYER_SPEED


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.moving_audio = pygame.mixer.Sound("assets/moving.mp3")

        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = game.character_spritesheet.get_sprite(0, 0, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.facing = 'down'
        self.animation_loop = 0

        self.down_animations = [
            self.game.character_spritesheet.get_sprite(0, 0, TILESIZE, TILESIZE),
            self.game.character_spritesheet.get_sprite(32, 0, TILESIZE, TILESIZE),
            self.game.character_spritesheet.get_sprite(64, 0, TILESIZE, TILESIZE)
        ]

        self.left_animations = [
            self.game.character_spritesheet.get_sprite(0, 32, TILESIZE, TILESIZE),
            self.game.character_spritesheet.get_sprite(32, 32, TILESIZE, TILESIZE),
            self.game.character_spritesheet.get_sprite(64, 32, TILESIZE, TILESIZE),
        ]

        self.right_animations = [
            self.game.character_spritesheet.get_sprite(0, 64, TILESIZE, TILESIZE),
            self.game.character_spritesheet.get_sprite(32, 64, TILESIZE, TILESIZE),
            self.game.character_spritesheet.get_sprite(64, 64, TILESIZE, TILESIZE),
        ]

        self.up_animations = [
            self.game.character_spritesheet.get_sprite(0, 96, TILESIZE, TILESIZE),
            self.game.character_spritesheet.get_sprite(32, 96, TILESIZE, TILESIZE),
            self.game.character_spritesheet.get_sprite(64, 96, TILESIZE, TILESIZE),
        ]

    def update(self):
        self.movement()
        self.animate()

        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')

        self.y_change = 0
        self.x_change = 0
    
    def animate(self):
        if self.facing == 'down':
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 0, TILESIZE, TILESIZE)
            else:
                self.image = self.down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.05

                if self.animation_loop > 3:
                    self.animation_loop = 1
        
        if self.facing == 'up':
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 96, TILESIZE, TILESIZE)
            else:
                self.image = self.up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.05

                if self.animation_loop > 3:
                    self.animation_loop = 1

        if self.facing == 'left':
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 32, TILESIZE, TILESIZE)
            else:
                self.image = self.left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.05

                if self.animation_loop > 3:
                    self.animation_loop = 1

        if self.facing == 'right':
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 64, TILESIZE, TILESIZE)
            else:
                self.image = self.right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.05

                if self.animation_loop > 3:
                    self.animation_loop = 1

    def make_sound(self):
        self.moving_audio.play()

    def collide_bridge(self, direction):
        pass
        # if direction == 'x':
        #         if self.x_change > 0:
        #             self.move_sprite_left()
        #         if self.x_change < 0:
        #             self.move_sprite_right() 
                    
        # if direction == 'y':
        #     if self.y_change > 0:
        #         self.move_sprite_up()
        #     if self.y_change < 0:
        #         self.move_sprite_down()

    def collide_blocks(self, direction):
        onBridge = pygame.sprite.spritecollide(self, self.game.bridge_sprites, False)

        if not onBridge:
            hits = pygame.sprite.spritecollide(self, self.game.obstacle_sprites, False)
            if direction == 'x':
                if hits:
                    if self.x_change > 0:
                        self.move_sprite_left()
                        self.rect.x = hits[0].rect.left - self.rect.width
                        
                    if self.x_change < 0:
                        self.move_sprite_right()
                        self.rect.x = hits[0].rect.right

            if direction == 'y':
                if hits:
                    if self.y_change > 0:
                        self.move_sprite_up()
                        self.rect.y = hits[0].rect.top - self.rect.height

                    if self.y_change < 0:
                        self.move_sprite_down()
                        self.rect.y = hits[0].rect.bottom
        else:
            self.collide_bridge(direction)

    def move_sprite_left(self):
        for sprite in self.game.all_sprites:
                sprite.rect.x += PLAYER_SPEED

    def move_sprite_right(self):
        for sprite in self.game.all_sprites:
                sprite.rect.x -= PLAYER_SPEED

    def move_sprite_up(self):
        for sprite in self.game.all_sprites:
                sprite.rect.y += PLAYER_SPEED
    
    def move_sprite_down(self):
        for sprite in self.game.all_sprites:
                sprite.rect.y -= PLAYER_SPEED

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.make_sound()
            self.move_sprite_left()
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'

        if keys[pygame.K_RIGHT]:
            self.make_sound()
            self.move_sprite_right()
            self.x_change += PLAYER_SPEED
            self.facing = 'right' 
        
        if keys[pygame.K_UP]:
            self.make_sound()
            self.move_sprite_up()
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
                  
        if keys[pygame.K_DOWN]:
            self.make_sound()
            self.move_sprite_down()
            self.y_change += PLAYER_SPEED
            self.facing = 'down'  
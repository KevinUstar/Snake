# © 2019 KidsCanCode LLC / All rights reserved.
# import setting varibles and pygame
import pygame as pg
from settings import *

# player class
class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x * TILESIZE 
        self.y = y * TILESIZE
# velocity in one direction is always positive for one direction, so the snake is always moving 
    def get_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.vx = -PLAYER_SPEED
            self.vy = 0
        elif keys[pg.K_d]:
            self.vx = PLAYER_SPEED
            self.vy = 0
        elif keys[pg.K_w]:
            self.vy = -PLAYER_SPEED
            self.vx = 0
        elif keys[pg.K_s]:
            self.vy = PLAYER_SPEED
            self.vx = 0
#creates a body segment at player x and y each time space is pressed.
        if keys[pg.K_SPACE]:
            x = self.x/TILESIZE
            y = self.y/TILESIZE
            Body(self.game, x, y)
            print(len(self.game.body))
# if the player collides with a wall, the velocity of the side that collided is turned to 0. this way, you can slide up walls
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y

    def update(self):
        self.get_keys()
        self.x += self.vx       
        self.y += self.vy 
        self.rect.x = self.x
        self.rect.y = self.y
        self.collide_with_walls('x')
        self.collide_with_walls('y')
        
        
# create body of snake Class
class Body(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.body
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

# create wall Class
class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
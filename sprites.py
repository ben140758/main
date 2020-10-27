# Page dedicated to sprites
import pygame as pg
from settings import *

vector = pg.math.Vector2


#The player

class Player(pg.sprite.Sprite):
  def __init__(self, game):
    self.group = game.AllSpriteGroup
    pg.sprite.Sprite.__init__(self, self.group)
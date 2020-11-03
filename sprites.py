# Page dedicated to sprites
import pygame as pg
from settings import *


# pygame in-built 2D vector maths
vector = pg.math.Vector2()

#The player
class Player(pg.sprite.Sprite):
  def __init__(self, game):
    self.game = game
    self.group = game.AllSpriteGroup

    pg.sprite.Sprite.__init__(self, self.group)

    self.image = pg.image.load(PLAYER_SPRITE).convert()
    self.image.set_colorkey(WHITE)

    # Get the 
    self.rect = self.image.get_rect()

    # player stats
    self.health = PLAYER_HEALTH # set the health to the initial value found in settings.py
    self.position = vector # set the initial starting positions type to ph.math.Vector2()
    self.position.xy = (PLAYER_START_X, PLAYER_START_Y) # set the coordinates for the players starting position
    self.velocity = vector
    self.velocity.xy = 0, 0 # changing this value will give the player an initial velocity
    self.acceleration = vector
    self.acceleration.xy = 0, 0

  def damage(self): 
    self.health -= 1 # reduce the players health by 1
    if self.health <= 0: # if they have 0 or less health then call the die function
      self.die()

  def die(self):
    pass # do dying stuff

  def move(self):
    # to move the player, update the velocity to some other values based on user input. 
    # e.g. if they press A then set the velocity to -1, 0 to make them move left (i believe)
    # if they press both A and W, make sure to set the velocity to -1, 1 instead
    # not sure how acceleration plays into this yet (look at line 53)

    self.velocity.xy = 0, 0 # reset the velocity so that the user doesn't keep moving after letting go of a button
                            # if there's any problems feel free to remove it and implement your own solution.

    # do movement stuff here, take inputs and change velocity depending on inputs
    pass
    
  def update(self):
    # most of this section could be moved to move()
    self.acceleration = vector
    self.acceleration.xy = 0, PLAYER_GRAVITY
    #Increase or decrease X acceleration by keypress
    self.velocity.xy += self.acceleration.xy # increase / decrease velocity depending on acceleration
    self.position = self.position.xy + self.velocity.xy # increase the current position by the velocity of the player
    self.rect.center = self.position # set the players position on the screen


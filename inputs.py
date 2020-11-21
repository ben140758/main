import pygame as pg
from enums import Direction
from settings import PLAYER_MOVE_SPEED

class InputHandler():
  def __init__(self, player):
    self.player = player # initialize the player variable to be used in both the Move and Jump class

    self.move = Move(self.player) # initialize the move variable with an instance of the Move class
    self.jump = Jump(self.player) # intiailize the jump varaible with an instance of the Jump class
    # both classes take in an instance of the player to avoid using a singleton or this class passing itself (not necessary)

    pg.key.set_repeat(50,50) # set the key repeat to after 50 milliseconds, every 50 milliseconds, this allows for continuous movement with keypresses

  def update(self):
    for event in pg.event.get(): # get all of the events in this current iteration of update
        if event.type == pg.QUIT: # if the user wants to quit, allow them to do so
          pg.quit(); # quit the game

        if event.type == pg.KEYDOWN: # if the user presses a key down
          if event.key == pg.K_LEFT or event.key == ord('a'): # if the key is the A key
            self.move.execute(Direction.LEFT) # move the player left using the move class instance and a direction

          if event.key == pg.K_RIGHT or event.key == ord('d'): # if the key is the D key
            self.move.execute(Direction.RIGHT) # move the player right using the move class instance and a direction

          if event.key == pg.K_UP or event.key == ord('w') or event.key == pg.K_SPACE: # if the key is SPACE
            self.jump.execute() # make the player jump by calling execute on the jump class instance


class Move():
  def __init__(self, player):
    self.player = player # initialize the player variable for use later

  def execute(self, direction):
    if direction == Direction.LEFT: # if the given direction is left
      self.player.control(-PLAYER_MOVE_SPEED, 0) # move the player left

    elif direction == Direction.RIGHT: # if the given direction is right
      self.player.control(PLAYER_MOVE_SPEED,0) # move the player right

class Jump():
  def __init__(self, player):
    self.player = player # initialize the player variable for use layer

  def execute(self):
    self.player.jump() # call the jump method of the player class


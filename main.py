import pygame as pg
import random

from settings import* # Put any game constants in here e.g. WIDTH and HEIGHT
from sprites import* # Put all moving objects in here e.g. Players and Platforms

class Game:
  def __init__(self):

    # Initialise game window
    pg.init()
    pg.font.init()
    self.screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption(TITLE)
    self.clock = pg.time.Clock()
    self.font_name = pg.font.match_font(FONT_NAME)
    self.running = True
    self.GameLoop()

  def InitialiseNewGame(self):
    # a group of sprites can be grouped with pg.sprite.group
    self.AllSpriteGroup = pg.sprite.group()

  def GameLoop(self):
    self.PlayerAlive = True
    while self.PlayerAlive:
      self.clock.tick(FPS)
      self.events()
      self.update()
      self.draw()

  def events(self):
    pass

  def update(self):
    pass

  def draw(self):
    pass

  def ShowStartScreen(self):
    pass

  def ShowEndScreen(self):
    pass


if __name__ == "__main__":
  #initialise game + loop
  game = Game()
  game.ShowStartScreen()

  while game.running:
    game.InitialiseNewGame()
    game.ShowEndScreen()
  
  pg.quit()



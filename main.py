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

    self.InitialiseNewGame()
    self.GameLoop()

  def InitialiseNewGame(self):
    # a group of sprites can be grouped with pg.sprite.group
    self.AllSpriteGroup = pg.sprite.Group()
    self.allSpriteGroups = [self.AllSpriteGroup]
    self.player = Player(self)
    self.AllSpriteGroup.add(self.player)

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
    # Try moving the player sprite
    self.player.update()


  def draw(self):
    self.screen.fill(BGCOLOUR)
    [group.draw(self.screen) for group in self.allSpriteGroups]
    pg.display.flip()

  def ShowStartScreen(self):
    pass

  def ShowEndScreen(self):
    pass

if __name__ == "__main__":
  #initialise game + loop
  print("HI")
  game = Game()
  game.ShowStartScreen()

  while game.running:
    game.InitialiseNewGame()
    game.ShowEndScreen()
  
  pg.quit()



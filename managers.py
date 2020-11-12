# all the managers needed for the game, likely where the score will go
import pygame as pygame

class BulletManager(): # the class that manages bullet movement and rendering, that way enemies are independent of the bullets they fire meaning if they die the bullets will still be able to move
  def __init__(self, game):
    self.bullets = [] # initialize a bullet array

    self.game = game

  def add_bullet(self, bullet):
    self.bullets.append(bullet) # add the new bullet to the bullets array
    self.game.AllSpriteGroup.add(bullet) # add the sprite to the AllSpriteGroup to be rendered

  def remove_bullet(self, bullet):
    self.bullets.remove(bullet) # remove the bullet from the bullets array
    self.game.AllSpriteGroup.remove(bullet) # remove the sprite from the allspritegroup so it's no longer rendered

  def update(self):
    for bullet in self.bullets:
      bullet.update() # update each bullet in the bullets array

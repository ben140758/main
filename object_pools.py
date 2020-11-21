from sprites import Enemy, Platform, Item
from enums import PlatformType


class EnemyPool:
  def __init__(self, game, poolSize):
    self.game = game
    self.enemiesInUse = self.game.enemiesInUse
    self.enemiesNotInUse = self.game.enemiesNotInUse
    self.POOL_SIZE = poolSize  

  def allocate_enemy(self, x, y, amountOfMutations):
    if len(self.enemiesNotInUse) > 0:
      print()
      newEnemy = self.game.enemiesNotInUse.pop()
      newEnemy.init(x, y)
      self.game.enemiesInUse.append(newEnemy)
    
    elif len(self.enemiesInUse) < self.POOL_SIZE:
      newEnemy = Enemy(self.game)
      newEnemy.init(x, y)
      self.game.enemiesInUse.append(newEnemy)

    else: 
      return None

  def update_all(self):
    for enemy in self.enemiesInUse:
        # get rid of removed enemies
        if not enemy.inUse:
          enemy.kill()
          self.enemiesNotInUse.append(enemy)
          self.enemiesInUse.remove(enemy)
        
        # update all enemies
        enemy.update()




class PlatformPool:
  def __init__(self, game, poolSize):
    self.game = game

    self.POOL_SIZE = poolSize
    self.platformsInUse = []
    self.platformsNotInUse = []

  def allocate_platform(self, x, y, p_type):
    # get new platform from unused list if there is one
    if len(self.platformsNotInUse) > 0: 
      newPlatform = self.platformsNotInUse.pop()
      newPlatform.init(x, y, p_type)
      self.platformsInUse.append(newPlatform)
      

    # create new platform and add it to the used list if there is no unused platforms.
    elif len(self.platformsInUse) < self.POOL_SIZE:
      newPlatform = Platform(self.game)
      newPlatform.init(x, y, p_type)
      self.platformsInUse.append(newPlatform)

    # pool is full so no platforms to allocate
    else:
      return None

  def update_all(self):

    for platform in self.platformsInUse:
      # get rid of removed platforms
      if not platform.inUse:
        platform.kill()
        self.platformsNotInUse.append(platform)
        self.platformsInUse.remove(platform)

      # update all platforms
      else:
        platform.update()



class ItemPool:
  pass

'''class Pool:
  def __init__(self, game, enemyCount, platformCount, itemCount):
    self.game = game
    # seperate pools of objects
    self.enemies = [Enemy(game) for count in range(enemyCount)]
    self.enemiesInUse = 0
    self.platforms = [Platform(game) for count in range(platformCount)]
    self.platformsInUse = 0
    #self.items = [Item() for count in range(itemCount)]
    self.maxEnemyCount = enemyCount
    self.maxPlatformCount = platformCount
    self.maxItemCount = itemCount

  # called from main, initialise an enemy if there is any spare
  def create_enemy(self): #enemyType, mutations):
    # take an enemy object from the enemies list
    if len(self.enemies) != 0:
        topEnemy = self.enemies.pop()
        topEnemy.init()
        #self.game.allSpriteGroups.append(topEnemy)
        return topEnemy
        
    # if there are no enemies left to give, return nothing
    return None

  def free_enemy(self, enemy):
    # if a non-enemy sprite is passed into this method
    if (type(enemy) != Enemy):
      return
    #self.game.AllSpritesGroup.remove(enemy)
    enemy.kill()
    enemy.reset()
    if len(self.enemies) < self.maxEnemyCount:
      self.enemies.append(enemy)

  def create_platform(self, x, y):
    if len(self.platforms) != 0:
      topPlatform = self.platforms.pop()
      topPlatform.init(x, y, PlatformType.DEFAULT)      
      return topPlatform

  def free_platform(self, platform):
    # if it isn't platform that is passed as a parameter, end function
    if type(platform) != Platform:
      return
    
    platform.kill()
    platform.rect.x = 0
    platform.rect.y = 0
    if len(self.platforms) < self.maxPlatformCount:
      self.platforms.append(platform)

  def create_item(self, itemType):
    pass
  
  def free_item(self, item):
    pass'''

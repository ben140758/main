import pygame as pg
import random

from settings import * # Put any game constants in here e.g. WIDTH and HEIGHT
from sprites import * # Put all moving objects in here e.g. Players and Platforms
from managers import * # import all the managers from managers.py
from object_pools import Pool, PlatformPool # import object pool

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
    self.Enemies = pg.sprite.Group()
    self.spriteGroups = [self.AllSpriteGroup, self.Enemies]
    self.enemiesInUse = []
    
    self.player = Player(self)
    self.AllSpriteGroup.add(self.player)

    self.bullet_manager = BulletManager(self)

    self.objectPool = Pool(self, ENEMY_COUNT, PLATFORM_COUNT, ITEM_COUNT)

    # test code, initializes an enemy for testing purposes
    newEnemy = self.objectPool.create_enemy()
    self.platformPool = PlatformPool(self, 10)
    # if any enemelies left in the object pool, spawn the enemies
    if (newEnemy != None):
      self.enemiesInUse.append(newEnemy)

    # test create Platform

    #newPlatform = self.objectPool.create_platform(300, 30)
    self.platformPool.allocate_platform(300, 30, PlatformType.DEFAULT)
    self.player.position.y = 50
      
    '''self.enemy = Enemy(self)
    self.enemy.init(self)
    self.AllSpriteGroup.add(self.enemy)'''



  def GameLoop(self):
    self.PlayerAlive = True
    self.ticksFromStart = 0 # track time using the frame rate, e.g. spawn an enemy in two seconds = spawn enemy in FPS * amount of seconds = 120 ticks
    while self.PlayerAlive:
      self.clock.tick(FPS)
      self.events()
      self.update()
      self.draw()
      self.update()  # update player position

  def events(self):
    # test spawn enemies every two seconds
    '''if (self.ticksFromStart % 120 == 0):
        newEnemy = self.objectPool.create_enemy()
        if (newEnemy != None):
          self.enemiesInUse.append(newEnemy)
        
          #enemyList = [x for x in self.AllSpriteGroup.sprites()]
          #[print(type(x) == Enemy) for x in enemyList]
          #onlyEnemies = [x for x in enemyList if type(x) == Enemy]
          #print(f'{onlyEnemies}\n')'''

    # getting keypress from user 
    for event in pygame.event.get():
        # best moving some of this into the player sprite
        if event.type == pygame.QUIT:
            pygame.quit(); quit()#sys.exit()
            main = False
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left')
                self.player.control(-PLAYER_MOVE_SPEED,0)
          if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right')
                self.player.control(PLAYER_MOVE_SPEED,0)
          if event.key == pygame.K_UP or event.key == ord('w') or event.key == pygame.K_SPACE:
                print('jump')
                # player.jump()
                

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left stop')
                #self.player.control(PLAYER_MOVE_SPEED,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right stop')
                #self.player.control(-PLAYER_MOVE_SPEED,0)
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False    

    #print(len([x for x in self.AllSpriteGroup.sprites() if type(x) == Bullet]))

    self.ticksFromStart += 1

  #testing putting enemies back in the object pool
    '''if (self.ticksFromStart % 300 == 0):
      enemy = self.enemiesInUse.pop()
      self.objectPool.free_enemy(enemy)'''

  def update(self):
    # Try moving the player sprite
    self.player.update()

    # update the bullet manager
    self.bullet_manager.update()

    self.platformPool.update_all()
    # test code
    [enemy.update() for enemy in self.enemiesInUse]


  def draw(self):
    # set background colour
    self.screen.fill(BGCOLOUR)
    
    # draw all sprites onto the screen
    [group.draw(self.screen) for group in self.spriteGroups]

    # tell pygame to stop drawing and to start processing again
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



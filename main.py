import pygame as pg
import random

from settings import * # Put any game constants in here e.g. WIDTH and HEIGHT
from sprites import * # Put all moving objects in here e.g. Players and Platforms
from managers import * # import all the managers from managers.py
from object_pools import EnemyPool, PlatformPool # import object pool
from inputs import InputHandler # import the input handler class from the inputs file

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
    self.enemiesSpawned = 0
    self.player = Player(self)
    self.AllSpriteGroup.add(self.player)
    self.enemyspawntime = 30
    self.enemiesInUse = []
    self.enemiesNotInUse = []

    self.inputHandler = InputHandler(self.player); # create an instance of the input handler

    self.bullet_manager = BulletManager(self)

    self.enemyPool = EnemyPool(self, ENEMY_COUNT)

    # test code, initializes an enemy for testing purposes
    #newEnemy = self.enemyPool.allocate_enemy(300, 30)
    self.platformPool = PlatformPool(self, 20)


    while len(self.platformPool.platformsInUse) < 10:
      self.platformPool.allocate_platform(random.randint(0, 700), random.randint(0, 500), PLATFORM_DEFAULT_TYPE)
    # test create Platform

    #newPlatform = self.objectPool.create_platform(300, 30)
    # line of code to create a platform
    self.player.position.xy = 300, 50
    self.platformsSpawned = 0
      
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
    '''for event in pygame.event.get():
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
                self.player.jump()
                

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left stop')
                #self.player.control(PLAYER_MOVE_SPEED,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right stop')
                #self.player.control(-PLAYER_MOVE_SPEED,0)
            if event.key == ord('q'):
                pg.quit()
                sys.exit()
                main = False    '''

    #print(len([x for x in self.AllSpriteGroup.sprites() if type(x) == Bullet]))

    self.ticksFromStart += 1

  #testing putting enemies back in the object pool
    '''if (self.ticksFromStart % 300 == 0):
      enemy = self.enemiesInUse.pop()
      self.objectPool.free_enemy(enemy)'''

  def update(self):
    # update the input handler
    self.inputHandler.update()

    # Try moving the player sprite
    self.player.update()

    # update the bullet manager
    self.bullet_manager.update()

    # check if any enemies are falling off of the screen
    for enemy in self.enemyPool.enemiesInUse:
      if enemy.position.y > 600:
        enemy.inUse = False

    # check if any platforms are falling off of the screen
    for platform in self.platformPool.platformsInUse:
      if platform.rect.y > 600:
        platform.inUse = False

    while len(self.platformPool.platformsInUse) < 10:
      # preferrably make this part into a function
      # seperate generation for safe platforms
      # try to make the platforms not group
      x = random.randint(0, 700)
      y = random.randint(-50, 0)
      self.platformPool.allocate_platform(x, y, PlatformType.DEFAULT)
      if len(self.enemyPool.enemiesInUse) < 10:
        if self.platformsSpawned % 10 == 0:
          randomRangeX = random.randint(x, x + 100)
          
          self.enemyPool.allocate_enemy(randomRangeX,y-21, 0)
          
          
      self.platformsSpawned += 1

        
    #if self.ticksFromStart% 60 is 0 and self.enemyspawntime >1:
      #self.enemyspawntime = self.enemyspawntime - 1
      
    self.enemyPool.update_all()
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



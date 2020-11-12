# Page dedicated to sprites
import pygame as pg
from settings import *
from enums import *
import time  # needed for adding a delay to the attacking of the enemy


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
        self.health = PLAYER_HEALTH  # set the health to the initial value found in settings.py
        self.position = pg.math.Vector2(
        )  # set the initial starting positions type to ph.math.Vector2()
        self.position.xy = (
            PLAYER_START_X, PLAYER_START_Y
        )  # set the coordinates for the players starting position
        self.velocity = pg.math.Vector2()
        self.velocity.xy = 0, 0  # changing this value will give the player an initial velocity

        self.acceleration = pg.math.Vector2()
        self.acceleration.xy = 0, 0

        # player movement variables
        self.movex = 0 # move along X
        self.movey = 0 # move along Y
        self.frame = 0 # count frames
        """
        # jump variables
        self.is_jumping = True
        self.is_falling = False
        """
        # function to make sprite move
    def control(self,x,y):
        '''self.movex += x
        self.movey += y'''
        self.acceleration.x = x
        """
        # gravity function for jumping 
    def gravity(self):
        if self.is_jumping:
            self.movey += 3.2

        # jump function
    def jump(self):
        if self.is_jumping is False:
            self.is_falling = False
            self.is_jumping = True
        """
    def damage(self, damage):
        self.health -= damage  # reduce the players health by damage
        if self.health <= 0:  # if they have 0 or less health then call the die function
            self.die()

        print("player damaged")

    def die(self):
        self.kill()  # do dying stuff

    def move(self):
        # to move the player, update the velocity to some other values based on user input.
        # e.g. if they press A then set the velocity to -1, 0 to make them move left (i believe)
        # if they press both A and W, make sure to set the velocity to -1, 1 instead
        # not sure how acceleration plays into this yet (look at line 53)

        self.velocity.xy = 0, 0  # reset the velocity so that the user doesn't keep moving after letting go of a button
        # if there's any problems feel free to remove it and implement your own solution.

        # do movement stuff here, take inputs and change velocity depending on inputs
        pass

    def update(self):
        # most of this section could be moved to move()
        #self.velocity.xy += self.acceleration.xy  # increase / decrease velocity depending on acceleration
        if (self.acceleration.x < 0):
          if (self.acceleration.x > -1):
            self.acceleration.x = 0
          else:
            self.acceleration.x += 0.5
        
        
        elif (self.acceleration.x > 0):
          if (self.acceleration.x < 1):
            self.acceleration.x = 0
          else:
            self.acceleration.x -= 0.5

        
        self.acceleration.x += self.velocity.x * PLAYER_FRICTION
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration
        #self.acceleration.xy = 0, 0#PLAYER_GRAVITY
        #Increase or decrease X acceleration by keypress
        self.position = self.position.xy + self.velocity.xy  # increase the current position by the velocity of the player
        self.rect.center = self.position  # set the players position on the screen

        # update sprite position on the screen
        #self.rect.x = self.rect.x + self.movex  
        #self.rect.y = self.rect.y + self.movey 
        
        ''''
        # plat_hit_list may need to be changed to suit our code
        # collision detection for sprite so it stops falling
        plat_hit_list = pygame.sprite.spritecollide(self, plat_list, False)
        for p in plat_hit_list:
            self.is_jumping = False  # stop jumping
            self.movey = 0

            # approach from below
            if self.rect.bottom <= p.rect.bottom:
               self.rect.bottom = p.rect.top
            else:
               self.movey += 3.2
        # may need to turn gravity on again after its touched a platform
        #self.is_jumping = True  # turn gravity on 
        # setting an amount of pixels to jump
        if self.is_jumping and self.is_falling is False:
            self.is_falling = True
            self.movey -= 33  # how high to jump
          '''
          
# enemies
class Enemy(pg.sprite.Sprite):

    # when the object pool is created
    def __init__(self, game):
        self.game = game  # establish the game variable
        self.inUse = False
        self.image = pg.image.load(
            ENEMY_SPRITE
        )  # load the image of the enemy, it already has transparency so no need for keying

        self.rect = self.image.get_rect()

        self.bullet_manager = game.bullet_manager  # the bullet manager instance

        self.player = game.player

    # when called from the object pool
    def init(self):
        self.group = self.game.AllSpriteGroup  # establish the group variable
        pg.sprite.Sprite.__init__(self, self.group)  # initialize the sprite
        self.game.AllSpriteGroup.add(
            self)  # add the sprite to the all sprites group
        self.health = ENEMY_HEALTH  # set the initial health of the enemy
        self.position = pg.math.Vector2(
        )  # set the position equal to a base vector, cannot be the same as any other enemy / player else it will update their position too
        self.position.xy = (
            ENEMY_START_X, ENEMY_START_Y
        )  # edit the base vector so that it starts at the initial position

        self.damage = ENEMY_DAMAGE
        self.damage_type = ENEMY_DEFAULT_DAMAGE_TYPE  # set the damage type to the default found in settings

        self.attack_period = ENEMY_DEFAULT_ATTACK_PERIOD  # set the attack period of the enemy found in settings
        self.time_to_reach = time.time(
        ) + self.attack_period  # initialize the time to reach variable so that it doesn't attack right away

        self.bullet_speed = BULLET_SPEED
        self.bullet_damage = ENEMY_DAMAGE

    # reset all variables before being put back in the object pool
    def reset(self):
        self.health = None
        self.position = None
        self.damage = None
        self.damage_type = None
        self.attack_period = None
        self.time_to_reach = None
        self.bullet_speed = None
        self.bullet_damage = None

    def take_damage(self):
        self.health -= 1  # deal 1 damage to this enemy
        if self.health <= 0:  # if the enemies health is less than or equal to 0
            self.die()  # call the die function to kill the enemy

    def die(self):
        # kill the enemy
        pass

    def move(self):
        # used for moving the enemy
        pass

    def set_damage_type(self, damage_type):
        self.damage_type = damage_type  # set the damage type of this enemy

    def damage_player(self):
        collide_check = pg.sprite.collide_circle(
            self, self.player)  # if the player and this enemy are touching

        if collide_check:
            self.player.damage(self.damage)  # damage the player

    def shoot(self):
        bullet = Bullet(
            self.game, self
        )  # create a new bullet passing the position of the enemy, the speed of the bullet, and the damage of the bullet
        self.bullet_manager.add_bullet(
            bullet)  # add the bullet to the bullet manager so it can move

    def mutate(self):
        # mutate all the statistics within this class when calling the mutate function
        pass

    def update(self):
        self.position.xy += (0, 0)
        self.rect.center = self.position  # set the position of the sprite on the screen

        # to stop the enemy from shooting, simply change its ENEMY_DEFAULT_DAMAGE_TYPE in settings.py to MELEE instead of RANGED
        if time.time(
        ) >= self.time_to_reach:  # if the current time is greater than or equal to the time to reach, the enemy should attack
            if self.damage_type == DamageType.MELEE:
                self.damage_player(
                )  # check if the player is near, if they are, damage them
            elif self.damage_type == DamageType.RANGED:
                self.shoot()  # call the shoot function

            self.time_to_reach = time.time(
            ) + self.attack_period  # reset the time to reach ready for the next attack


# Bullet
class Bullet(pg.sprite.Sprite):
    def __init__(self, game, enemy):
        self.game = game  # establish the game variable
        self.group = game.AllSpriteGroup  # establish the group variable

        pg.sprite.Sprite.__init__(self, self.group)  # initialize the sprite

        self.image = pg.image.load(
            BULLET_SPRITE
        )  # load the image of the bullet, it already has transparency so no need for keying

        self.rect = self.image.get_rect()

        self.position = pg.math.Vector2(
        )  # set the position equal to a base vector, cannot be the same as any other bullet
        self.position.xy = (
            enemy.position.x, enemy.position.y
        )  # edit the base vector so that it starts at the initial position

        self.speed = enemy.bullet_speed  # initialize the speed variable of this bullet

        self.damage = enemy.bullet_damage  # initialize the damage variable of this bullet

        self.player = game.player  # initialize the player variable, used for collision detection

    def check_collision(self):
        collide_check = pg.sprite.collide_circle(
            self, self.
            player)  # check for collision between the bullet and the player

        if collide_check:  # if they collide
            self.player.damage(self.damage)  # damage the player
            self.game.bullet_manager.remove_bullet(
                self)  # remove the bullet from the bullet manager

    def move(self):
        self.position = self.position.xy + (0, -self.speed
                                            )  # make the bullet go upwards

    def update(self):
        self.move()  # move the bullet
        self.check_collision()  # check for collisions

        self.rect.center = self.position  # set the position on the screen

#platform's x and y location, the img width and height, img file
class Platform(pg.sprite.Sprite):
    def __init__(self,game):
      #pg.sprite.Sprite.__init__(self)
      self.game = game
      self.image = pg.image.load(PLATFORM_SPRITE).convert()
      self.image.convert_alpha()
      self.image.set_colorkey(WHITE)
      self.rect = self.image.get_rect()
      self.platformType = PLATFORM_DEFAULT_TYPE # the type of platform that this is, safe or default

      self.stoodOn = False # if this platform has been stood on or not
      self.safeTime = 0 # the time allowed for safety on a platform, x seconds before the platform will start to decay
      self.time = 0 # the current time the platform has been stood on for

      self.inUse = False

    # for when creating a platform from the object pool
    def init(self, x, y, p_type):
      self.group = self.game.AllSpriteGroup  # establish the group variable
      pg.sprite.Sprite.__init__(self, self.group)  # initialize the sprite
      self.game.AllSpriteGroup.add(self)
      self.rect.x = x
      self.rect.y = y
      self.platformType = p_type # the type of platform that this is, safe or default

      self.stoodOn = False # if this platform has been stood on or not
      self.safeTime = 0 # the time allowed for safety on a platform, x seconds before the platform will start to decay
      self.time = 0 # the current time the platform has been stood on for

      self.inUse = True


    # if the player stands on this platform
    def stood_on(self):
      self.time = time.time() + PLATFORM_DEFAULT_TIME_LIMIT # make a timer for the default time 

      self.stoodOn = True # a boolean to determine if this platform has been stood on

      if self.platformType == PlatformType.SAFE: # if this is a safe platform, also include a small delay before decaying begins
        self.safeTime = time.time() + PLATFORM_SAFE_TIME_LIMIT # set the safe time
        self.time += PLATFORM_SAFE_TIME_LIMIT # also increase the default time to account for this safe time

    # for scrolling screen
    def update(self):
      self.rect.y -= 0.1 # for scrolling screen

      if self.stoodOn: # if this platform has been stood on
        if time.time() >= self.safeTime: # if the safe time has been reached
          self.rect.y -= 0.01 # move the platform down if it is decaying, adds visual feedback
          if time.time() >= self.time: # if the total time has been reached
            # destroy this platform
            self.inUse = False # should remove it from the screen and add it back to the platform pool


class Item(pg.sprite.Sprite):
    def __init__(self):
        self.pos = (0, 0)

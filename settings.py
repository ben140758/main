import os
from enums import *

TITLE = "SE DP Platformer Group Project"
WIDTH = 0
HEIGHT = 0
FPS = 60
FONT_NAME = "arial"

# Put Player properties (acceleration, friction, gravity, jump height. HERE)

PLAYER_SPRITE = os.path.join('images', 'player.png')

PLAYER_ACCELERATION = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAVITY = 0.01
JUMP_HEIGHT = 0
PLAYER_HEALTH = 3
PLAYER_START_X = 50
PLAYER_START_Y = 0

# amount of pixels in one step of the player
PLAYER_MOVE_SPEED = 3

# Put Enemy properties here (base speed, base health, base damage etc...)
ENEMY_COUNT = 10
ENEMY_SPRITE = os.path.join('images', 'enemy.png') # the sprite that is linked with the enemy

ENEMY_SPEED = 1 # the starting speed of the enemy, used for movement should it be needed
ENEMY_HEALTH = 1 # the starting health of the enemy
ENEMY_DAMAGE = 1 # the starting damage of the enemy
ENEMY_START_X = 50 # the starting y position of the enemy
ENEMY_START_Y = 100 # the starting x position of the enemy
ENEMY_DEFAULT_DAMAGE_TYPE = DamageType.RANGED # the default damage type of the enemy
ENEMY_DEFAULT_ATTACK_PERIOD = 2 # how often the enemy attacks, every 2 seconds currently

# Put Bullet properties here

BULLET_SPRITE = os.path.join('images', 'bullet.png') # the sprite of the bullet

BULLET_SPEED = 1 # the speed of the bullet

# platform properties here

PLATFORM_SPRITE = os.path.join('images', 'platform.png') # load the sprite of the platform

PLATFORM_COUNT = 10
PLATFORM_DEFAULT_TYPE = PlatformType.DEFAULT
PLATFORM_DEFAULT_TIME_LIMIT = 3 # the time before the platform fully decays, 3 seconds
PLATFORM_SAFE_TIME_LIMIT = 2 # the safe period of the safe platform, the platform wont start decaying for another 2 seconds

# item properties here

ITEM_COUNT = 10

# DEFINE COLOURS (for simplicity later)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 191, 255)
BROWN = (139, 69, 19)
DARKGREY = (64, 64, 64)
BGCOLOUR = BLACK
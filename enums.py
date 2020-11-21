from enum import Enum

# enums
# damage type enum to hold the different damage types, makes the code a little more easy to read as oppose to just using numbers or strings to represent the different types
class DamageType(Enum):
  MELEE = 1
  RANGED = 2

# platform type enum to hold the different platform types
class PlatformType(Enum):
  DEFAULT = 1
  SAFE = 2

class Direction(Enum):
  LEFT = 1
  RIGHT = 2
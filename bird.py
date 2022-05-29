
##############
# BIRD CLASS #
##############

import pygame
import constants as const

class Bird():
  
  def __init__(self, loc, sprites, curr_sprite) -> None:
    self.x = loc[0]
    self.y = loc[1]
    self.sprites = sprites
    self.displayed = curr_sprite
    
  def flap(self):
    self.y -= 25
  

################################
# HELPER FUNCTIONS FOR SPRITES #
################################

import pygame

def resize(sprites):
  resized_sprites = {}
  
  for key in sprites:
    element_size = sprites[key]
    new_w = element_size[0] * 1.5
    new_h = element_size[1] * 1.5
    new_size = (new_w, new_h)
    
    resized_sprites[key] = new_size
  
  return resized_sprites

def move_grass(grass_loc):
  if grass_loc[0] > -75:
    grass_loc[0] -= 3
  else:
    grass_loc[0] = 0
  
  return grass_loc
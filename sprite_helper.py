
################################
# HELPER FUNCTIONS FOR SPRITES #
################################

from xml.etree import ElementTree
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
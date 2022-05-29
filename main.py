import pygame
import sys
from bird import Bird
import constants as const
import sprite_helper as sprhelp

def main():
  # pygame setup
  pygame.init()
  game_clock = pygame.time.Clock()

  # set the display screen dimensions
  screen = pygame.display.set_mode(const.DIMENSIONS)
  
  # load sprites into a dictionary mapping name to the sprite image
  sprites = {}
  sprites["background_day"] = pygame.image.load(const.BG_DAY)
  sprites["background_night"] = pygame.image.load(const.BG_NIGHT)
  sprites["yellow_bird_down"] = pygame.image.load(const.Y_DOWN_FLAP)
  sprites["yellow_bird_mid"] = pygame.image.load(const.Y_MID_FLAP)
  sprites["yellow_bird_up"] = pygame.image.load(const.Y_UP_FLAP)
  
  # store the sizes of each sprite
  sprite_sizes = {}
  resized_sprites = {}
  for key in sprites:
    sprite_sizes[key] = sprites[key].get_size()
  
  resized_sprites = sprhelp.resize(sprite_sizes)
  
  # resize each sprite according to  in the dictionary
  sprites["background_day"] = pygame.transform.scale(sprites["background_day"], resized_sprites["background_day"])
  sprites["background_night"] = pygame.transform.scale(sprites["background_night"], resized_sprites["background_night"])
  sprites["yellow_bird_down"] = pygame.transform.scale(sprites["yellow_bird_down"], resized_sprites["yellow_bird_down"])
  sprites["yellow_bird_mid"] = pygame.transform.scale(sprites["yellow_bird_mid"], resized_sprites["yellow_bird_mid"])
  sprites["yellow_bird_up"] = pygame.transform.scale(sprites["yellow_bird_up"], resized_sprites["yellow_bird_up"])
  
  bird = Bird(const.CENTRE, sprites, sprites["yellow_bird_mid"])
  
  # flag `running` boolean to true to enter game loop
  running = True 

  # game loop
  while running:
    
    # check for user input
    for event in pygame.event.get():
      
      # quit the pygame window
      if event.type == pygame.QUIT:
        running = False
      
      if event.type == pygame.KEYDOWN:
        
        if event.key == pygame.K_ESCAPE:
          running = False
        
        if event.key == pygame.K_SPACE:
          bird.flap()
        
    # blit background image onto screen
    screen.blit(sprites["background_day"], (0,0))
    
    # blit bird image onto screen
    screen.blit(bird.displayed, (bird.x, bird.y))
    
    # flip the display
    pygame.display.flip()
    
    # run according to the set framerate
    game_clock.tick(const.FPS)


  # quit pygame
  pygame.quit()
  sys.exit()

if __name__ == "__main__":
  main()
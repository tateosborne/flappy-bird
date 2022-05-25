
import pygame
import sys
import constants as const

def main():
  # pygame setup
  pygame.init()
  game_clock = pygame.time.Clock()

  # set the display screen dimensions
  screen = pygame.display.set_mode(const.DIMENSIONS)

  # flag `running` boolean to true to enter game loop
  running = True

  # game loop
  while running:
    
    # check for user input
    for event in pygame.event.get():
      
      # quit the pygame window
      if event.type == pygame.QUIT:
        running = False
        
    # fill the screen background white
    screen.fill(const.WHITE)
    
    # flip the display
    pygame.display.flip()
    
    # run according to the set framerate
    game_clock.tick(const.FPS)


  # quit pygame
  pygame.quit()
  sys.exit()

if __name__ == '__main__':
  main()
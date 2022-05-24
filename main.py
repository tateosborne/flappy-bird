
import pygame
import constants as const

pygame.init()

# set the display screen dimensions
screen = pygame.display.set_mode(const.DIMENSIONS)

# flag boolean to true to enter game loop
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


# quit pygame
pygame.quit()
import pygame
import sys

# Initialize Pygame #
pygame.init()
clock = pygame.time.Clock()

# Set up the window #
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Astral Thread")

# Add this in the main loop after setting up the screen #
character_pos = [100, 100]
character_speed = 5 ## Change to adjust speed please:) ##


# Main game loop #
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ## Key pressed event for movement ##
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and character_pos[0] > 0: # Move left #
        character_pos[0]-= character_speed
    if keys[pygame.K_d] and character_pos[0] < screen_width # Move right #
        character_pos[0]+= character_speed
    if keys[pygame.K_w] and character_pos[1] > 0: # Move up #
        character_pos[1]-= character_speed
    if keys[pygame.K_s]and character_pos[1]< screen_height: ## Move down ##
        character_pos[1]+= character_speed



    # Load an image (make sure you have a background image)
    #background_image = pygame.image.load('background.png')

    # Fill the screen with the background image instead of black
    #screen.blit(background_image, (0, 0))
    

    ## Fill the Screen ##
    screen.fill((0, 0, 0))


    # Draw the Character #
    pygame.draw.rect(screen, (0, 255, 0), (character_pos[0], character_pos[1], 50, 50))

    ## Limit the frame rate ##
    clock.tick(60)

    ## Update the DIsplay ##
    pygame.display.flip()
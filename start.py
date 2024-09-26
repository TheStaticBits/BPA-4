import pygame
import json

with open("data/constants.json", "r") as file:
    constants: dict = json.load(file)

pygame.init()

clock = pygame.time.Clock()
FPS: int = 60 # relocate to a constants file soon

# Define screen size as 1200x675 (16:9 ratio)
screen = pygame.display.set_mode(constants["windowSize"], pygame.RESIZABLE)
pygame.display.set_caption("my game :]")

running = True


while running: # Everything happens here
    clock.tick(constants["FPS"])
    
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False

        # Check for window resize
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                print(" you pressed space lmao   !")
            elif event.key == pygame.K_BACKSPACE:
                print("he he he haw")
            elif event.key == pygame.K_RETURN:
                print("heee heeee heeeee hawwwwwww!")
            
                
    pygame.display.update() # END OF FRAME

pygame.quit()
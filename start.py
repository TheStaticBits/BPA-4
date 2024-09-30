import pygame
import json
from src.entity import Entity
from util.vect import Vect

with open("data/constants.json", "r") as file:
    constants: dict = json.load(file)

pygame.init()

clock = pygame.time.Clock()
FPS: int = 60 # relocate to a constants file soon

# Define screen size as 1200x675 (16:9 ratio)
screen = pygame.display.set_mode(constants["windowSize"], pygame.RESIZABLE)
pygame.display.set_caption("my game :]")

running = True

box1 = Entity(Vect(200, 200), Vect(50, 50))
box2 = Entity(Vect(100, 100), Vect(50, 50))

while running: # Everything happens here
    clock.tick(constants["FPS"])

    #get mouse position
    mousePos: Vect = Vect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    #set mouse pos to box2 pos
    box2.pos = mousePos

    if(box1.collide(box2)):
        print("collision")
    else:
        print("nuh uh")

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (box1.getPos().getX(), box1.getPos().getY(), box1.getSize().getX(), box1.getSize().getY()))
    pygame.draw.rect(screen, (0, 255, 0), (box2.getPos().getX(), box2.getPos().getY(), box2.getSize().getX(), box2.getSize().getY()))
    
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
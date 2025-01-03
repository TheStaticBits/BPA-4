import pygame
import json
import time
from src.entity import Entity
from src.util.vect import Vect
from src.player import Player
from src.tile import Tile
from src.tilemanager import TileManager

with open("data/constants.json", "r") as file:
    constants: dict = json.load(file)

with open("data/animData.json", "r") as file:
    animData: dict = json.load(file)

pygame.init()

clock = pygame.time.Clock()

# Define screen size as 1200x675 (16:9 ratio)
screen = pygame.display.set_mode(constants["windowSize"], pygame.RESIZABLE)
pygame.display.set_caption("my game :]")

player = Player(Vect(), animData["player"]["animations"], constants)

running = True

#box1 = Entity(Vect(200, 200), Vect(12, 12), None)
#box2 = Entity(Vect(100, 100), Vect(12, 12), None)
#box3 = Entity(Vect(500, 300), Vect(12, 12), animData["player"]["animations"])

inputs = {
    "left": False,
    "right": False,
    "up": False,
    "down": False
}

#print(Vect(1, -4).getSign().getY())
#print(Vect(3, 0).getSign().getY())

deltatime = 0
previousFrameTime: float = time.time() - 0.1

TileManager.getTileData()
levelThing = TileManager("data/data.txt", constants)

while running: # Everything happens here
    clock.tick(constants["FPS"])

    # calculate deltatime
    currentTime = time.time()
    deltaTime = currentTime - previousFrameTime
    previousFrameTime = currentTime

    print(1 / deltaTime) # FPS

    #get mouse position
    mousePos: Vect = Vect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    #set mouse pos to box2 pos
    #box2.pos = mousePos

    #if(box1.collide(box2)):
        #print("collision")
    #else:
        #print("nuh uh")


    screen.fill((0, 0, 0))

    #box1.draw(screen, None)
    #box2.draw(screen, None)
    #box3.draw(screen, "idle")
    
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

            elif event.key == pygame.K_UP:
                inputs["up"] = True
            elif event.key == pygame.K_DOWN:
                inputs["down"] = True
            elif event.key == pygame.K_LEFT:
                inputs["left"] = True
            elif event.key == pygame.K_RIGHT:
                inputs["right"] = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                inputs["up"] = False
            elif event.key == pygame.K_DOWN:
                inputs["down"] = False
            elif event.key == pygame.K_LEFT:
                inputs["left"] = False
            elif event.key == pygame.K_RIGHT:
                inputs["right"] = False





    #actual gameplay calculation stuff happens here
    player.update(deltaTime, inputs, levelThing)
    player.draw(screen)

    levelThing.drawTiles(screen)






    pygame.display.update() # END OF FRAME

pygame.quit()
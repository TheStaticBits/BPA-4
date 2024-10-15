from src.util.vect import Vect
import pygame

class Entity:
    def __init__(self, pos: Vect, size: Vect, animData: dict | None = None):
        self.pos: Vect = pos
        self.size: Vect = size
        #self.animData: dict = animData
        self.animMode: str = "basic"
        if animData is not None:
            self.animMode = "animated"
            self.animationList = animData["animations"]
            pass
            print("fix this [entity.py:Entity.__init__]")
            #once youve decided the format for the animdata, implement it in two modes:
            # 1. static / single image in spritesheet
            # 2. animated / multiple images in spritesheet
        
    def draw(self, surface, animation: str):
        pass
        if self.animMode == "basic":
            # Draw rectangle in place of entity
            pygame.draw.rect(surface, (255, 0, 0), (self.pos.getX(), self.pos.getY(), self.size.getX(), self.size.getY()))
        else:
            # Draw image in place of entity
            imgToDraw = pygame.image.load(self.animationList[animation]["path"])
            surface.blit(imgToDraw, (self.pos.getX(), self.pos.getY()))

    def update(self):
        pass

    def getSize(self):
        return self.size
    
    def getPos(self):
        return self.pos

    def collide(self, other):
        if (other.getPos().x < self.getPos().x + self.getSize().x 
        and other.getPos().x + other.getSize().x > self.getPos().x 
        and other.getPos().y < self.getPos().y + self.getSize().y 
        and other.getPos().y + other.getSize().y > self.getPos().y):
            return True
        return False

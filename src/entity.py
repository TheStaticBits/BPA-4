from src.util.vect import Vect
import pygame

class Entity:
    def __init__(self, pos: Vect, size: Vect, animData: dict | None = None, currentFrame: int = 0):
        self.pos: Vect = pos
        self.size: Vect = size
        #self.animData: dict = animData
        self.animMode: str = "basic"
        self.currentFrame: int = currentFrame
        self.remainingFrameDelay = 0.01
        if animData is not None:
            self.animMode = "animated"
            self.animationList = animData["animations"]
            self.preloadedSpritesheets = {}
            for key, animation in self.animationList.items():
                self.preloadedSpritesheets[key] = pygame.image.load(animation["path"]).convert_alpha()
        
    def draw(self, surface, animation: str):
        pass
        if self.animMode == "basic":
            # Draw rectangle in place of entity
            pygame.draw.rect(surface, (255, 0, 0), (self.pos.getX(), self.pos.getY(), self.size.getX(), self.size.getY()))
        else:
            # cut up spritesheet into n chunks, where n is frame count
            # draw each chunk in place of entity
            if self.animationList[animation]["frameCount"] > 1:
                boundingRect = pygame.Rect(self.currentFrame * self.size.getX(), 0, self.size.getX(), self.size.getY())
                spritePortion = self.preloadedSpritesheets[animation].subsurface(boundingRect)
                surface.blit(spritePortion, (self.pos.getX(), self.pos.getY()))
            else:
                surface.blit(self.preloadedSpritesheets[animation], (self.pos.getX(), self.pos.getY()))
                
    def update(self, deltatime: float, animation: str):
        # change current frame based on animation mode
        if self.animMode == "animated":
            self.remainingFrameDelay -= deltatime
            if self.remainingFrameDelay <= 0:
                self.currentFrame = (self.currentFrame + 1) % (self.animationList[animation]["frameCount"])
                self.remainingFrameDelay = self.animationList[animation]["delay"]

    def getSize(self):
        return self.size
    
    def getPos(self):
        return self.pos
    
    def getCurrentFrame(self):
        return self.currentFrame 

    def collide(self, other):
        if (other.getPos().x < self.getPos().x + self.getSize().x 
        and other.getPos().x + other.getSize().x > self.getPos().x 
        and other.getPos().y < self.getPos().y + self.getSize().y 
        and other.getPos().y + other.getSize().y > self.getPos().y):
            return True
        return False

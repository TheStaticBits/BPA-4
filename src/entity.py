from src.util.vect import Vect
import src.util.util as util
import pygame

class Entity:
    def __init__(self, pos: Vect, size: Vect, defaultAnim: str, animData: dict | None = None, currentFrame: int = 0):
        self.pos: Vect = pos
        self.size: Vect = size
        #self.animData: dict = animData
        self.animMode: str = "basic"
        self.currentFrame: int = currentFrame
        self.remainingFrameDelay = 0
        if animData is not None:
            self.animMode = "animated"
            self.animationList = animData
            self.preloadedSpritesheets = {}
            for key, animation in self.animationList.items():
                self.preloadedSpritesheets[key] = util.getImage(animation["path"])
            self.remainingFrameDelay = self.animationList[defaultAnim]["delay"]
            self.activeAnimation = defaultAnim
        
    def draw(self, surface, activeAnimation: str):
        if self.animMode == "basic":
            # Draw rectangle in place of entity
            pygame.draw.rect(surface, (255, 0, 0), (self.pos.getX(), self.pos.getY(), self.size.getX(), self.size.getY()))
        else:
            # Cut up spritesheet into n chunks, where n is frame count
            # Draw each chunk in place of entity
            if self.animationList[activeAnimation]["frameCount"] > 1:
                frameWidth = self.preloadedSpritesheets[activeAnimation].get_width() // self.animationList[activeAnimation]["frameCount"]
                boundingRect = pygame.Rect(self.currentFrame * frameWidth, 0, frameWidth, self.preloadedSpritesheets[activeAnimation].get_height())
                spritePortion = self.preloadedSpritesheets[activeAnimation].subsurface(boundingRect)
                surface.blit(spritePortion, (self.pos.getX(), self.pos.getY()))
            else:
                surface.blit(self.preloadedSpritesheets[activeAnimation], (self.pos.getX(), self.pos.getY()))

    def update(self, deltatime: float, activeAnimation: str):
        # Change current frame based on animation mode
        if self.animMode == "animated" and self.animationList[activeAnimation]["delay"] > 0:
            self.remainingFrameDelay -= deltatime
            if self.remainingFrameDelay <= 0:
                self.currentFrame = (self.currentFrame + 1) % (self.animationList[activeAnimation]["frameCount"])
                self.remainingFrameDelay = self.animationList[activeAnimation]["delay"]

    def changeActiveAnimation(self, newAnimation: str):
        self.activeAnimation = newAnimation

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

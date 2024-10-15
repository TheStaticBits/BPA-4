from util.vect import Vect
from src.entity import Entity
class Player(Entity):
    def __init__(self, pos: Vect, hitboxType: str, animData: dict):
        self.hitboxType = hitboxType

    def getPos(self):
        return self.pos
    
    def getHitboxType(self):
        return self.hitboxType
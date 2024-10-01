from util.vect import Vect
from src.entity import Entity
class Tile(Entity):
    def __init__(self, pos: Vect, hitboxType: str, animData: dict):
        super().__init__(pos, Vect(16, 16), animData)
        # todo: implement sprite stuff
        self.hitboxType = hitboxType
        """
        hitboxType = "damaging", "solid", "semisolid", "passable"
        """

    def getPos(self):
        return self.pos
    
    def getHitboxType(self):
        return self.hitboxType
    
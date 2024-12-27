from src.util.vect import Vect
from src.entity import Entity

class Tile(Entity):
    def __init__(self, pos: Vect, tileChar: str, TILE_DATA: dict):
        super().__init__(pos, Vect(16, 16), "default", TILE_DATA[tileChar]["animations"])
        self.hitboxType: str = TILE_DATA[tileChar]["hitboxType"]
        """
        hitboxType = "damaging", "solid", "semisolid", "passable"
        """

        self.isBreakable: bool = TILE_DATA[tileChar]["isBreakable"]

    # Gets the position omg
    def getPos(self):
        return self.pos
    
    # Gets the hitbox type omg
    def getHitboxType(self):
        return self.hitboxType
    

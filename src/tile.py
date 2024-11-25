from src.util.vect import Vect
from src.entity import Entity
import json

class Tile(Entity):
    @classmethod
    def getTileData(cls):
        with open("data/tileData.json", "r") as f:
            cls.TILE_DATA = json.load(f)

    def __init__(self, pos: Vect, tileChar: str):
        super().__init__(pos, Vect(16, 16), self.TILE_DATA[tileChar]["animData"])
        self.hitboxType = self.TILE_DATA[tileChar]["hitboxType"]
        """
        hitboxType = "damaging", "solid", "semisolid", "passable"
        """

    # Gets the position omg
    def getPos(self):
        return self.pos
    
    # Gets the hitbox type omg
    def getHitboxType(self):
        return self.hitboxType
    

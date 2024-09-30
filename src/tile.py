from util.vect import Vect
from src.entity import Entity
class Tile(Entity):
    def __init__(self, pos: Vect, hitboxType: str, animData: dict):
        super().__init__(pos, Vect(16, 16), animData)
        # implement sprite stuff
        self.hitboxType = hitboxType # 3 types of hitboxes: "blue" which are solid blocks, "red" which are spikes or damaging blocks, "green" which are one-way blocks (semi-solid)

    def getPos(self):
        return self.pos
    
    def getHitboxType(self):
        return self.hitboxType
    

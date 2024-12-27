from src.util.vect import Vect
from src.entity import Entity
from src.tile import Tile
import json

class TileManager:
    @classmethod
    def getTileData(cls):
        with open("data/tileData.json", "r") as f:
            cls.tileData = json.load(f)

    def __init__(self, filePath: str, constants: dict):
        self.tileList = []
        with open(filePath, "r") as f:
            lines = f.read().split("\n")
            print(lines)
            for y, line in enumerate(lines):
                for x, char in enumerate(line):
                    if self.tileData[char]["isStatic"] == True:
                        self.tileList.append(Tile(Vect(x, y) * constants["tileSize"], char, self.tileData))

    def drawTiles(self, surface):
        for tile in self.tileList:
            tile.draw(surface, "default")

    def getTileList(self):
        return self.tileList
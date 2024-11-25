from src.util.vect import Vect
from src.entity import Entity
from src.tile import Tile


class TileManager:
    def __init__(self, filePath: str, constants: dict):
        self.tileList = []
        with open(filePath, "r") as f:
            lines = f.readlines()
            for y, line in enumerate(lines):
                for x, char in enumerate(line):
                    self.tileList.append(Tile(Vect(x, y) * constants["tileSize"], char))


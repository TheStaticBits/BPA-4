from src.util.vect import Vect
from src.entity import Entity
from src.tilemanager import TileManager

class Player(Entity):
    def __init__(self, pos: Vect, animData: dict, constants: dict):
        super().__init__(pos, Vect(constants["playerSize"]), "idle", animData)
        self.velocity = Vect(0, 0)

    def getPos(self):
        return self.pos
    
    def getHitboxType(self):
        return self.hitboxType
    
    def getDisplayAnimation(self):
        if self.velocity.getMagnitude() > 0:
            return "walk"
        else:
            return "idle"
    
    def draw(self, surface):
        super().draw(surface, self.getDisplayAnimation())
    
    def update(self, deltaTime: float, inputs: dict, tileManager: TileManager):
        # this function will call a bunch of other functions and be used by the game loop to access all these functions
        self.handleInput(deltaTime, inputs)
        self.updatePosition(deltaTime, "x")
        self.checkTileCollision(deltaTime, tileManager, "x")
        self.updatePosition(deltaTime, "y")
        self.checkTileCollision(deltaTime, tileManager, "y")
        print(self.size)
        super().update(deltaTime, self.getDisplayAnimation())

    def checkTileCollision(self, deltaTime: float, tileManager: TileManager, axis: str):
        for tile in tileManager.getTileList():
            if self.collide(tile) and tile.getHitboxType() == "solid":
                # Warp player to side of tile dependent on their velocity in a given direction
                if self.velocity.getSign().get(axis) > 0:
                    self.pos.set(axis, tile.getPos().get(axis) - self.getSize().get(axis))
                else:
                    self.pos.set(axis, tile.getPos().get(axis) + tile.getSize().get(axis))
                self.velocity.set(axis, 0)

    def handleInput(self, deltaTime: float, inputs: dict):
        leftRightInputs = inputs["right"] - inputs["left"]
        upDownInputs = inputs["down"] - inputs["up"]

        self.velocity += Vect(leftRightInputs, 0) * deltaTime * 1600

        if leftRightInputs == 0:
            # Velocity decay
            if abs(self.velocity.x) > abs(1300 * deltaTime * self.velocity.getSign().x):
                self.velocity.x -= 1300 * deltaTime * self.velocity.getSign().x
            else:
                self.velocity.x *= 0.5

            #if its basically zero, set to 0
            if abs(self.velocity.x) < 0.1:
                self.velocity.x = 0

        self.velocity.y += upDownInputs * deltaTime * 1600
        # Swimming up/down


        #check if velocity is above max velocity, if so, clamp

        self.velocity.clampX(170)

        self.velocity.clampY(135)
        #note: change 1 to max velocity from constants.json

    def updatePosition(self, deltaTime: float, axis):
        # DELTATIME
        self.pos.set(axis, self.pos.get(axis) + self.velocity.get(axis) * deltaTime)
        
        if axis == "y":
            #gravity only exists in the y direction, obviously
            self.velocity.y += 700 * deltaTime

            #check if on ground if not already
            if self.pos.y >= 600:
                self.pos.y = 600
                self.velocity.y = 0
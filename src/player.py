from src.util.vect import Vect
from src.entity import Entity

class Player(Entity):
    def __init__(self, pos: Vect, animData: dict, constants: dict):
        super().__init__(pos, Vect(constants["playerSize"]), animData)
        self.velocity = Vect(0, 0)

    def getPos(self):
        return self.pos
    
    def getHitboxType(self):
        return self.hitboxType
    
    def update(self, deltaTime: float, inputs: dict):
        # this function will call a bunch of other functions and be used by the game loop to access all these ufnctions
        self.checkTileCollision(deltaTime)
        self.handleInput(deltaTime, inputs)
        self.updatePosition(deltaTime)
        pass

    def checkTileCollision(self, deltaTime: float):
        pass

    def handleInput(self, deltaTime: float, inputs: dict):
        #get inputs

        #update velocity
        leftRightInputs = inputs["right"] - inputs["left"]
        upDownInputs = inputs["down"] - inputs["up"]

        self.velocity += Vect(leftRightInputs, upDownInputs) * deltaTime

        #check if velocity is above max velocity, if so, clamp

        self.velocity.circularClamp(1)
        #note: change 1 to max velocity from constants.json

        pass

    def updatePosition(self, deltaTime: float):
        # DELTATIME
        self.pos += self.velocity 
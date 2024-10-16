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
    
    def draw(self, surface):
        super().draw(surface, "idle")
    
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

        self.velocity += Vect(leftRightInputs, 0) * deltaTime * 1000

        if leftRightInputs == 0:
            #velocity decay
            if abs(self.velocity.x) > abs(1300 * deltaTime * self.velocity.getSign().x):
                self.velocity.x -= 1300 * deltaTime * self.velocity.getSign().x
            else:
                self.velocity.x *= 0.5
            #if its basically zero, set to 0
            if abs(self.velocity.x) < 0.1:
                self.velocity.x = 0

        #check if velocity is above max velocity, if so, clamp

        self.velocity.clampX(170)

        self.velocity.clampY(190)
        #note: change 1 to max velocity from constants.json

        pass

    def updatePosition(self, deltaTime: float):
        # DELTATIME
        self.pos += self.velocity * deltaTime
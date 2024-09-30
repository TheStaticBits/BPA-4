from util.vect import Vect
class Entity:
    def __init__(self, pos: Vect, size: Vect):
        self.pos: Vect = pos
        self.size: Vect = size
        #self.animData: dict = animData

    def update(self):
        pass

    def getSize(self):
        return self.size
    
    def getPos(self):
        return self.pos

    def collide(self, other):
        if (other.getPos().x < self.getPos().x + self.getSize().x 
        and other.getPos().x + other.getSize().x > self.getPos().x 
        and other.getPos().y < self.getPos().y + self.getSize().y 
        and other.getPos().y + other.getSize().y > self.getPos().y):
            return True
        return False

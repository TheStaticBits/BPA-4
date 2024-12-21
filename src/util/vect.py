class Vect:
    def __init__(self, x=None, y=None):
        if isinstance(x, list):
            self.x = x[0]
            self.y = x[1]

        else:
            if (x is None and y is None):
                self.x = 0
                self.y = 0
            
            elif (y is None):
                self.x = x
                self.y = x
            
            else:
                self.x = x
                self.y = y

    def __add__(self, other):
        # Overriding functions
        # Vect(1,2) + Vect(3,4) returns Vect(4,6)
        return Vect(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vect(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vect(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vect(self.x / other, self.y / other)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getMagnitude(self):
        return (self.x**2 + self.y**2)**0.5
    
    def squareClamp(self, max):
        if self.x > max:
            self.x = max
        if self.y > max:
            self.y = max
        if self.x < -max:
            self.x = -max
        if self.y < -max:
            self.y = -max

    def clampX(self, max):
        if self.x > max:
            self.x = max
        if self.x < -max:
            self.x = -max

    def clampY(self, max):
        if self.y > max:
            self.y = max
        if self.y < -max:
            self.y = -max

    #get sign of vector
    def getSign(self):
        return Vect(
            1 if self.x > 0 else -1 if self.x < 0 else 0,
            1 if self.y > 0 else -1 if self.y < 0 else 0
        )

    def circularClamp(self, radius=1):
        if self.getMagnitude() > radius:
            self.circularUnitize(radius)

    def circularUnitize(self, radius=1):
        magnitude = self.getMagnitude()
        if magnitude != 0:
            self = self * (radius / magnitude)


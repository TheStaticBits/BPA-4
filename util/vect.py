class Vect:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vect(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vect(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vect(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vect(self.x / other, self.y / other)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
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

    def circularClamp(self, radius=1):
        if self.getMagnitude() > radius:
            if self.getMagnitude() == 0:
                # Prevent division by zero
                self = Vect(0, 0)
            else:
                self = self * (radius / self.getMagnitude())

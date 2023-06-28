import math

class MagicClass:
    def __init__(self, radius=0):
        self.radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.radius = radius

    def area(self):
        return self.radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.radius

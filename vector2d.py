import math
import pygame

class Vector2D:

    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar):
        return Vector2D(self.x / scalar, self.y / scalar)
    
    def get_magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def normalize(self):
        mag = self.get_magnitude()
        if mag == 0:
            return Vector2D()
        return Vector2D(self.x / mag, self.y / mag)
    
        
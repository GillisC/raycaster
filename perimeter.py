from vector2d import Vector2D
import pygame
from colors import * 
from ray import Ray
import math


class Perimeter:

    def __init__(self, points: list[(int)]) -> None:
        self.points = points

    def intersect(self, ray):
        current_shortest = 10000000
        current_vec = None
        for i in range(len(self.points)):
            p1 = self.points[i]
            p2 = self.points[(i + 1) % len(self.points)]
            intersection = ray.intersect(p1, p2)
            if intersection:
                length = math.sqrt((intersection.x - ray.origin.x) ** 2 + (intersection.y - ray.origin.y) ** 2)
                if length < current_shortest:
                    current_shortest = length
                    current_vec = Vector2D(intersection.x, intersection.y)
        return current_vec
        

    def show(self, surface):
        for i in range(len(self.points)):
            pygame.draw.line(surface, 
                             PERIMETER_COLOR, 
                             (self.points[i].x, self.points[i].y), 
                             (self.points[(i+1) % len(self.points)].x, self.points[(i+1) % len(self.points)].y),
                             2)    
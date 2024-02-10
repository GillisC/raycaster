from vector2d import Vector2D
import pygame
from colors import * 
from settings import *
import math
class Ray:

    def __init__(self, origin=Vector2D(), direction=Vector2D()) -> None:
        self.origin = origin
        self.direction = direction.normalize()
    

    def look(self, walls):
        current_shortest = 1000000
        final_intersection = None
        for wall in walls:
            intersection = wall.intersect(self)
            if intersection is not None:
                length = math.sqrt((intersection.x - self.origin.x) ** 2 + (intersection.y - self.origin.y) ** 2)
                if length < current_shortest:
                    current_shortest = length
                    final_intersection = intersection
        return final_intersection

    def intersect(self, p1, p2):
        x1 = p1.x
        y1 = p1.y
        x2 = p2.x
        y2 = p2.y

        x3 = self.origin.x
        y3 = self.origin.y
        x4 = self.origin.x + self.direction.x
        y4 = self.origin.y + self.direction.y

        denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if denominator == 0:
            return None
        
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denominator
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denominator
        #print(f"t: {t}, u: {u}")
        if u >= 0 and t >= 0 and t <= 1:
            #print("ray intersection")
            intersection_point_x = x1 + t * (x2 - x1)
            intersection_point_y = y1 + t * (y2 - y1)
            return Vector2D(intersection_point_x, intersection_point_y)
        else:
            #print("ray didn't intersect")
            return None
        
    def show(self, surface):
        pygame.draw.line(surface, RAY_COLOR, (self.origin.x, self.origin.y), (self.origin.x + self.direction.x, self.origin.y + self.direction.y))

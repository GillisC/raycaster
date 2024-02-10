import pygame
from settings import *
from colors import *
from vector2d import Vector2D
from ray import Ray
from perimeter import Perimeter
import math
import random

class RayCaster:

    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.rays = []
        self.walls = []

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


    def setup(self):
        perimeter = Perimeter([Vector2D(800, 100), Vector2D(800, 900), Vector2D(900, 500)])
        playing_perimeter = Perimeter([Vector2D(0, SCREEN_WIDTH), Vector2D(SCREEN_WIDTH, SCREEN_HEIGHT), Vector2D(SCREEN_WIDTH, 0), Vector2D(0, 0)])
        
        for i in range(10):
            rand_perimeter = Perimeter([Vector2D(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)),
                                        Vector2D(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))])
            self.walls.append(rand_perimeter)
        self.walls.append(playing_perimeter)

    def createRays(self, mouse_x, mouse_y):
        self.rays = []
        angle_diff = (2 * math.pi) / RAYS_AMOUNT
        for i in range(RAYS_AMOUNT):
            self.rays.append(Ray(Vector2D(mouse_x, mouse_y), Vector2D(math.cos(angle_diff * i), math.sin(angle_diff * i))))

    
    def run(self):
        self.setup()
        while self.running:
            self.clock.tick(FPS)
            self.screen.fill(BACKGROUND)
            
            self.handle_events()
            mouse_pos = pygame.mouse.get_pos()
            self.createRays(mouse_pos[0], mouse_pos[1])
        
            draw_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)

            for wall in self.walls:
                wall.show(draw_surface)

            
            for ray in self.rays:
                intersection_point = ray.look(self.walls)

                if intersection_point:
                    pygame.draw.line(draw_surface, RAY_COLOR, (ray.origin.x, ray.origin.y), (intersection_point.x, intersection_point.y))
                    self.rays.remove(ray)
            self.screen.blit(draw_surface, (0, 0))
            pygame.display.update()


        
        pygame.quit()
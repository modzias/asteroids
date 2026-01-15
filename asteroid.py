import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # self.velocity = pygame.Vector2(0, 1).rotate(pygame.math.Vector2().uniform_angle()) * 100

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return  # too small to split
        log_event("asteroid_split")
        new_rotation = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS 
        for _ in range(2):
            new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid.velocity = self.velocity.rotate(new_rotation) * 1.2
            new_rotation = -new_rotation
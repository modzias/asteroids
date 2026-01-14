from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # self.velocity = pygame.Vector2(0, 1).rotate(pygame.math.Vector2().uniform_angle()) * 100

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
from circleshape import CircleShape
from constants import *
import pygame
class Shot(CircleShape):
    SHOT_RADIUS = 5

    def __init__(self, x, y):
        super().__init__(x, y, self.SHOT_RADIUS)
        self.position = pygame.Vector2(x, y)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += self.velocity * dt
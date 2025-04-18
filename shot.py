import pygame
from circleshape import CircleShape
import constants


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.SHOT_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    # unsure, task 4
    def update(self, dt):
        self.position += self.velocity * dt

        import pygame
from constants import *
from circleshape import CircleShape
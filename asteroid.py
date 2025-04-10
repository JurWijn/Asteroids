import pygame
import random
from circleshape import CircleShape
import constants

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    # unsure, task 4
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            ast1 = Asteroid(self.position.x, self.position.y, self.radius-constants.ASTEROID_MIN_RADIUS)
            ast2 = Asteroid(self.position.x, self.position.y, self.radius-constants.ASTEROID_MIN_RADIUS)

            ast1.velocity = self.velocity.rotate(self.rotation+angle)
            ast1.velocity *= 1.2
            ast2.velocity = self.velocity.rotate(self.rotation-angle)
            ast2.velocity *= 1.2


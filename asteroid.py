import pygame
import random

from constants import ASTEROID_MIN_RADIUS
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        spread_angle = random.uniform(20,50)
        new_asteroid1 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
        new_asteroid1.velocity = self.velocity.rotate(-spread_angle) * 1.2
        new_asteroid2 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
        new_asteroid2.velocity = self.velocity.rotate(spread_angle) * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

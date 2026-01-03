import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if (self.radius <= ASTEROID_MIN_RADIUS):
            return None

        log_event("asteroid_split")
        split_degree = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_asteroid.velocity = self.velocity.rotate(split_degree) * 1.2

        second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid.velocity = self.velocity.rotate(-split_degree) * 1.2
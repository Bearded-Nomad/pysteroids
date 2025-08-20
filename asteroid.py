import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, "white", (self.position.x, self.position.y), self.radius, 2
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        random_angle = random.uniform(20, 50)
        new_vel1 = self.velocity.rotate(random_angle)
        new_vel2 = self.velocity.rotate(-random_angle)

        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            old_radius = self.radius
            self.radius = old_radius - ASTEROID_MIN_RADIUS
            new1 = Asteroid(self.position.x, self.position.y, self.radius)
            new2 = Asteroid(self.position.x, self.position.y, self.radius)

            new1.velocity = new_vel1 * 1.2
            new2.velocity = new_vel2 * 1.2

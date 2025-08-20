import pygame
from circleshape import *


class Collision(CircleShape):
    def check(self, other_position):
        distance = pygame.math.Vector2.distance_to(
            self.position, other_position.position
        )
        if distance < (self.radius + other_position.radius):
            return True
        else:
            return False

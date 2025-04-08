import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        old_radius = self.radius
        current_position = self.position
        self.kill()
        
        

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            first_astroid_angle = self.velocity.rotate(random_angle)
            second_astroid_angle = self.velocity.rotate(-random_angle)

            new_radius = old_radius - ASTEROID_MIN_RADIUS
            first_astroid = Asteroid(current_position[0], current_position[1], new_radius)
            second_astroid = Asteroid(current_position[0], current_position[1], new_radius)

            first_astroid.velocity = first_astroid_angle * 1.2
            second_astroid.velocity = second_astroid_angle * 1.2



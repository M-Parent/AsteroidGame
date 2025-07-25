import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
      super().__init__(x, y, radius)

    def draw(self, screen):
      pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
      self.position += self.velocity * dt

    def split(self):
       old_radius = self.radius
       self.kill()
       if self.radius <= ASTEROID_MIN_RADIUS:
          return
       else:
          angle = random.uniform(20,50)
          A1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
          A2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
          A1.velocity = pygame.math.Vector2.rotate(self.velocity, angle)*1.2
          A2.velocity = pygame.math.Vector2.rotate(self.velocity, -angle)*1.2

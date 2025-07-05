import pygame
import sys
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)

    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          return
        
      updatable.update(dt)
      
      for asteroid in asteroids:
         if asteroid.collides_with(player):
            print("Game over!")
            sys.exit(1)


      screen.fill("black")
      for obj in drawable:
         obj.draw(screen)
     
      pygame.display.flip()

      # limit the framerate to 60 fps
      dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

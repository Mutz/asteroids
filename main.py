# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys

import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    dt = 0.0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # assign Player Class
    Player.containers = updatable, drawable
    Asteroid.containers = updatable, drawable, asteroids
    AsteroidField.containers = updatable
    Shot.containers = updatable, drawable, shots

    # instantiate Player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update Player Position
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                sys.exit("Game Over!")
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.kill()

        # Rendering
        screen.fill("black")
        # Update drawable group
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60.0) / 1000.0


if __name__ == "__main__":
    main()

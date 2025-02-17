import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import *
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Shot.containers = (shots, updateable, drawable)
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroid_field = AsteroidField()

    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updateable.update(dt)
        
        for obj in asteroids:
            if obj.collides_with(player):
                print("Game over!")
                sys.exit()
        screen.fill("black")

        for obj in asteroids:
            for bullet in shots:
                if obj.collides_with(bullet):
                    obj.split()
                    bullet.kill()
        
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        

        # frame rate limiter
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

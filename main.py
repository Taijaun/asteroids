import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    asteroids = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shooting = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shooting)


    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        #player.draw(screen)
        for drawing in drawable:
            drawing.draw(screen)
        #player.update(dt)

        updateable.update(dt)

        # Check if player and asteroid collide
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game over!")
                return
        
        # Check if shot and asteroid collide
        for asteroid in asteroids:
            for shot in shooting:
                if asteroid.collision_check(shot):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()
        dt = clock.tick(60) / 1000

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
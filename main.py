import pygame

from constants import *
from player import *
from asteroidfield import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    

    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    game_not_over = True

    while game_not_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        
        for thing in updatable:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

        for asteroid in asteroids:
            if asteroid.has_collided_with(player):
                game_not_over = False
                print("Game Over!")
                break
            for shot in shots:
                if asteroid.has_collided_with(shot):
                    asteroid.split()
                    shot.kill()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

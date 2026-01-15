import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Shot.containers = (updatable, drawable, shots)

    Asteroid.containers = (updatable, drawable, asteroids)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((0, 0, 0))
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            hit_shots = [shot for shot in shots if shot.collides_with(asteroid)]
            if any(hit_shots):
                log_event("asteroid_shot")
                asteroid.split()
                for shot in hit_shots:
                    shot.kill()
                                      
        for asteroid in drawable:
            asteroid.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0  # Limit to 60 FPS
        # print(f"Delta time for this frame: {dt} seconds")


if __name__ == "__main__":
    main()

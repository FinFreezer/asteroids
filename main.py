import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import Shot

def main():
    pygame.init()
    game_speed = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode( [SCREEN_WIDTH, 
                                       SCREEN_HEIGHT] )
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    player_one = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while ( True ):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        dt = ( game_speed.tick(60) / 1000 )
        screen.fill( (0,0,0) )
        updatable.update(dt)
        
        for asteroid in asteroids:
            if ( player_one.checkCollision(asteroid) ):
                print(f"Game over!")
                exit()

        for asteroid in asteroids:
            for shot in shots:
                if ( asteroid.checkCollision(shot) ):
                    asteroid.kill()
                    shot.kill()

        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()

import pygame
from constants import *
from player import *
def main():
    pygame.init()
    game_speed = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode( [SCREEN_WIDTH, 
                                       SCREEN_HEIGHT] )
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    Player.containers = (updatable, drawable)
    player_one = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    #player_one.containers(updatable, drawable)

    while ( True ):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        dt = ( game_speed.tick(60) / 1000 )
        screen.fill( (0,0,0) )
        #drawable.draw(screen)
        updatable.update(dt)

        for entity in drawable:
            entity.draw(screen)

        #player_one.draw(screen)
        #player_one.update(dt)
        pygame.display.flip()

if __name__ == "__main__":
    main()

import pygame
import sys
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from constants import *
from logger import log_state, log_event

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0 #delta time

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()

    #set up player object in middle of screen
    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))

    while True: #start game loop (infinite)
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #check if user closed window, exit game loop if closed (makes Windows close button work)
                return 
        screen.fill("black") #colour the screen black
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill() #remove shot from game
                    asteroid.split() #remove asteroid from game
        for drawable_item in drawable:
            drawable_item.draw(screen)
        pygame.display.flip() #refresh screen
        dt = clock.tick(60)/1000 #pauses game until 1/60 of a second passes, effectively locking FPS to 60


if __name__ == "__main__":
    main()

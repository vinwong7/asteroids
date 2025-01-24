import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Creating game objects
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #Create containers for items to go into, based on what actions they are taking
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    #Player will be drawn and updated
    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    #Create player model
    p1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS) 
    astroField = AsteroidField()

    #Game Loop
    while True:
        #Quit line
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #Fill the screen black    
        screen.fill(color="black") 
        
        #Loop through drawable group and draw the objects
        for i in drawable:
            i.draw(screen)

        #Loop through updatable group and update the objects
        for i in updatable:
            i.update(dt)
        
        for i in asteroids:
            if i.collision_check(p1):
                print("Game Over!")
                sys.exit()
        
        #Refresh screen
        pygame.display.flip() 

        #.tick keeps game at 60 fps, dt variable keeps track of time change
        dt = clock.tick(60)/1000 

if __name__ == "__main__":
    main()
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

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
    shots = pygame.sprite.Group()

    #Each class belongs to different groups
    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable, updatable, shots)

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
        
        #Loop through asteroids and check collsion against player; if hit, then exit
        for i in asteroids:
            if i.collision_check(p1):
                print("Game Over!")
                sys.exit()

        #Loop through asteroids and shots and check collisions, if they collide, destroy both objects
            for j in shots:
                if i.collision_check(j):
                    i.split()
                    j.kill()

        #Refresh screen
        pygame.display.flip() 

        #.tick keeps game at 60 fps, dt variable keeps track of time change
        dt = clock.tick(60)/1000 

if __name__ == "__main__":
    main()
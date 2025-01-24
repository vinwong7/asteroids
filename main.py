import pygame
from constants import *
from player import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    p1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS) #Create player model

    #Game Loop
    while True:
        #Quit line
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black") #Fill the screen black
        p1.draw(screen) #Draw player model
        pygame.display.flip() #Refresh screen

        dt = clock.tick(60)/1000 #.tick keeps game at 60 fps

if __name__ == "__main__":
    main()
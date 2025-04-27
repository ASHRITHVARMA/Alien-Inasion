import sys
import pygame

class AlienInvaders:
    "overall class to manage game assets and behavior"

    def __init__(self):
        "initialize the game and create game resources"
        pygame.init()

        self.screen= pygame.display.set_mode((1000, 800))
        pygame.display.set_caption("Alien Invaders")

        # Setting the background color
        self.bg_color= (230, 230, 230)


    def run_game(self):
        "start the main loop for the game"
        while True:
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    sys.exit()

            # Redrawing the screen during each pass through the loop
            self.screen.fill(self.bg_color)
            # Make the most recently drawn screen visible

            pygame.display.flip()

if __name__== '__main__':
    ai= AlienInvaders()
    ai.run_game()

# This code initializes a simple Pygame window with a title "Alien Invaders".
# It also includes a main loop that keeps the window open until the user closes it.
# The game window is set to a size of 800x600 pixels.
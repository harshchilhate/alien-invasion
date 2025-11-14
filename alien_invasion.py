import sys 
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    #overall class to manage game assets and behaviour
    def __init__(self):
        #initialize the game, and create game resources
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        
        #set background colour 
        self.bg_colour = (230,230,230)
        
    def run_game(self):
        #start the main looop for the game
        while True:
            #watch for the keyboard and mouse movements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #redraw the screen during each pass through the loop 
            self.screen.fill(self.settings.bg_colour)
            self.ship.blitme()
            
            #make the most recently drawn screen visible 
            pygame.display.flip()
            self.clock.tick(200)

if __name__ == '__main__':
    #make a game instance , and run the game
    ai = AlienInvasion()
    ai.run_game()
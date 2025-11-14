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
            self._check_events()
            self._update_screen()
            self.clock.tick(200)

    def _check_events(self):
        #respond to the keypresses and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
         #update images on the screen, and filp to the new screen  
            self.screen.fill(self.settings.bg_colour)
            self.ship.blitme()
             
            pygame.display.flip()
         


if __name__ == '__main__':
    #make a game instance , and run the game
    ai = AlienInvasion()
    ai.run_game()
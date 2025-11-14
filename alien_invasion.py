import sys 
import pygame

class AlienInvasion:
    #overall class to manage game assets and behaviour
    def __init__(self):
        #initialize the game, and create game resources
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1080, 720))
        pygame.display.set_caption("Alien Invasion")

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
            self.screen.fill(self.bg_colour)
            
            #make the most recently drawn screen visible 
            pygame.display.flip()
            self.clock.tick(200)

if __name__ == '__main__':
    #make a game instance , and run the game
    ai = AlienInvasion()
    ai.run_game()
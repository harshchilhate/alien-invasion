import pygame
from pygame.sprite import Sprite
from settings import Settings

class Alien(Sprite):
    """a class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        """initialize the alien in the fleet"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings


        #load the alien image and set it's rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #start each new alien near the top left of the screen 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien's exact horizontal position
        self.x = float(self.rect.x)
        
    
    def check_edges(self):
        """return true if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    

    def update(self):
        """move the alien righnt or left"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
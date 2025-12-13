import sys
from time import sleep 
import pygame
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    #overall class to manage game assets and behaviour
    def __init__(self):
        #initialize the game, and create game resources
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width 
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        
        #create an instance to store game statistics.
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #Start alien invasion in an inactive state.
        self.game_active = False

        #make the play button
        self.play_button = Button(self, "Play")

        
    def run_game(self):
        #start the main looop for the game
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(200)

    
    def _update_aliens(self):
        """check if the fleet is at an edge, update the positions."""
        self._check_fleet_edges()
        self.aliens.update()

        #look for the aliens-ship collosions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        #look for the aliens hitting the bottom of the screen
        self._check_aliens_bottom()


    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            #Decrement ship_left
            self.stats.ships_left -= 1

            #Get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            #create a new fleet amd centre the ship
            self._create_fleet()
            self.ship.centre_ship()
            #pause
            sleep(0.8)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)


    def _check_events(self):
        #respond to the keypresses and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
                elif event.type == pygame.KEYDOWN:
                     self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                     self._check_keyup_events(event)
                
    def _check_keydown_events(self, event):
         if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
         elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
         elif event.key == pygame.K_q:
            sys.exit()
         elif event.key == pygame.K_SPACE:
            self._fire_bullet()
         elif event.key == pygame.K_p:
            #reset the game settings.
            self.settings.initialize_dynamic_settings()
            self._start_game()

    def _check_keyup_events(self, event):
         if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
         elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            #reset the game settings.
            self.settings.initialize_dynamic_settings()
            self._start_game()


    def _start_game(self):
        """Start a new game when the player clicks Play."""
        #reset the game statistics.
        self.stats.reset_stats()
        self.game_active = True

        #get rid of any remaining bullets and aliens.
        self.bullets.empty()
        self.aliens.empty()

        #create a new fleet and center the ship.
        self._create_fleet()
        self.ship.centre_ship()

        #Hide the mouse cursor
        pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        """create new bullet and add bullet to the group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _create_fleet(self):
        """Create the fleet of the alien"""
        #create an alien and keep adding aliens until there's no room left
        #space between aliens is one alien width and one alien height
        alien = Alien(self)
        alien_width ,alien_height  = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < ((self.settings.screen_height * 0.90 ) - (3 * alien_height)):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            #finsihed a row ; reset x vlaue, and increment y value
            current_x = alien_width
            current_y += 2 * alien_height


    def _create_alien(self, x_position, y_position):
        """crete an alien and place it in the fleet"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

                     

    def _update_screen(self):
         #update images on the screen, and filp to the new screen  
            self.screen.fill(self.settings.bg_colour)
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.ship.blitme()
            self.aliens.draw(self.screen)

            #Draw the play button if the game is inactive
            if not self.game_active:
                self.play_button.draw_button()
             
            pygame.display.flip()
         

    def _update_bullets(self):
        """update position of bullets and get rid of old bullet"""
        #update bullet positions
        self.bullets.update()
        
        #get rid of the bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisons()

        
    def _check_bullet_alien_collisons(self):
        """respond to bullet-alien collisions."""
        #remove any bullets and aliens that have collided
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if not self.aliens:
            #destory existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
        

    def _check_fleet_edges(self):
        """respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """drop the entire fleet and chnge the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                #Treat this the same as if the ship got hiyt.
                self._ship_hit()
                break

if __name__ == '__main__':
    #make a game instance , and run the game
    ai = AlienInvasion()
    ai.run_game()
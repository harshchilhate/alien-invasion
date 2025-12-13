import pygame.font

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialze scorekeeping attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.stats

        #font settings for scoring information
        self.text_colour = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #Prepare the initial score image.
        self.prep_score()

    
    def prep_score(self):
        """Turn the score into a renderd image."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_colour, self.settings.bg_color)

        #Display the score at the top right of the screen
        self.screen_rect = self.score_image.get_rect()
        self.screen_rect.right = self.screen_rect.right - 20
        self.screen_rect.top = 20 

    def show_scores(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.screen_rect)
class GameStats:
    """track statics for the alien invasion"""
    def __init__(self, ai_games):
        """Initialize statistics"""
        self.settings = ai_games.settings
        self.reset_stats()

        #high score should never be reset 
        self.high_score = 0

    def reset_stats(self):
        """Initialze statistics that can chane during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
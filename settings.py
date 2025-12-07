class Settings:
    #a class to store all the settings for the alien invasion
    def __init__(self):
        #initialize the game settings

        #Screen settings
        self.screen_width = 1080
        self.screen_height = 720
        self.bg_colour = (230,230,230)

        #ship settings
        self.ship_speed = 1.5

        #Bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_colour = (165,95,55)
        self.bullets_allowed = 3
        
        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
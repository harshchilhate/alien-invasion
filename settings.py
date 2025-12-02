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
        self.bullet_speed = 2.0
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_colour = (165,95,55)
class Settings:
    """A class to store all the settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (200, 200, 200)

        # Ship Settings
        self.ship_speed = 3.5

        # Bullet Settings
        self.bullet_speed = 1.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (250, 60, 60)
        self.bullets_allowed = 3
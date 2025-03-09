class Settings:
    """A class to store all the settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (200, 200, 200)

        # Alien Settings
        self.drop_speed = 0.1
        self.fleet_drop_speed = 10

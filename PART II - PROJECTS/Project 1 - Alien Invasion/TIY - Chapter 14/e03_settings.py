class Settings:
    """A class to store all the settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (200, 200, 200)

        # Ship Settings
        self.ship_limit = 2

        # Bullet Settings
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (250, 60, 60)
        self.bullets_allowed = 3

        # Alien Settings
        self.fleet_drop_speed = 0
        self.alien_color = (250, 250, 60)

        # How quick the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize the game's dynamic settings."""
        # Ship Settings
        self.ship_speed = 1.5
        # Bullet Settings
        self.bullet_speed = 1.5
        # Alien Settings
        self.alien_speed = 0.5
        self.fleet_direction = 1  # 1=right , -1=left

    def increase_speed(self):
        """Increase the speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
import pygame
from pygame.sprite import Sprite

class Drop(Sprite):
    """A class to represent a single raindrop in the fleet."""
    def __init__(self, ai_game):
        """Initialize the raindrop and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the raindrop image and set its rect attribute
        self.image = pygame.image.load('images/e03_drop.bmp')
        self.rect = self.image.get_rect()

        # Start each new raindrop line near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the raindrop's exact horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if alien is at the edge of the screen."""
        if self.rect.bottom == 800:
            return True

    def update(self):
        """Move the alien right or left."""
        self.y += self.settings.drop_speed
        self.rect.y = self.y

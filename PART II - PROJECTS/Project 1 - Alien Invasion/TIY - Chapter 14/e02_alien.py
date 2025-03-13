import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.alien_color

        # Create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(1200, 0, 100, 200)

        # Start each new alien line near the top right of the screen
        self.rect.x = self.rect.width + 1000
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def check_edges(self):
        """Return True if alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True

    def update(self):
        """Move the alien right or left."""
        self.y += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.y = self.y

    def draw_alien(self):
        """Draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
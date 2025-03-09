import sys
import pygame
from e03_settings import Settings
from e03_drop import Drop
from random import randint

class DropInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Raindrops')
        self.bg_color = (0, 150, 250)

        self.drops = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_drops()
            self._update_screen()

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_drops(self):
        """Check if the fleet is at an edge, then update the positions of all drops in the fleet."""
        self.drops.update()

    def _create_fleet(self):
        """Create the fleet of drops."""
        drop = Drop(self)
        drop_width, drop_height = drop.rect.size

        number_drops_x = int((self.settings.screen_width // drop_width)/2)-4
        number_rows = int((self.settings.screen_height // drop_height)/2)+3

        print(number_drops_x, number_rows)

        # Create the full fleet of drops
        for row_number in range(number_rows):
            for drop_number in range(number_drops_x):
                self._create_drop(drop_number, row_number)

    def _create_drop(self, drop_number, row_number):
        """Create a drop and place it in a row"""
        drop = Drop(self)
        drop_width, drop_height = drop.rect.size
        drop.x = drop_width + 2 * drop_width * drop_number
        drop.y = drop_height + 2 * drop_height * drop_number

        drop.rect.x = (drop.rect.width + 2 * drop.rect.width * row_number) + self.rn()
        drop.rect.y = (drop.rect.height + 2 * drop.rect.height * row_number) + self.rn()
        self.drops.add(drop)

    def rn(self):
        random_number = randint(-25, 25)
        return random_number

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.bg_color)
        self.drops.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    ai = DropInvasion()
    ai.run_game()
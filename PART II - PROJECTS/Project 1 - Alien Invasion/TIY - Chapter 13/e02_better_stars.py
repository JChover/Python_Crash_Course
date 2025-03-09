import sys
import pygame
from e01_star import Star
from random import randint

class StarInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.screen_width = 1200
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Better Stars')
        self.bg_color = (0, 150, 250)


        self.stars = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


    def _create_fleet(self):
        """Create the fleet of stars."""
        star = Star(self)
        star_width, star_height = star.rect.size

        number_stars_x = int((self.screen_width // star_width)/2)-1
        number_rows = int((self.screen_height // star_height)/2)
        print(number_stars_x, number_rows)

        # Create the full fleet of stars
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        """Create a star and place it in a row"""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x + self.rn()
        star.rect.y = (star.rect.height + 2 * star.rect.height * row_number) + self.rn()
        self.stars.add(star)

    def rn(self):
        random_number = randint(-25, 25)
        return random_number

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.bg_color)
        self.stars.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    ai = StarInvasion()
    ai.run_game()
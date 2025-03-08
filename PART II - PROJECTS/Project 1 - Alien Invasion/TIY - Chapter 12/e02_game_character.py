import pygame

class Character:

    def __init__(self, bs_game):
        """Initialize the character and its starting position."""
        self.screen = bs_game.screen
        self.screen_rect = bs_game.screen.get_rect()

        # Load the character image and get its rect.
        self.image = pygame.image.load('images/e02_character.bmp')
        self.rect = self.image.get_rect()

        # Start each new Character at the bottom center of the screen
        self.rect.center = self.screen_rect.center

        self.character_speed = 3.5

        # Store a decimal value for the Character's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        """Update the Character's position based on the movement flags."""
        # Update the Character's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.character_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.character_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.character_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.character_speed

        # Update rect object from self x.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the Character at the current location."""
        self.screen.blit(self.image, self.rect)
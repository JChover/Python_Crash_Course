import pygame.font

class Button:
    def __init__(self, ai_game, msg, pos):
        """Initialize the button attribute."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.text_color = (230, 230, 230)
        self.font = pygame.font.SysFont(None, 32)

        if pos == "center":
            # Build the button's rect object and center it
            self.rect = pygame.Rect(0, 0, self.width, self.height)
            self.rect.center = self.screen_rect.center
            self.rect.y = self.rect.y - 18

            self.button_color = (199, 178, 46)

        elif pos == "right":
            # Build the button's rect object and center right it
            self.rect = pygame.Rect(0, 0, self.width, self.height)
            self.rect.center = self.screen_rect.center
            self.rect.x = self.rect.x + 270
            self.rect.y = self.rect.y - 18

            self.button_color = (199, 46, 46)

        elif pos == "left":
            # Build the button's rect object and center left it
            self.rect = pygame.Rect(0, 0, self.width, self.height)
            self.rect.center = self.screen_rect.center
            self.rect.x = self.rect.x - 270
            self.rect.y = self.rect.y - 18

            self.button_color = (89, 194, 107)


        elif pos == "top":
            # Build the button's rect object and center top it
            self.rect = pygame.Rect(0, 0, self.width, self.height)
            self.rect.center = self.screen_rect.center
            self.rect.y = self.rect.y - 140

            self.button_color = (200, 200, 200)
            self.text_color = (50, 50, 50)

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
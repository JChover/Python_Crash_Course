# 14-1 Press P to Play - e01_press_p_to_play.py
def _check_keydown_events(self, event):
    """Respond to key presses."""
    if event.key == pygame.K_RIGHT:
        self.ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        self.ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        self._fire_bullet()
    elif event.key == pygame.K_p: # Add the P keydown
        self._start_game() # Call _start_game method
    elif event.key == pygame.K_q:
        sys.exit()

    def _start_game(self):
        # Reset the game statistics
        self.stats.reset_stats()
        self.stats.game_active = True

        # Get rid of any remaining aliens and bullets.
        self.aliens.empty()
        self.bullets.empty()

        # Create a new fleet and center the ship.
        self._create_fleet()
        self.ship.center_ship()

        # Hide the mouse cursor
        pygame.mouse.set_visible(False)

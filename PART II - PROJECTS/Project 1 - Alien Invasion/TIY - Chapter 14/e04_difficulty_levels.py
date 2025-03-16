# Added to the main Alien Invasion Project a set of three difficulty levels as follows:

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        if self.easy_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
            # Reset the game settings
            self.settings.initialize_dynamic_settings()
            self.settings.speedup_scale = 1.1 # For Easy
            self._start_game()
        elif self.medium_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
            # Reset the game
            self.settings.initialize_dynamic_settings()
            self.settings.speedup_scale = 1.5 # For Medium
            self._start_game()
        elif self.hard_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
            # Reset the game settings
            self.settings.initialize_dynamic_settings()
            self.settings.speedup_scale = 1.7 # For Hard
            self._start_game()
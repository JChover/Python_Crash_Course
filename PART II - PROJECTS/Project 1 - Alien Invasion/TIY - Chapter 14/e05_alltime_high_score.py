# In scoreboard.py we import json and in check_high_score method
def check_high_score(self):
    """Check to see if there's a new high score."""
    if self.stats.score > self.stats.high_score:
        self.stats.high_score = self.stats.score
        self.prep_high_score()
        with open('highscore.json', 'w') as f: # Save new HS to json file
            json.dump(self.stats.high_score, f)

# In game_stats.py we initialize the high_score loading from the same file
import json

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start Alien Invasion in an inactive State
        self.game_active = False
        # High score should never be reset.
        with open('highscore.json') as f: # Here we get HS from json
            self.high_score = json.load(f)

# Issue of this approach is json file must be manually initialized with a '0' if not it does not work
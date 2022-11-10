class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 100
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Ship settings
        self.ship_speed = 3
        self.ship_limit = 1

        # Bullet Settings
        self.bullet_speed = 5
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

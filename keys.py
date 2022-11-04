import sys
import pygame
from keys_settings import Settings

class Keys():
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Keys")

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses"""
        print(event.key)
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def _update_screen(self):
        def _update_screen(self):
            """Update images on the screen, and flip to the new screen"""
            self.screen.fill(self.settings.bg_color)

            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ky = Keys()
    ky.run_game()


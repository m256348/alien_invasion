import pygame
import sys
from rocket_settings import Settings

pygame.init()

class draw_character:
    """Draws character at center of screen"""

    def __init__(self):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.settings = Settings()

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update images on the screen, and flip to the new screen"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        self.rect.x = self.x
        self.rect.y = self.y


pygame.init()

screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))

rocket = draw_character()
rocket.blitme()

pygame.display.flip()

class Rocket_game():

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.rocket = draw_character()
        self.screen = screen

    def run_game(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    rg = Rocket_game()
    rg.run_game()
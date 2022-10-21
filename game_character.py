import pygame
import sys
import time

pygame.init()
class draw_character:
    """Draws character at center of screen"""
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load('images/hog_rider.bmp')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)


pygame.init()

screen = pygame.display.set_mode((1000, 1000))
screen.fill((0, 0, 255))

my_character = draw_character(screen)
my_character.blitme()

pygame.display.flip()

time.sleep(20)
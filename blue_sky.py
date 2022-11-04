import pygame
import sys
import time

pygame.init()
screen = pygame.display.set_mode((600, 400))
screen.fill((0, 0, 255))

pygame.display.flip()

time.sleep(20)

self.image = pygame.image.load('images/ship.png').convert_alpha()
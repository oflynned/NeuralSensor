import struct
import pygame
from Constants import Constants
import random

class Screen:
    WIDTH = 100
    HEIGHT = 100
    WHITE = (255, 255, 255)

    def __init__(self):
        self.display = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT), 0, 32)
        pygame.display.set_caption("AI Art")
        self.display.fill(Screen.WHITE)

    def draw(self, squares):
        for square in squares:
            pygame.draw.rect(self.display, square.get_colour(),
                             (square.get_x() * Constants.SQ_SIZE, square.get_y() * Constants.SQ_SIZE,
                              Constants.SQ_SIZE, Constants.SQ_SIZE))
        pygame.display.update()

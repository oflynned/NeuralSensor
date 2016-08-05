import struct
import pygame
from Constants import Constants


class Screen:
    WIDTH = 600
    HEIGHT = 600
    WHITE = (255, 255, 255)

    def __init__(self):
        self.display = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT), 0, 32)
        pygame.display.set_caption("AI Art")
        self.display.fill(Screen.WHITE)

    def draw(self, squares):
        for square in squares:
            colour = (int(square.get_colour()), 0, 0)
            pygame.draw.rect(self.display, colour,
                             (square.get_x() * Constants.SQ_SIZE, square.get_y() * Constants.SQ_SIZE,
                              Constants.SQ_SIZE, Constants.SQ_SIZE))
        pygame.display.update()

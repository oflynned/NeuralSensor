import struct
import pygame


class Screen:
    WIDTH = 600
    HEIGHT = 600
    WHITE = (255, 255, 255)

    def __init__(self):
        self.display = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT), 0, 32)
        pygame.display.set_caption("AI Art")
        self.display.fill(Screen.WHITE)

    def draw(self, squares, SQ_SIZE):
        #pygame.time.delay(100)
        for square in squares:
            pygame.draw.rect(self.display, (square.get_colour(), 0, 0),
                             (square.get_x() * SQ_SIZE, square.get_y() * SQ_SIZE, SQ_SIZE, SQ_SIZE))
        pygame.display.update()

    @staticmethod
    def get_hex_from_int(rgb_int):
        rgb = (rgb_int, 0, 0)
        return "#" + str(struct.pack('BBB', *rgb).encode('hex'))

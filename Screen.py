import matplotlib.pyplot as plt
import struct


x0 = y0 = 0
x1 = y1 = 3


class Screen:


    def __init__(self):
        pass

    def map_to_screen(self, squares):
        plt.clf()

        for sq in squares:
            sq_colour = sq.get_colour()
            hex_colour = Screen.get_hex_from_int(sq_colour)

            rectangle = plt.Rectangle((sq.get_x(), sq.get_y()), 1, 1, fc=hex_colour)
            plt.gca().add_patch(rectangle)

        plt.interactive(False)
        plt.axis([x0, x1, y0, y1])

        ax = plt.subplot()
        ax.set_autoscale_on(False)

        plt.show(block='true')


    @staticmethod
    def get_hex_from_int(rgb_int):
        rgb = (rgb_int, 0, 0)
        return "#" + str(struct.pack('BBB', *rgb).encode('hex'))

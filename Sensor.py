import random


class Sensor:
    def __init__(self):
        pass

    @staticmethod
    def get_input():
        return random.randint(0, 255)

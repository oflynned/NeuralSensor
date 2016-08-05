import random
from Constants import Constants


class Sensor:
    def __init__(self):
        pass

    @staticmethod
    def generate_light():
        return random.randint(128, 255)

    @staticmethod
    def generate_dark():
        return random.randint(0, 127)

    @staticmethod
    def generate_random_colour():
        return random.randint(0, 255)

    @staticmethod
    def logarithmic_splicing():
        return 600

    @staticmethod
    def generate_n_sensors(n, m):
        sensor_data = []
        for i in range(n*m):
            if i < Sensor.logarithmic_splicing():
                sensor_data.append(Sensor.generate_light())
            else:
                sensor_data.append(Sensor.generate_dark())
        return sensor_data

import random


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
    def generate_n_sensors(n, m, sensors_per_tile):
        sensor_data = []
        for i in range(n*m):
            sensor_tile = []
            for j in range(sensors_per_tile):
                sensor_tile.append(Sensor.generate_random_colour())
            sensor_data.append(sensor_tile)
        #print sensor_data
        return sensor_data

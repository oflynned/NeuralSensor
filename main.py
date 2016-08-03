from Screen import Screen
from Sensor import Sensor
from Square import Square
from NeuralNet import Util, NeuralNet
import pygame, sys
from pygame.locals import *

MAX_ROWS = 100
MAX_COLS = 100
SENSORS_PER_SQUARE = 1
SQ_SIZE = 6

pygame.init()
screen = Screen()

while True:
    squares = []
    sensors = Sensor.generate_n_sensors(MAX_ROWS, MAX_COLS, SENSORS_PER_SQUARE)

    for i in range(0, MAX_COLS):
        for j in range(0, MAX_ROWS):
            average = Util.get_avg(sensors, i, j)
            squares.append(Square(i, j, average))

    screen.draw(squares, SQ_SIZE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

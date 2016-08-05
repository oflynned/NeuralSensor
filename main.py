from Screen import Screen
from Constants import Constants
from Square import Square
from NeuralNet import Util, NeuralNet
import pygame, sys
from pygame.locals import *

pygame.init()
screen = Screen()

with open(Constants.DATA_FILE_NAME) as data_file:
    sensor_data = data_file.read()
    sensor_data = sensor_data.replace("[", "").replace("]", "").split(",")

while True:
    squares = []

    for i in range(0, Constants.MAX_COLS):
        for j in range(0, Constants.MAX_ROWS):
            squares.append(Square(i, j, Util.get_value(sensor_data, i, j)))

    screen.draw(squares)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

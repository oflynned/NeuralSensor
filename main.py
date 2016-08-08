from Screen import Screen
from Constants import Constants
from Square import Square
from NeuralNet import Util, NeuralNet
import pygame, sys
from pygame.locals import *
import random, time

pygame.init()
screen = Screen()

with open(Constants.DATA_FILE_NAME) as data_file:
    sensor_data = data_file.read()
    sensor_data = sensor_data.replace("[", "").replace("]", "").split(",")

while True:
    squares = []

    for i in range(0, Constants.MAX_COLS):
        for j in range(0, Constants.MAX_ROWS):

            rand = random.randrange(0, 3)
            if rand == 0:
                colour = (int(Util.get_value(sensor_data, i, j)), 0, 0)
            elif rand == 1:
                colour = (0, int(Util.get_value(sensor_data, i, j)), 0)
            else:
                colour = (0, 0, int(Util.get_value(sensor_data, i, j)))

            squares.append(Square(i, j, colour))
            screen.draw(squares)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

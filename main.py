from Screen import Screen
from Sensor import Sensor
from Square import Square

screen = Screen()
squares = []

MAX_ROWS = 3
MAX_COLS = 3

for i in range(0, MAX_ROWS):
    for j in range(0, MAX_COLS):
        squares.append(Square(i, j, Sensor.get_input()))

for square in squares:
    print(str(square.get_id()) + " with colour " + str(Screen.get_hex_from_int(square.get_colour())))

screen.map_to_screen(squares)


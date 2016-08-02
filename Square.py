class Square:
    def __init__(self, x_id, y_id, colour):
        self.x_id = x_id
        self.y_id = y_id
        self.colour = colour

    def set_colour(self, colour):
        self.colour = colour

    def get_colour(self):
        return self.colour

    def get_id(self):
        return self.x_id, self.y_id

    def get_x(self):
        return self.x_id

    def get_y(self):
        return self.y_id
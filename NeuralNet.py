class Util:
    @staticmethod
    def get_avg(items, row, skip):
        return sum(items[row + (row*skip)]) / len(items[row + (row*skip)])

    @staticmethod
    def summate(items):
        total = 0
        for item in items:
            total += item
        return total

    @staticmethod
    def get_input_w_weight(input, weight):
        return input * weight


class NeuralNet:
    def __init__(self, size):
        self.size = size

import tensorflow as tf


class Util:
    @staticmethod
    def get_value(items, row, skip):
        return items[row + (row * skip)]


class NeuralNet:
    def __init__(self):
        self.X = tf.placeholder(tf.int32, None)

    def interpolate(self, data):
        print data

        with tf.Session as session:
            session.run(tf.initialize_all_variables())

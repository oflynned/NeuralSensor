import tensorflow as tf


class Util:
    @staticmethod
    def get_value(items, row, skip):
        return items[row + (row * skip)]


class NeuralNet:

    @staticmethod
    def interpolate(data):
        print data

        with tf.Session as session:
            session.run(tf.initialize_all_variables())

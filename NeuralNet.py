import tensorflow as tf


class Util:
    @staticmethod
    def get_avg(items, row, skip):
        return sum(items[row + (row * skip)]) / len(items[row + (row * skip)])


class Clustering:
    weights = {
        'encoder_h1': tf.Variable(tf.random_normal([1, 100]))
    }
    biases = {
        'encoder_b1': tf.Variable(tf.random_normal(100, 1))
    }

    def __init__(self):
        self.d = tf.placeholder('float32', None)
        self.y = tf.reshape(self.d, [100, 1])
        self.x = tf.placeholder('float32', None)

    def encode(self, x):
        layer1 = tf.nn.sigmoid(tf.add(tf.matmul(x, self.weights['encoder_h1']), self.biases['encoder_b1']))
        return tf.nn.relu(layer1)

    def get_y(self):
        return self.y

    def get_x(self):
        return self.x

    def get_d(self):
        return self.d


class NeuralNet:
    def __init__(self):
        self.X = tf.placeholder("float", None)

    def interpolate(self, data):
        clustering = Clustering()
        print data

        with tf.Session as session:
            session.run(tf.initialize_all_variables())

            for d in range(len(data)):
                self.X = session.run(clustering.get_y(), feed_dict=data[d])
                out = session.run(clustering.encode(self.X))
                return out

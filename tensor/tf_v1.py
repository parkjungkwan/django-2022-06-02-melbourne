import tensorflow.compat.v1 as tf
from icecream import ic
if __name__ == '__main__':

    tf.disable_v2_behavior()
    hello = tf.constant("Hello")
    session = tf.Session()
    ic(session.run(hello))
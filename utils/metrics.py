"""
The implementation of some metrics based on Tensorflow.

@Author: Mékéné
@Github: https://github.com/IsmaelMekene
@Project: https://github.com/luyanger1799/meteor-CUTIE

"""
import tensorflow as tf


class MeanIoU(tf.keras.metrics.MeanIoU):
    def update_state(self, y_true, y_pred, sample_weight=None):
        # sparse code
        y_true = tf.argmax(y_true, axis=-1)
        y_pred = tf.argmax(y_pred, axis=-1)
        return super(MeanIoU, self).update_state(y_true, y_pred, sample_weight)

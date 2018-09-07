# Made Imports
import tensorflow as tf


# Initializing TensorFlow Variable.
m = tf.Variable(tf.random_normal([]))
init = tf.global_variables_initializer()

with tf.Session() as sess:
    # Check if initialized.
    print "Init: " + str(sess.run(init))
    

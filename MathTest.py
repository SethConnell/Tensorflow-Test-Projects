# Made Imports
import tensorflow as tf


# Basic Math.
const_a = tf.constant(3.6)
const_b = tf.constant(1.2)
total = const_a + const_b
quot = tf.div(const_a, const_b)

# Matrix Multiplication.
mat_a = tf.constant([[2,3], [1,2], [4,5]])
mat_b = tf.constant([[6,4,1], [3,7,2]])
mat_product = tf.matmul(mat_a, mat_b)

with tf.Session() as sess:
    print "Total: " + str(sess.run(total))
    print "Quotient: " + str(sess.run(quot))
    print "Matrix Product: " + str(sess.run(mat_product))

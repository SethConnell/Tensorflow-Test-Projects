import tensorflow as tf

const_a = tf.constant(3.6)
const_b = tf.constant(1.2)
total = const_a + const_b
quot = tf.div(const_a, const_b)

with tf.Session() as sess:
    print "Total: " + str(sess.run(total))
    print "Quotient: " + str(sess.run(quot))

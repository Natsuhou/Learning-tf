import tensorflow as tf

x1 = tf.constant(5)
x2 = tf.constant(6)
result = tf.matmul(x1, x2)

#Creates an abstract tensor

sess = tf.Session()
print(sess.run(result))
sess.close()

with tf.Session() as sess:
    print(sess.run(result))

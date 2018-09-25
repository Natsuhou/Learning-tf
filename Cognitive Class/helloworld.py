import tensorflow as tf

a = tf.constant([3])
b = tf.constant([5])
c = tf.add(a, b)

session = tf.Session()
result = session.run(c)
session.close()

with tf.Session() as session:
    result = session.run(c)
    print(result)

# Tensor is a multidimentional array
# Dimensions specify how many coordinates are needed for an array


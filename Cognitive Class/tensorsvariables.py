import tensorflow as tf

# Tensor is a multidimentional array
# Dimensions specify how many coordinates are needed for an array

state = tf.Variable(0)

one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)

init_op = tf.initialize_all_variables()
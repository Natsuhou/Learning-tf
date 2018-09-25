import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

'''
0 = [1,0,0,0,0,0,0,0,0,0]
1 = [0,1,0,0,0,0,0,0,0,0]
2 = [0,0,1,0,0,0,0,0,0,0]
3 = [0,0,0,1,0,0,0,0,0,0]
'''

# Changeable
n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500

n_classes = 10

# Go through batches of 100 of features like images or something
batch_size = 100

# Height x Width
x = tf.placeholder('float'[None, 784])
y = tf.placeholder('float')


# This creates a tensor or array of your data using a bunch of random numbers
# This is now all of our weights in a tensor


def neural_network_model(data):

    # Biases are added to replicate the real world and if inputs are 0

    hidden_1_layer = {'weights': tf.Variable(tf.random_normal([784, n_nodes_hl1])),
                      'biases': tf.Variable(tf.random_normal(n_nodes_hl1))}

    hidden_2_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
                      'biases': tf.Variable(tf.random_normal(n_nodes_hl2))}

    hidden_3_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
                      'biases': tf.Variable(tf.random_normal(n_nodes_hl3))}

    output_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])),
                      'biases': tf.Variable(tf.random_normal([n_classes]))}

    # (input_data * weights) + biases

    # Rectified linear is your threshold function
    # Apply this function to layer 1
    l1 = tf.add(tf.matmul(data, hidden_1_layer['weights']) + hidden_1_layer['biases'])
    l1 = tf.nn.relu(l1)

    l2 = tf.add(tf.matmul(l1, hidden_2_layer['weights']) + hidden_2_layer['biases'])
    l2 = tf.nn.relu(l2)

    l3 = tf.add(tf.matmul(l2, hidden_3_layer['weights']) + hidden_3_layer['biases'])
    l3 = tf.nn.relu(l1)

    output = tf.add(tf.matmul(l3, output_layer['weights']) + output_layer['biases'])

    return output
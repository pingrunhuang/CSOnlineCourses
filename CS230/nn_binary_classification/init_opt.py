"""
this is part of the tunning skills: initialization
"""
import numpy as np

def initialize_parameters_zeros(layer_dims):
    parameters = {}
    L = len(layer_dims)
    for i in range(1, L):
        parameters['W'+str(i)] = np.zeros((layer_dims[i-1], layer_dims[i]))
        parameters['b' + str(i)] = np.zeros((layer_dims[i], 1))
    return parameters


def initialize_parameters_random(layers_dims):
    # initialize your weights to large random values (scaled by *10) 
    parameters = {}
    L = len(layers_dims)
    np.random.seed(3)
    for l in range(1, L):
        parameters['W'+str(l)] = np.random.randn(layers_dims[l], layers_dims[l-1])*10
        parameters['b'+str(l)] = np.zeros((layers_dims[l], 1))
    return parameters

def initialize_parameters_he(layers_dims):
    np.random.seed(3)
    parameters = {}
    L = len(layers_dims) - 1 # integer representing the number of layers
     
    for l in range(1, L + 1):
        # 'He' initialization recommends for layers with a ReLU activation.
        parameters['W' + str(l)] = np.random.randn(layers_dims[l], layers_dims[l-1]) * np.sqrt(2/layers_dims[l-1])
        parameters['b' + str(l)] = np.zeros((layers_dims[l], 1))
        
    return parameters
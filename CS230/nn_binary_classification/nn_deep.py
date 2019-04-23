import numpy as np
from utils import linear_activation_backward, linear_activation_forward, L_model_forward, compute_cost
import time
import numpy as np
import h5py
import matplotlib.pyplot as plt
import scipy
from PIL import Image
from scipy import ndimage

plt.rcParams['figure.figsize'] = (5.0, 4.0) # set default size of plots
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'

np.random.seed(1)

"""
Implement backpropagation for the [LINEAR->RELU]  X  (L-1) -> LINEAR -> SIGMOID model.
"""

def initialize_parameters_deep(layer_dims):
    """
    Arguments:
    layer_dims -- python array (list) containing the dimensions of each layer in our network
    
    Returns:
    parameters -- python dictionary containing your parameters "W1", "b1", ..., "WL", "bL":
                    Wl -- weight matrix of shape (layer_dims[l], layer_dims[l-1])
                    bl -- bias vector of shape (layer_dims[l], 1)
    """
    
    np.random.seed(3)
    parameters = {}
    L = len(layer_dims)            # number of layers in the network

    for l in range(1, L):
        parameters['W' + str(l)] = np.random.randn(layer_dims[l],layer_dims[l-1])
        parameters['b' + str(l)] = np.zeros((layer_dims[l],1))
        
        assert(parameters['W' + str(l)].shape == (layer_dims[l], layer_dims[l-1]))
        assert(parameters['b' + str(l)].shape == (layer_dims[l], 1))
    return parameters

def update_parameters(parameters, grads, learning_rate):
    """
    Update parameters using gradient descent
    
    Arguments:
    parameters -- python dictionary containing your parameters 
    grads -- python dictionary containing your gradients, output of L_model_backward
    
    Returns:
    parameters -- python dictionary containing your updated parameters 
                  parameters["W" + str(l)] = ... 
                  parameters["b" + str(l)] = ...
    """
    
    L = len(parameters) // 2 # number of layers in the neural network

    # Update rule for each parameter. Use a for loop.
    for l in range(L):
        parameters["W" + str(l+1)] = parameters["W"+str(l+1)] - learning_rate * grads['dW'+str(l+1)]
        parameters["b" + str(l+1)] = parameters["b"+str(l+1)] - learning_rate * grads['db'+str(l+1)]
    return parameters

def L_model_backward(AL, Y, caches):
    """
    Implement the backward propagation for the [LINEAR->RELU] * (L-1) -> LINEAR -> SIGMOID group
    
    Arguments:
    AL -- probability vector, output of the forward propagation (L_model_forward())
    Y -- true "label" vector (containing 0 if non-cat, 1 if cat)
    caches -- list of caches containing:
                every cache of linear_activation_forward() with "relu" (it's caches[l], for l in range(L-1) i.e l = 0...L-2)
                the cache of linear_activation_forward() with "sigmoid" (it's caches[L-1])
    
    Returns:
    grads -- A dictionary with the gradients
             grads["dA" + str(l)] = ... 
             grads["dW" + str(l)] = ...
             grads["db" + str(l)] = ... 
    """
    grads = {}
    L = len(caches) # the number of layers
    m = AL.shape[1]
    Y = Y.reshape(AL.shape) # after this line, Y is the same shape as AL
    
    # Initializing the backpropagation
    dAL = -np.divide(Y, AL) - np.divide(1-Y, 1-AL)

    # Lth layer (SIGMOID -> LINEAR) gradients. Inputs: "dAL, current_cache". Outputs: "grads["dAL-1"], grads["dWL"], grads["dbL"]
    current_cache = linear_activation_backward(dAL, caches[L-1], 'sigmoid')
    grads["dA" + str(L-1)], grads["dW" + str(L)], grads["db" + str(L)] = current_cache
    
    # Loop from l=L-2 to l=0
    for l in reversed(range(L-1)):
        # lth layer: (RELU -> LINEAR) gradients.
        # Inputs: "grads["dA" + str(l + 1)], current_cache". Outputs: "grads["dA" + str(l)] , grads["dW" + str(l + 1)] , grads["db" + str(l + 1)] 
        current_cache = linear_activation_backward(grads["dA" + str(l+1)], caches[l], 'relu')
        dA_prev_temp, dW_temp, db_temp = current_cache
        grads["dA" + str(l)] = dA_prev_temp
        grads["dW" + str(l + 1)] = dW_temp
        grads["db" + str(l + 1)] = db_temp
    return grads

def L_layer_model(X, Y, layers_dims, learning_rate = 0.0075, num_iterations = 3000, print_cost=False):
    """
    Implements a L-layer neural network: [LINEAR->RELU]*(L-1)->LINEAR->SIGMOID.
    
    Arguments:
    X -- data, numpy array of shape (number of examples, num_px * num_px * 3)
    Y -- true "label" vector (containing 0 if cat, 1 if non-cat), of shape (1, number of examples)
    layers_dims -- list containing the input size and each layer size, of length (number of layers + 1).
    learning_rate -- learning rate of the gradient descent update rule
    num_iterations -- number of iterations of the optimization loop
    print_cost -- if True, it prints the cost every 100 steps
    
    Returns:
    parameters -- parameters learnt by the model. They can then be used to predict.
    """

    np.random.seed(1)
    costs = []                         # keep track of cost
    
    # Parameters initialization. (≈ 1 line of code)
    parameters = initialize_parameters_deep(layers_dims)
    
    # Loop (gradient descent)
    for i in range(0, num_iterations):

        # Forward propagation: [LINEAR -> RELU]*(L-1) -> LINEAR -> SIGMOID.
        AL, caches = L_model_forward(X, parameters)
        
        # Compute cost.
        cost = compute_cost(AL, Y)
    
        # Backward propagation.
        grads = L_model_backward(AL, Y, caches)
 
        # Update parameters.
        parameters = update_parameters(parameters, grads, learning_rate)
                
        # Print the cost every 100 training example
        if print_cost and i % 100 == 0:
            print ("Cost after iteration %i: %f" %(i, cost))
        if print_cost and i % 100 == 0:
            costs.append(cost)
            
    # plot the cost
    plt.plot(np.squeeze(costs))
    plt.ylabel('cost')
    plt.xlabel('iterations (per tens)')
    plt.title("Learning rate =" + str(learning_rate))
    plt.show()
    
    return parameters

def predict(X, y, parameters):
    """
    This function is used to predict the results of a  L-layer neural network.
    
    Arguments:
    X -- data set of examples you would like to label
    parameters -- parameters of the trained model
    
    Returns:
    p -- predictions for the given dataset X
    """
    m = X.shape[1]
    n = len(parameters) // 2 # number of layers in the neural network
    p = np.zeros((1,m))
    
    # Forward propagation
    probas, caches = L_model_forward(X, parameters)

    # convert probas to 0/1 predictions
    for i in range(0, probas.shape[1]):
        if probas[0,i] > 0.5:
            p[0,i] = 1
        else:
            p[0,i] = 0
    
    #print results
    print ("predictions: " + str(p))
    print ("true labels: " + str(y))
    print("Accuracy: "  + str(np.sum((p == y)/m)))
        
    return p

def print_mislabeled_images(classes, X, y, p):
    """
    Plots images where predictions and truth were different.
    X -- dataset
    y -- true labels
    p -- predictions
    """
    a = p + y
    mislabeled_indices = np.asarray(np.where(a == 1))
    plt.rcParams['figure.figsize'] = (40.0, 40.0) # set default size of plots
    num_images = len(mislabeled_indices[0])
    for i in range(num_images):
        index = mislabeled_indices[1][i]
        
        plt.subplot(2, num_images, i + 1)
        plt.imshow(X[:,index].reshape(64,64,3), interpolation='nearest')
        plt.axis('off')
        plt.title("Prediction: " + classes[int(p[0,index])].decode("utf-8") + " \n Class: " + classes[y[0,index]].decode("utf-8"))

def load_data(dir='hot-dog-not-hot-dog', image_height=256, image_width=256):
    from os import listdir
    from os.path import isfile, join
    from matplotlib.pyplot import imread
    import numpy as np

    def get_images(file_name):
        img = Image.open(file_name)
        return img.resize((image_height,image_width), Image.ANTIALIAS)

    def get_file_list(folder):
        return [f for f in listdir(folder) if isfile(join(folder, f))]

    def get_array(folder):
        image_list = get_file_list(folder)
        m = np.array([])
        for i_name in image_list:
            p = np.array(get_images(folder+i_name))

            p = p.reshape(p.shape[0]*p.shape[1]*p.shape[2],1)
            if len(m)==0:
                m = p
            else:
                # Join a sequence of arrays along an existing axis.
                m = np.concatenate((m,p),axis=1)
        return m

    if dir == "hot-dog-not-hot-dog":
        train_hot_dog_jpgs = get_array(dir+'/train/hot_dog/')
        train_hot_dog_y = np.ones((1, train_hot_dog_jpgs.shape[1]))
        train_not_hot_dog_jpgs = get_array(dir+'/train/not_hot_dog/')
        train_not_hot_dog_y = np.ones((1, train_not_hot_dog_jpgs.shape[1]))
        test_hot_dog_jpgs = get_array(dir+'/test/hot_dog/')
        test_hot_dog_y = np.ones((1, test_hot_dog_jpgs.shape[1]))
        test_not_hot_dog_jpgs = get_array(dir+'/test/not_hot_dog/')
        test_not_hot_dog_y = np.ones((1, test_not_hot_dog_jpgs.shape[1]))

        train_set_x_orig = np.concatenate((train_hot_dog_jpgs, train_not_hot_dog_jpgs), axis=1)
        train_set_y_orig = np.concatenate((train_hot_dog_y, train_not_hot_dog_y), axis=1)

        test_set_x_orig = np.concatenate((test_hot_dog_jpgs, test_not_hot_dog_jpgs), axis=1)
        test_set_y_orig = np.concatenate((test_hot_dog_y, test_not_hot_dog_y), axis=1)

        classes = {1:"hot dog", 0:"not hot dog"}
        return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes

def image_reshape(train_x_orig, test_x_orig):
    # Reshape the training and test examples 
    print("train_x_origin's shep:"+str(train_x_orig.shape))
    print("test_x_origin's shep:"+str(test_x_orig.shape))
    train_x_flatten = train_x_orig.reshape(train_x_orig.shape[0], -1).T   # The "-1" makes reshape flatten the remaining dimensions
    test_x_flatten = test_x_orig.reshape(test_x_orig.shape[0], -1).T
    # Standardize data to have feature values between 0 and 1.
    train_x = train_x_flatten/255.
    test_x = test_x_flatten/255.
    print ("train_x's shape: " + str(train_x.shape))
    print ("test_x's shape: " + str(test_x.shape))



if __name__ == "__main__":
    train_x_orig, train_y, test_x_orig, test_y, classes = load_data()
    # feature match
    assert train_x_orig.shape[1] == train_y.shape[1]
    assert test_x_orig.shape[1] == test_y.shape[1]
    layers_dims = [train_x_orig.shape[0], 20, 7, 5, 1] #  4-layer model
    parameters = L_layer_model(train_x_orig, train_y, layers_dims, num_iterations=1)
    predict(test_x_orig, test_y, parameters)
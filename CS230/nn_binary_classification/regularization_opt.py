"""
another tuning technique for preventing overfitting: regularization
"""
import numpy as np

def L2_regularization_cost(Y, parameters, lambd):
    m = Y.shape[1]
    W = {}
    L = len(parameters)
    for l in range(1,L):
        W[str(l)] = parameters["W"+str(l)]
    # this is computing the augmented regularization part
    regularization = sum([np.sum(np.square(W[str(l)])) for l in range(1,L)])  * lambd / (2*m)
    return regularization

def compute_cost_with_regularization(A3, Y, parameters, lambd, cost_function):
    cost = cost_function(A3, Y) + L2_regularization_cost(Y, parameters, lambd)
    return cost

def backward_propagation_with_regularization(X, Y, parameters, lambd):
    m = X.shape[1]
    Z1 = parameters["Z1"]
    A1 = parameters["A1"]
    W1 = parameters["W1"]
    b1 = parameters["b1"]
    Z2 = parameters["Z2"]
    A2 = parameters["A2"]
    W2 = parameters["W2"]
    b2 = parameters["b2"]
    Z3 = parameters["Z3"]
    A3 = parameters["A3"]
    W3 = parameters["W3"]
    b3 = parameters["b3"]
    dZ3 = A3 - Y
    dW3 = 1./m * np.dot(dZ3, A2.T) + lambd*W3/m
    db3 = 1./m * np.sum(dZ3, axis=1, keepdims = True)
    
    dA2 = np.dot(W3.T, dZ3)
    dZ2 = np.multiply(dA2, np.int64(A2 > 0))
    dW2 = 1./m * np.dot(dZ2, A1.T) + lambd*W2/m
    db2 = 1./m * np.sum(dZ2, axis=1, keepdims = True)
    
    dA1 = np.dot(W2.T, dZ2)
    dZ1 = np.multiply(dA1, np.int64(A1 > 0))
    dW1 = 1./m * np.dot(dZ1, X.T) + lambd*W1/m
    db1 = 1./m * np.sum(dZ1, axis=1, keepdims = True)
    
    gradients = {"dZ3": dZ3, "dW3": dW3, "db3": db3,"dA2": dA2,
                 "dZ2": dZ2, "dW2": dW2, "db2": db2, "dA1": dA1, 
                 "dZ1": dZ1, "dW1": dW1, "db1": db1}
    
    return gradients

def print_backprop_with_reg(X_assess, Y_assess, cache):
    grads = backward_propagation_with_regularization(X_assess, Y_assess, cache, lambd = 0.7)
    print ("dW1 = "+ str(grads["dW1"]))
    print ("dW2 = "+ str(grads["dW2"]))
    print ("dW3 = "+ str(grads["dW3"]))

"""
Write some test data
"""



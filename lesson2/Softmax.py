import numpy as np


# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    L_softmax = []
    for v in L:
        L_softmax.append(np.exp(v) / np.sum(np.exp(L)))

    return L_softmax
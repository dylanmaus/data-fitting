"""
compute the gradient
"""

import copy

class Gradient:
    def __init__(self, func, h, params):
        self.func
        self.h
        self.params
        self.gradients = []

    def derivative(self, t, s):
        return (self.func(t) - self.func(s))/self.h

    def compute_gradient(self):
        for i in range(len(params)):
            t = copy.deepcopy(params)
            t[i] += self.h
            partial_derivative = self.derivative(t, params)
            self.gradients.append(partial_derivative)

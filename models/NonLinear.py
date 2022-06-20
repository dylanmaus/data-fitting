"""
nonlinear function of the form
f(x) = alpha*x/(beta+x)
"""

class NonLinear:
    def __init__(self, alpha, beta):
        self.alpha = alpha
        self.beta = beta

    def model(x):
        return self.alpha*x/(self.beta+x)

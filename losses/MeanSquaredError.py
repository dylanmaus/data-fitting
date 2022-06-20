"""
compute mean squared error
"""

class MeanSquaredError:
    def __init__(self, model, params, data):
        self.model = model
        self.params = params
        self.data = data
        self.data_count = len(data)
        self.loss = 0

    def compute_loss(self):
        self.loss = 0
        for i in range(data_count):
            self.loss += (self.model(data[i][:-1], params) - data[i][-1])**2
        self.loss *= 1/data_count
        return self.loss

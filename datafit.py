import copy

def linear_function(x, m, b):
	return m*x + b

def nonlinear_function(x, a, b):
	return a*x/(b+x)

class SumSquaredError:
	def __init__(self, data, func):
		self.data = data
		self.func = func

	def compute_sse(self, params):
		'''Compute SSE'''
		sse = 0
		for s in self.data:
			se = (self.func(s[0], *params) - s[1])**2
			sse += se
		return sse

def compute_gradient(f, h, t, s):
	return (f(t) - f(s))/h

# data = [[1, 2], [2, 1], [3, 4], [4, 3]]

x = [0.038, 0.194, 0.425, 0.626, 1.253, 2.500, 3.740]
y = [0.050, 0.127, 0.094, 0.2122, 0.2729, 0.2665, 0.3317]
data = []
for i in range(len(x)):
	data.append([x[i], y[i]])
# intial geuss
a = 0.9
b = 0.2
params = [a, b]
param_count = len(params)
sse_delta = 99999
h = 0.00001
steps = [1, 1]
learning_rate = 0.003
SSE = SumSquaredError(data, nonlinear_function)

while any(step > 0.0000001 for step in steps):
	for i in range(param_count):
		t = copy.deepcopy(params)
		t[i] += h
		g = compute_gradient(SSE.compute_sse, h, t, params)
		# print(g)
		steps[i] = -g*learning_rate

	for i in range(param_count):
		params[i] += steps[i]

print(params)

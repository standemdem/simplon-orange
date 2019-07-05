from layer import Layer
import numpy as np

class FCLayer(Layer):
	'''
	inherit from base class Layer
	'''
	def __init__(self, input_size, output_size):
		'''
		initialisatiing function
		:params: input_size = number of input neurons
		:params: output_size = number of output neurons
		:params: weights = weight matrice
		:params: bias = bias vector	
		'''
		self.weights = np.random.rand(input_size,output_size) - 0.5
		self.bias = np.random.rand(1,output_size) - 0.5

	def forward_propagation(self, input_data):
		'''
		returns output for a given input
		'''
		self.input = input_data
		self.output = np.dot(self.input, self.weights) + self.bias
		return self.output

	def backward_propagation(self, output_error, learning_rate):
		'''
		computes dE/dw, dE/dB, for a given output_error = dE/dY
		updates parameters
		:return: input_error = dE/dX
		'''
		input_error = np.dot(output_error, self.weights.T)
		weights_error = np.dot(self.input.T, output_error)
		dBias = output_error

		self.weights -= learning_rate * weights_error
		self.bias -= learning_rate * dBias

		return input_error
from layer import Layer

class ActivationLayer(Layer):
	'''
	inherit from base class Layer
	add the activation part giving the output of every layer
	'''
	def __init__(self, activation, activation_prime):
		'''
		initialize the activation parameters
		:params: activation = activation function of the layer
		:params: activation_prime = derivative of the activation function
		'''
		self.activation = activation
		self.activation_prime = activation_prime

	def forward_propagation(self, input_data):
		'''
		last calculation step of the forward propagation
		:returns: the activated input
		'''
		self.input = input_data
		self.output = self.activation(self.input)
		return self.output

	def backward_propagation(self, output_error, learning_rate):
		'''
		:return: the outputs of the derivated activation function
		'''
		return self.activation_prime(self.input) * output_error

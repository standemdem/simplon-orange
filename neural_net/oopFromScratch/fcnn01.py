import numpy as np

class Layer:
	'''
	contains the common characteristics of all layers:
	an input, an output, the forward / backward prop
	'''
	def __init__(self, input, output):
		'''
		initialize the params
		:params: input - what is fed into every layer
		:params: output - what is returned by every layer
		'''
		self.input = None
		self.output = None

	def forward_propagation(self, input):
		'''
		Computes the output Y of a layer for a given input X
		:params: input - what is fed to every layer
		'''
		raise NotImplementedError

	def backward_propagation(self, output_error, learning_rate):
		'''
		computes dE/dX for a given dE/dY (and update parameters if any)
		:params: output_error - 
		:params: learning_rate - rate at wich the params are updated
		'''
		raise NotImplementedError

class Network:
	''' 
	faire une explication de ce que la classe Network est censée faire
	'''

	def __init__(self):
		'''
		explications

		:param: layers => list contenant la structure du FC NN
		'''
		self.layers = []

class Error(Exception):
	'''Base Error for Exceptions.'''
	pass

class MissingInputError(Error):
	'''Exception for when a function requires an input but it is None.'''
	def __init__(self, expression):
		self.expression = expression
		self.message = 'You have passed in a None input variable.'


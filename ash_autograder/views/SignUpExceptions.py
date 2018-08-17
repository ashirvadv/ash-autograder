from ash_autograder.views.Exceptions import *

class EmailExistsError(Error):
	'''Exception that is thrown if an email is already in use.'''

	def __init__(self, expression):
		self.expression = expression
		self.message = 'You are using an email that has already been used.'

class EmailInvalidError(Error):
	'''Exception that is thrown if an email is not valid.'''

	def __init__(self, expression):
		self.expression = expression
		self.message = 'The email you provided is invalid.'

class UsernameExistsError(Error):
	'''Exception that is thrown if a username is already in use.'''

	def __init__(self, expression):
		self.expression = expression
		self.message = 'You are using a username that has already been used.'

class PasswordWeakError(Error):
	'''Exception that is thrown if the password provided is not strong enough.'''

	def __init__(self, expression):
		self.expression = expression
		self.message = 'Your password is not strong enough.'

class PasswordMatchError(Error):
	'''Exception that is thrown if the passwords provided do not match.'''

	def __init__(self, expression):
		self.expression = expression
		self.message = 'Your passwords do not match.'
from ash_autograder.views.Exceptions import *

from sqlite3 import OperationalError as SQLError

class UnequalListSizeError(Error):
	'''Exception that is thrown if a sql command is using an unqual number of elements in lists.'''

	def __init__(self, expression):
		self.expression = expression
		self.message = 'You have passed in an incorrect number of columns and data to execute.'

class TableNotExistError(Error):
	'''Exception when a table is trying to be used but does not exist.'''
	def __init__(self, expression):
		self.expression = expression
		self.message = 'You are trying to use a table that does not exist.'
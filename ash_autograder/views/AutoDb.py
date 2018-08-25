from ash_autograder.model import get_db
from ash_autograder.views.Exceptions import *
from ash_autograder.views.SQLExceptions import *

def retrieve_from_table(table_name, columns):
	'''Retrieve all rows of given columns from the table.'''
	return retrieve_from_table_condition(table_name, columns, None)

def retrieve_from_table_condition(table_name, columns, condition):
	'''Retrieve all rows of given columns from table given condition.'''
	database = get_db()
	cursor = database.cursor()
	query = build_select_command(table_name, columns, condition)

	try:
		rows = cursor.execute(query)
	except SQLError as e:
		raise SQLError

	result = rows.fetchall()
	return result

def build_select_command(table_name, columns, condition):
	'''Build the select query.'''
	if table_name == None:
		raise MissingInputError('You must specify a table_name when running a SELECT command.')

	if columns == None:
		raise MissingInputError('You must specify columns when running a SELECT command.')

	query = 'SELECT '
	query += ', '.join(columns)
	query += ' FROM ' + table_name
	if condition != None:
		query += ' WHERE ' + condition
	return query

def retrieve_max_from_table(table_name, column, condition=None):
	'''Retrieve the maximum on a column from a table.'''
	database = get_db()
	cursor = database.cursor()
	query = build_max_command(table_name, column, condition)

	try:
		rows = cursor.execute(query)
	except SQLError:
		raise SQLError

	result = rows.fetchone()
	return result


def build_max_command(table_name, column, condition=None):
	'''Build a max query.'''

	if table_name == None:
		raise MissingInputError('You must specify a table_name when running a SELECT command.')

	if column == None:
		raise MissingInputError('You must specify a column when running a SELECT command.')

	query = 'SELECT MAX(' + column + ')'
	query += ' FROM ' + table_name
	if condition != None:
		query += ' WHERE ' + condition
	return query

def insert_into_table(table_name, columns, data):
	'''Insert the following data into table_name.'''
	database = get_db()
	cursor = database.cursor()
	query = build_insert_command(table_name, columns, data)
	try:
		cursor.execute(query)
	except Exception as e:
		print(e)
	database.commit()

def build_insert_command(table_name, columns, data):
	'''Build the insert query.'''
	if table_name == None:
		raise MissingInputError('You must specify a table_name when running an INSERT command.')

	if columns == None:
		raise MissingInputError('You must specify columns when running an INSERT command.')
	
	if len(columns) != len(data):
		raise UnequalListSizeError('Occured in insert_into_table in AutoDb.py')

	query = 'INSERT INTO ' + table_name + ' ('
	query += ', '.join(columns) + ') VALUES ("'
	query += '", "'.join(data) + '")'
	return query

def update_table(table_name, columns, data):
	'''Update all rows in a table.'''
	update_table(table_name, columns, data, None)

def update_table(table_name, columns, data, condition):
	'''Update a row in the given table that satisfy the condition.'''
	database = get_db()
	cursor = database.cursor()
	query = build_update_command(table_name, columns, data, condition)
	cursor.execute(query)
	database.commit()

def build_update_command(table_name, columns, data, condition):
	'''Build the update query.'''

	if table_name == None:
		raise MissingInputError('You must specify a table_name when running an UPDATE command.')

	if columns == None:
		raise MissingInputError('You must specify columns when running an UPDATE command.')

	if data == None:
		raise MissingInputError('You must specify data when running an UPDATE command.')

	if len(columns) != len(data):
		raise UnequalListSizeError('Occured in update_table with condition in AutoDb.py')

	query = 'UPDATE ' + table_name + ' SET '
	last_index = len(columns) - 1
	for i in range(last_index):
		query += columns[i] + ' = ' + '"' + data[i] + '", '

	query += columns[last_index] + ' = ' + '"' + data[last_index] + '"'
	if condition != None:
		query += ' ' + condition
	return query
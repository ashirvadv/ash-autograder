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
	except SQLError:
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

def insert_into_table(table_name, columns, data):
	'''Insert the following data into table_name.'''
	if table_name == None:
		raise MissingInputError('You must specify a table_name when running an INSERT command.')

	if columns == None:
		raise MissingInputError('You must specify columns when running an INSERT command.')

	database = get_db()
	cursor = database.cursor()

	if len(columns) != len(data):
		raise UnequalListSizeError('Occured in insert_into_table in AutoDb.py')

	query = build_insert_command(table_name, columns, data)
	cursor.execute(query)
	database.commit()

def build_insert_command(table_name, columns, data):
	'''Build the insert query.'''
	query = 'INSERT INTO ' + table_name + '('
	query += ', '.join(columns) + ') VALUES ("'
	query += '", '.join(data) + '")'
	return query

def update_table(table_name, columns, data):
	'''Update all rows in a table.'''
	try:
		update_table(table_name, columns, data, None)
	except UnequalListSizeError:
		raise UnequalListSizeError('Occured in update_table in AutoDb.py')

def update_table(table_name, columns, data, condition):
	'''Update a row in the given table that satisfy the condition.'''
	database = get_db()
	cursor = database.cursor()

	if len(columns) != len(data):
		raise UnequalListSizeError('Occured in update_table with condition in AutoDb.py')

	query = build_update_command(table_name, columns, data, condition)
	cursor.execute(query)
	database.commit()

def build_update_command(table_name, columns, data, condition):
	'''Build the update query.'''
	query = 'UPDATE ' + table_name + ' SET '
	last_index = len(columns) - 1
	for i in range(last_index):
		query += columns[i] + ' = ' + '"' + data[i] + '",'

	query += columns[last_index] + ' = ' + '"' + data[last_index] + '"'
	if condition != None:
		query += condition
	return query
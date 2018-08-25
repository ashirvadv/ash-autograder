from ash_autograder.model import get_db
from ash_autograder.views.Exceptions import *
from ash_autograder.views.SQLExceptions import *
from ash_autograder.views.AutoDb import *

def get_user(user_id):
	'''Retrieve user row given user_id.'''
	return get_user_with_columns(user_id, ['*'])

def get_user_with_columns(user_id, columns):
	'''Retrieve user row with specific columns.'''
	condition = 'user_id = "{}"'.format(user_id)
	user = retrieve_from_table_condition('Users', columns, condition)
	return user[0]

def get_last_row():
	'''Retrieve the last row insert into the table.'''

	maximum = retrieve_max_from_table('Users', 'created')
	result = retrieve_from_table_condition('Users', ['*'], 'created = "{}"'.format(maximum['MAX(created)']))
	return result[0]

def get_all_users():
	'''Retrieve all users.'''
	return get_all_users_with_columns()

def get_all_users_with_columns(columns):
	'''Retrieve users with specific columns.'''
	users = retrieve_from_table('Users', columns)
	return users

def create_user(data):
	'''Create a user given the provided data.'''
	columns = ['first_name', 'last_name', 'email', 'password']
	data_col = [data['first_name'], data['last_name'], data['email'], data['password']]
	insert_into_table('Users', columns, data_col)

	last_row = get_last_row()
	user_id = str(last_row['user_id'])
	email = last_row['email']

	data = [email, user_id]
	col = ['email', 'user_id']
	insert_into_table('Email_to_Id', col, data)
	return last_row['user_id']

def get_user_id_from_email(email):
	'''Return user_id for an email.'''
	condition = 'email = "{}"'.format(email)
	try:
		temp = retrieve_from_table('Email_to_Id', ['*'])
		user_id = retrieve_from_table_condition('Email_to_Id', ['user_id'], condition)
		if len(user_id) == 0:
			return None
		return user_id[0]['user_id']
	except Exception as e:
		return None

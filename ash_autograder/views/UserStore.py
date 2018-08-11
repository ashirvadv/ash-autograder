from ash_autograder.model import get_db
from ash_autograder.views.Exceptions import *
from ash_autograder.views.SQLExceptions import *
from ash_autograder.views.AutoDb import *

def get_user(user_id):
	'''Retrieve user row given user_id.'''
	return get_user_with_columns(user_id, ['*'])

def get_user_with_columns(user_id, columns):
	'''Retrieve user row with specific columns.'''
	condition = 'WHERE user_id = "{}"'.format(user_id)
	user = retrieve_from_table_condition('Users', columns, condition)
	return user	

def get_all_users():
	'''Retrieve all users.'''
	return get_all_users_with_columns()

def get_all_users_with_columns(columns):
	'''Retrieve users with specific columns.'''
	users = retrieve_from_table('Users', columns)
	return users

def create_user(data):
	'''Create a user given the provided data.'''
	columns = ['first_name', 'last_name', 'email', 'username', 'password']
	insert_into_table('Users', columns, data)
	user = retrieve_from_table_condition('Users', ['user_id'])
	user_id = user['user_id']
	insert_into_table('Username_to_Id', ['username', 'user_id'])

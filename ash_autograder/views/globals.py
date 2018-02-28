"""Global functions."""
import flask
from flask import session, redirect, url_for, request
from ash_autograder.model import get_db
import ash_autograder

def get_all_table(table_name):
	"""Get all data from table specified."""
	database = get_db()
	cursor = database.execute('SELECT * FROM ' + table_name)
	return cursor.fetchall()

def get_projects():
	"""Get all data from projects table."""
	return get_all_table('projects')

def get_users():
	"""Get all users from users table."""
	return get_all_table('users')

def get_user(username):
	"""Get user with username from users table."""
	database = get_db()
	cursor = database.execute('SELECT * FROM users WHERE '
								+ 'username = ?', (username,))
	return cursor.fetchone()

def logged_in():
	"""Checks if user is logged in, else redirects to login."""
	return 'username' in session

def form_file_name(project_num, submission_num):
	"""Given project and submission, return submission filename."""
	filename = 'project_' + str(project_num)
	filename += '_submission_' + str(submission_num)
	filename += '.txt'
	return filename

def is_admin():
	"""Return true if admin is logged in."""
	return session['username'] == 'admin'

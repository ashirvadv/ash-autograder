"""Global functions."""
import flask
from flask import session, redirect, url_for, request
from ash_autograder.model import get_db

def get_all_table(table_name):
	"""Get all data from table specified."""
	database = get_db()
	cursor = database.execute('SELECT * FROM ' + table_name)
	return cursor.fetchall()

def get_projects():
	"""Get all data from projects table."""
	return get_all_table('projects')

def check_logged_in():
	"""Checks if user is logged in, else redirects to login."""
	if 'username' not in session:
		redirect(url_for('login'))

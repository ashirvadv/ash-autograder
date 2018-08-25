import flask
from flask import session, redirect, url_for, request
import ash_autograder

from ash_autograder.views.UserStore import *
from ash_autograder.views.Authenticate import *
from ash_autograder.views.Cryptography import correct_password

from ash_autograder.views.urls import LOGIN_HTML, LOGIN_URL, SIGN_UP_URL

def is_email(username):
	'''Return whether the username provided is an email.'''
	return '@' in username

def login_user_by_id(user_id, password):
	'''Login user by user_id.'''

	try:
		user = get_user(user_id)
	except Exception:
		'''Some other error came up.'''
		return redirect(url_for('show_login'))
	if not correct_password(user['password'], password):
		'''Incorrect password.'''
		return redirect(url_for('show_login'))

	insert_into_session(user['user_id'], user['email'])
	return redirect(url_for('show_dashboard'))

def login_user(username, password):
	'''Log user in.'''
	user_id = -1

	try:
		if is_email(username):
			user_id = get_user_id_from_email(username)
		else:
			user_id = get_user_id_from_username(username)
	except Exception:
		'''Username was invaild.'''
		return redirect(url_for('show_login'))

	return login_user_by_id(user_id, password)

@ash_autograder.app.route(LOGIN_URL, methods=['GET', 'POST'])
def show_login():
	'''Show sign up page.'''

	authenticated = authenticate_user()

	if authenticated == None:
		redirect(url_for('show_dashboard'))

	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		return login_user(username, password)

	context = {'SIGN_UP_URL' : SIGN_UP_URL}

	return flask.render_template(LOGIN_HTML, **context)
from flask import session, redirect, url_for, request

def authenticate_user():
	'''
	This functions asserts that the user is authenticated.
	If not, then this function will redirect to the login page.
	'''
	if 'logged_in' in session:
		return None
	else:
		return redirect(url_for('show_login'))

def insert_into_session(user_id, email=None):
	'''Include this user_id into the session.'''
	session['logged_in'] = True
	session['user_id'] = user_id
	if email != None:
		session['username'] = email
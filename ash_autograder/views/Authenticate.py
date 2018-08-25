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

def remove_elt_from_session(elt):
	'''Remove elt from session.'''
	if elt in session:
		session.pop(elt)

def remove_from_session():
	'''Remove from session.'''
	elements = []
	elements.append('logged_in')
	elements.append('user_id')
	elements.append('username')
	for elt in elements:
		remove_elt_from_session(elt)

def authenticate_admin():
	'''
	This function asserts that the user is an admin.
	'''
	authenticated = authenticate_user()

	if authenticated != None:
		return authenticated

	if session['username'] == 'ashirvad.varma@gmail.com':
		return None
	else:
		return redirect(url_for('show_dashboard'))
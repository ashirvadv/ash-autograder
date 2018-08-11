from flask import session, redirect, url_for, request

def authenticate_user():
	'''
	This functions asserts that the user is authenticated.
	If not, then this function will redirect to the login page.
	'''
	if 'logged_in' in session:
		return
	else:
		return redirect(url_for('show_login'))
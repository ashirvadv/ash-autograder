import flask
from flask import session, redirect, url_for, request
import ash_autograder

from ash_autograder.views.UserStore import *
from ash_autograder.views.SignUpException import *

def check_valid_email(email):
	'''Return if email is valid, throw exception otherwise.'''
	if '@' not in email:
		raise EmailInvalidError('Please provide a valid email address.')

	user_id = get_user_id_from_email(email)

	if user_id != None:
		raise EmailExistsError('Please provide a new email address.')

def check_valid_username(username):
	'''Return if username is valid, throw exception otherwise.'''
	user_id = get_user_id_from_username(username)

	if user_id != None:
		raise UsernameExistsError('Please provide a new username.')

def password_is_strong(password):
	'''Return true if the password is strong enough.'''
	'''
	A password is considered strong if:
	*at least 8 characters long
	*includes at least 1 number
	*includes at least 1 special character
	*includes at least 1 regular character
	'''
	num_reg = 0
	num_spec = 0
	num_int = 0

	specials = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
	numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

	for c in password:
		if c in specials:
			num_spec += 1
		elif c in numbers:
			num_int += 1
		else:
			num_reg += 1
	
	is_strong = (len(password) >= 8) and (num_reg >= 1) and (num_spec >= 1) and (num_int >= 1)

	if !is_strong:
		raise PasswordWeakError('Please input a stronger password')

def passwords_match(password1, password2):
	'''Return true if the passwords match.'''
	if password1 != password2:
		raise PasswordMatchError('Please confirm your passwords.')

def check_valid_password(password1, password2):
	'''Return if password is valid, throw exception otherwise.'''
	password_is_strong(password1)
	passwords_match(password1, password2)

def check_valid_inputs(user_data):
	'''
	Check for the following:
	Valid Email
	Valid Username
	Valid Password
	'''
	check_valid_email(user_data['email'])
	check_valid_username(user_data['username'])
	check_valid_password(user_data['password'], user_data['password2'])

def create_user_account(user_data):
	'''Given user data, create a new user.'''
	try:
		check_valid_inputs(user_data)
		create_user(user_data)
		return redirect(url_for('show_dashboard'))
	except Exception:
		return flask.render_template('sign_up.html')

@ash_autograder.app.route('/accounts/create/', methods=['GET', 'POST'])
def show_sign_up():
	'''Show sign up page.'''

	if request.method == 'POST':
		user_data = request.form.to_dict()
		return create_user_account(user_data)

	return flask.render_template('sign_up.html')
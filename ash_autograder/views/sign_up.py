import flask
from flask import session, redirect, url_for, request
import ash_autograder

from ash_autograder.views.Cryptography import hash_password
from ash_autograder.views.UserStore import *
from ash_autograder.views.SignUpExceptions import *

def check_valid_email(email):
	'''Return if email is valid, throw exception otherwise.'''
	print('check valid email')
	if '@' not in email:
		print('Invalid email')
		raise EmailInvalidError('Please provide a valid email address.')

	try:
		user_id = get_user_id_from_email(email)
	except Exception as e:
		print('got an exception here')
		print(e)
		print(e.message)
		raise e

	if user_id != None:
		print('email exists')
		raise EmailExistsError('Please provide a new email address.')

	print('ending check valid email')

def check_valid_username(username):
	'''Return if username is valid, throw exception otherwise.'''
	print('check valid username')
	user_id = get_user_id_from_username(username)

	if user_id != None:
		print('username exists')
		raise UsernameExistsError('Please provide a new username.')
	print('ending check valid username')

def password_is_strong(password):
	'''Return true if the password is strong enough.'''
	'''
	A password is considered strong if:
	*at least 8 characters long
	*includes at least 1 number
	*includes at least 1 special character
	*includes at least 1 regular character
	'''
	print('password is strong')
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

	if not is_strong:
		print('password weak error')
		raise PasswordWeakError('Please input a stronger password')
	print('ending password is strong')

def passwords_match(password1, password2):
	'''Return true if the passwords match.'''
	print('passwords match')
	if password1 != password2:
		print('password match error')
		raise PasswordMatchError('Please confirm your passwords.')
	print('ending passwords match')

def check_valid_password(password1, password2):
	'''Return if password is valid, throw exception otherwise.'''
	print('check valid password')
	password_is_strong(password1)
	passwords_match(password1, password2)
	print('ending check valid password')

def check_valid_inputs(user_data):
	'''
	Check for the following:
	Valid Email
	Valid Username
	Valid Password
	'''
	print('check valid inputs')
	check_valid_email(user_data['email'])
	check_valid_username(user_data['username'])
	check_valid_password(user_data['password'], user_data['password2'])
	print('ending check valid inputs')

def create_user_account(user_data):
	'''Given user data, create a new user.'''
	print('create user account')
	try:
		check_valid_inputs(user_data)
		print('about to hash password')
		user_data['password'] = hash_password(user_data['password'])
		print('got a hashed password: {}'.format(user_data['password']))
		create_user(user_data)
		print('created user')
		print('redirect to dashboard')
		return redirect(url_for('show_dashboard'))
	except Exception:
		print('exception')
		return flask.render_template('sign_up.html')

@ash_autograder.app.route('/accounts/create/', methods=['GET', 'POST'])
def show_sign_up():
	'''Show sign up page.'''
	print('show signup')
	if request.method == 'POST':
		print('post')
		user_data = request.form.to_dict()
		print('return create user account')
		return create_user_account(user_data)
	print('regular')
	return flask.render_template('sign_up.html')
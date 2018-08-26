import flask
from flask import session, redirect, url_for, request
import ash_autograder

from ash_autograder.views.Cryptography import hash_password
from ash_autograder.views.UserStore import *
from ash_autograder.views.Authenticate import *
from ash_autograder.views.SignUpExceptions import *

from ash_autograder.views.urls import SIGN_UP_HTML, SIGN_UP_URL, LOGIN_URL


def check_valid_email(email):
	'''Return if email is valid, throw exception otherwise.'''
	if '@' not in email:
		raise EmailInvalidError('Please provide a valid email address.')

	try:
		user_id = get_user_id_from_email(email)
	except Exception as e:
		raise e

	if user_id != None:
		raise EmailExistsError('Please provide a new email address.')

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

	if not is_strong:
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
	check_valid_password(user_data['password'], user_data['password2'])

def render_sign_up(context={}):
	'''Return the sign up page.'''
	context['LOGIN_URL'] = LOGIN_URL
	return flask.render_template(SIGN_UP_HTML, **context)

def create_user_account(user_data):
	'''Given user data, create a new user.'''
	try:
		check_valid_inputs(user_data)

		user_data['password'] = hash_password(user_data['password'])
		user_id = create_user(user_data)

		insert_into_session(user_id, user_data['email'])
		
		return redirect(url_for('show_dashboard'))
	except Exception as e:
		return render_sign_up()

@ash_autograder.app.route(SIGN_UP_URL, methods=['GET', 'POST'])
def show_sign_up():
	'''Show sign up page.'''
	if request.method == 'POST':
		user_data = request.form.to_dict()
		return create_user_account(user_data)

	return render_sign_up()
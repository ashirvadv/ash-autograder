import hashlib
import flask
from flask import session, redirect, url_for, request
import ash_autograder
from ash_autograder.views.globals import get_user, logged_in

def user_not_exist(user):
	return user is None

def password_not_match(correct, input):
	return correct is not input

def find_salt(password):
    """Find salt."""
    start = password.index('$') + len('$')
    end = password.index('$', start)
    return password[start:end]


def hash_password(password, pass_db):
    """Hash password."""
    algorithm = 'sha512'
    salt = find_salt(pass_db)
    hash_obj = hashlib.new(algorithm)
    password_salted = salt + password
    hash_obj.update(password_salted.encode('utf-8'))
    password_hash = hash_obj.hexdigest()
    password_db_string = "$".join([algorithm, salt, password_hash])
    return password_db_string

def login(username, password):
	user = get_user(username)

	if user_not_exist(user):
		return flask.render_template('login.html')

	hashed_password = hash_password(password, user['password'])

	if password_not_match(user['password'], hashed_password):
		return flask.render_template('login.html')

	session['username'] = username
	return redirect(url_for('show_index'))


@ash_autograder.app.route('/accounts/login/', methods=['GET', 'POST'])
def show_login():
	"""Display login page."""

	if request.method is 'POST':
		return login(request.form['username'], request.form['password'])
	
	if logged_in():
		return redirect(url_for('show_index'))

	return flask.render_template('login.html')
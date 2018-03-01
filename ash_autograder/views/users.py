from functools import wraps
import flask
from flask import session, redirect, url_for, request
import ash_autograder
from ash_autograder.views.globals import is_admin, logged_in, get_users

@ash_autograder.app.route('/users/', methods=['GET'])
def show_users():
	"""Show users."""
	if not logged_in():
		redirect(url_for('show_index'))

	if not is_admin():
		redirect(url_for('show_index'))

	users = get_users()

	context = {'users': users}

	return flask.render_template('users.html', **context)
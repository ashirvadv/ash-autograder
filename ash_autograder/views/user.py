from functools import wraps
import flask
from flask import session, redirect, url_for, request
import ash_autograder
from ash_autograder.views.globals import get_projects, logged_in, get_user

@ash_autograder.app.route('/user/', methods=['GET'])
def show_user():
	"""Show users."""
	if logged_in() == False:
		return redirect(url_for('show_index'))

	projects = get_projects()
	user = get_user(session['username'])

	context = {'user': user, 'projects': projects}

	return flask.render_template('user.html', **context)
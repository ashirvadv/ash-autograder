import flask
from flask import session, redirect, url_for, request
import ash_autograder
from ash_autograder.views.Authenticate import authenticate_user


@ash_autograder.app.route('/dashboard/', methods=['GET', 'POST'])
def show_dashboard():
	'''Show dashboard page.'''

	authenticated = authenticate_user()

	if authenticated != None:
		return authenticated

	username = session['username']
	user_id = session['user_id']

	return flask.render_template('dashboard.html')
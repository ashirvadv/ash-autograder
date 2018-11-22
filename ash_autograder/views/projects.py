import flask
from flask import session, redirect, url_for, request
import ash_autograder
from ash_autograder.views.Authenticate import authenticate_user
from ash_autograder.views.ProjectStore import *
from ash_autograder.views.urls import LOGOUT_URL, PROJECTS_URL


@ash_autograder.app.route(PROJECTS_URL, methods=['GET'])
def show_projects():
	'''Show projects page.'''

	authenticated = authenticate_user()

	if authenticated != None:
		return authenticated

	username = session['username']
	user_id = session['user_id']

	projects = get_all_projects(user_id)

	context = {'username': username, 'user_id': user_id}
	context['LOGOUT_URL'] = LOGOUT_URL
	context['projects'] = projects

	return flask.render_template(PROJECTS_URL, **context)
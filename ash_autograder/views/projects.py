import flask
from flask import session, redirect, url_for, request
import ash_autograder
from ash_autograder.views.Authenticate import authenticate_user, authenticate_admin
from ash_autograder.views.ProjectStore import *
from ash_autograder.views.urls import LOGOUT_URL, PROJECTS_URL, PROJECTS_HTML


def get_project_numbers(projects):
	'''Get project numbers.'''
	result = [project['project_id'] for project in projects]
	return result


@ash_autograder.app.route(PROJECTS_URL, methods=['GET'])
def show_projects():
	'''Show projects page.'''

	authenticated = authenticate_user()

	if authenticated != None:
		return authenticated

	username = session['username']
	user_id = session['user_id']

	if authenticate_admin() == None:
		projects = get_all_projects()
	else:
		projects = get_all_projects(user_id)
	projects = get_project_numbers(projects)

	context = {'username': username, 'user_id': user_id}
	context['LOGOUT_URL'] = LOGOUT_URL
	context['projects'] = projects

	return flask.render_template(PROJECTS_HTML, **context)
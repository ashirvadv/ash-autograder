import flask
from flask import session, redirect, url_for, request
import ash_autograder
from ash_autograder.views.Authenticate import authenticate_admin
from ash_autograder.views.ProjectStore import get_all_projects
from ash_autograder.views.urls import *

@ash_autograder.app.route(ADMIN_PROJECTS_URL, methods=['GET'])
def show_admin_projects():
	'''Show admin projects page.'''

	authenticated = authenticate_admin()

	if authenticated != None:
		return authenticated

	projects = get_all_projects()
	context = {'projects': projects}
	context['LOGOUT_URL'] = LOGOUT_URL
	context['ADMIN_PROJECTS_CREATE_URL'] = ADMIN_PROJECTS_CREATE_URL

	return flask.render_template(ADMIN_PROJECTS_HTML, **context)
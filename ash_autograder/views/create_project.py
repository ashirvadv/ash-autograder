import flask
from flask import session, redirect, url_for, request
import ash_autograder
from ash_autograder.views.Authenticate import authenticate_admin
from ash_autograder.views.ProjectStore import *
from ash_autograder.views.urls import DASHBOARD_HTML, DASHBOARD_URL, LOGOUT_URL

@ash_autograder.app.route(DASHBOARD_URL, methods=['GET', 'POST'])
def show_create_project():
	'''Show create project page.'''

	authenticated = authenticate_admin()

	if authenticated != None:
		return authenticated

	projects = get_all_projects()
	context = {'projects': projects}
	context['LOGOUT_URL'] = LOGOUT_URL

	return flask.render_template(DASHBOARD_HTML, **context)
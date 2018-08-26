import flask
from flask import session, redirect, url_for, request
import ash_autograder
from ash_autograder.views.Authenticate import authenticate_admin
from ash_autograder.views.ProjectStore import *
from ash_autograder.views.urls import ADMIN_PROJECTS_CREATE_HTML, ADMIN_PROJECTS_CREATE_URL, LOGOUT_URL

def render_create_project():
	'''Render create project.'''
	context = {'LOGOUT_URL': LOGOUT_URL}
	return flask.render_template(ADMIN_PROJECTS_CREATE_HTML, **context)

def create_new_project(project_name, files):
	'''Create new project.'''
	try:
		filename = files['filename']
		starter_files = files['starter_files']
		autograder = files['autograder']
	except Exception as e:
		return render_create_project()

@ash_autograder.app.route(ADMIN_PROJECTS_CREATE_URL, methods=['GET', 'POST'])
def show_admin_create_project():
	'''Show create project page.'''

	authenticated = authenticate_admin()

	if authenticated != None:
		return authenticated

	if request.method == 'POST':
		return create_new_project(request.form.project_name, request.files)

	return render_create_project()
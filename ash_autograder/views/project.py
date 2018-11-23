import flask
from flask import session, redirect, url_for, request
import ash_autograder
from ash_autograder.views.Authenticate import authenticate_user
from ash_autograder.views.ProjectStore import *
from ash_autograder.views.urls import LOGOUT_URL, PROJECT_URL, PROJECT_HTML
from ash_autograder.config import UPLOAD_FOLDER
import os



@ash_autograder.app.route(os.path.join(PROJECT_URL, '<path:filename>'))
def download_file(project_id, filename):
	'''Download file.'''
	path = os.path.join(UPLOAD_FOLDER, 'project_{}'.format(str(project_id)))
	return flask.send_from_directory(path, filename, as_attachment=True)


@ash_autograder.app.route(PROJECT_URL, methods=['GET'])
def show_project(project_id):
	'''Show project page.'''

	authenticated = authenticate_user()

	if authenticated != None:
		return authenticated

	username = session['username']
	user_id = session['user_id']

	context = {'username': username, 'user_id': user_id, 'num': project_id}

	project = get_project_by_id(project_id)

	context['project_name'] = project['project_name']
	context['spec_filename'] = project['filename']
	context['starter_files'] = project['starter_files']
	context['LOGOUT_URL'] = LOGOUT_URL

	return flask.render_template(PROJECT_HTML, **context)
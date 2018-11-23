import flask
from flask import session, redirect, url_for, request
import ash_autograder
from ash_autograder.views.Authenticate import authenticate_user, authenticate_admin
from ash_autograder.views.ProjectStore import *
from ash_autograder.views.urls import LOGOUT_URL, PROJECT_URL, PROJECT_HTML
from ash_autograder.config import UPLOAD_FOLDER
from ash_autograder.views.admin_create_project import build_project_path, upload_file
import os


@ash_autograder.app.route(os.path.join(PROJECT_URL, '<path:filename>'))
def download_file(project_id, filename):
	'''Download file.'''
	path = build_project_path(project_id)
	return flask.send_from_directory(path, filename, as_attachment=True)


def update_file(project_id, file, filename):
	'''Update file.'''
	upload_file(project_id, file)
	update_project_file(project_id, filename, file.filename)


def update_files(project_id, files):
	'''Update files.'''
	print(files)
	for key in files:
		update_file(project_id, files[key], key)


@ash_autograder.app.route(PROJECT_URL, methods=['GET', 'POST'])
def show_project(project_id):
	'''Show project page.'''

	authenticated = authenticate_user()

	if authenticated != None:
		return authenticated

	if authenticate_admin() != None:
		is_admin = False
	else:
		is_admin = True

	username = session['username']
	user_id = session['user_id']

	context = {'username': username, 'user_id': user_id, 'num': project_id}
	context['is_admin'] = is_admin

	project = get_project_by_id(project_id)

	context['project_name'] = project['project_name']
	context['spec_filename'] = project['filename']
	context['starter_files'] = project['starter_files']
	context['LOGOUT_URL'] = LOGOUT_URL

	if request.method == 'POST':
		update_files(project_id, request.files)

	return flask.render_template(PROJECT_HTML, **context)
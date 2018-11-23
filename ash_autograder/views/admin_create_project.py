import flask
from flask import session, redirect, url_for, request
import ash_autograder
from ash_autograder.views.Authenticate import authenticate_admin
from ash_autograder.views.ProjectStore import *
from ash_autograder.views.urls import ADMIN_PROJECTS_CREATE_HTML, ADMIN_PROJECTS_CREATE_URL, LOGOUT_URL

import os
import shutil
import tempfile
from ash_autograder.config import UPLOAD_FOLDER


def render_create_project():
	'''Render create project.'''
	context = {'LOGOUT_URL': LOGOUT_URL}
	return flask.render_template(ADMIN_PROJECTS_CREATE_HTML, **context)


def build_project_path(num):
	'''Build project path.'''
	result = os.path.join(UPLOAD_FOLDER, 'project_{}'.format(num))
	# result = UPLOAD_FOLDER + '/project_{}/'.format(num)
	return result


def upload_file(proj_num, file):
	'''Upload file into directory.'''
	dummy, temp_filename = tempfile.mkstemp()
	file.save(temp_filename)
	path = os.path.join(build_project_path(proj_num), file.filename)
	shutil.move(temp_filename, path)


def create_new_project_folder(id):
	'''Create new project folder.'''
	path = build_project_path(id)
	os.makedirs(path)


def create_new_project(project_name, files):
	'''Create new project.'''
	try:
		filename = files['filename']
		starter_files = files['starter_files']
		autograder = files['autograder']
		add_new_project(project_name, filename.filename, starter_files.filename, autograder.filename)
		proj_id = get_project_id_by_name(project_name)
		create_new_project_folder(proj_id)
		upload_file(proj_id, filename)
		upload_file(proj_id, starter_files)
		upload_file(proj_id, autograder)
		return render_create_project()
	except Exception as e:
		return render_create_project()


@ash_autograder.app.route(ADMIN_PROJECTS_CREATE_URL, methods=['GET', 'POST'])
def show_admin_create_project():
	'''Show create project page.'''

	authenticated = authenticate_admin()

	if authenticated != None:
		return authenticated

	if request.method == 'POST':
		return create_new_project(request.form['project_name'], request.files)

	return render_create_project()

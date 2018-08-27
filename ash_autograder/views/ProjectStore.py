from ash_autograder.model import get_db
from ash_autograder.views.Exceptions import *
from ash_autograder.views.SQLExceptions import *
from ash_autograder.views.AutoDb import *

def get_all_projects(user_id=None):
	'''Get all projects for a given user.'''
	if user_id == None:
		projects = retrieve_from_table('Projects', ['*'])
		return projects
	condition = 'user_id = "{}"'.format(user_id)
	projects = retrieve_from_table_condition('Project_Permissions', ['project_id'], condition)
	return projects

def get_project_by_name(name):
	'''Get project of given name.'''
	condition = 'project_name = "{}"'.format(name)
	result = retrieve_from_table_condition('Projects', ['project_id'], condition)
	return result[0]['project_id']

def add_new_project(name, filename, starter_files, autograder):
	'''Add new project to database.'''
	table_name = 'Projects'
	columns = ['project_name', 'filename']
	data = [name, filename]

	if starter_files != None:
		columns.append('starter_files')
		data.append(starter_files)

	if autograder != None:
		columns.append('autograder')
		data.append(autograder)

	insert_into_table(table_name, columns, data)
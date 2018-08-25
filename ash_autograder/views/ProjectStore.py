from ash_autograder.model import get_db
from ash_autograder.views.Exceptions import *
from ash_autograder.views.SQLExceptions import *
from ash_autograder.views.AutoDb import *

def get_all_projects():
	'''Get all projects.'''
	projects = retrieve_from_table('Projects', ['*'])
	return projects
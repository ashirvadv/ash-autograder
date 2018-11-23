from ash_autograder.model import get_db
from ash_autograder.views.Exceptions import *
from ash_autograder.views.SQLExceptions import *
from ash_autograder.views.AutoDb import *


def build_submission_table_name(user_id, project_id):
	'''Create string of submission table name.'''
	result = '{}_{}_submissions'.format(str(user_id), str(project_id))
	return result


def submission_table_exists(user_id, project_id):
	'''Return true if user has a submission table for project_id.'''
	table_name = build_submission_table_name(user_id, project_id)
	return table_exists(table_name)


def create_submission_table(user_id, project_id):
	'''Create a submission table for user_id for project_id.'''
	table_name = build_submission_table_name(user_id, project_id)
	database = get_db()
	cursor = database.cursor()
	query = 'CREATE TABLE {}(submission_id INTEGER NOT NULL, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL, score REAL, PRIMARY KEY(submission_id))'.format(table_name)
	cursor.execute(query)
	database.commit()


def get_all_submissions_for_project(user_id, project_id):
	'''Return all rows in table for user_id and project_id.'''
	table_name = build_submission_table_name(user_id, project_id)
	return retrieve_from_table(table_name, ['*'])


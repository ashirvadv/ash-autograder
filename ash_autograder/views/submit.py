import flask
from flask import session, redirect, url_for, request
import ash_autograder
from ash_autograder.views.Authenticate import authenticate_user
from ash_autograder.views.SubmitStore import *
from ash_autograder.views.urls import LOGOUT_URL, SUBMIT_URL, SUBMIT_HTML


@ash_autograder.app.route(SUBMIT_URL, methods=['GET'])
def show_submit(project_id):
	'''Show autograder for project_id page.'''

	authenticated = authenticate_user()

	if authenticated != None:
		return authenticated

	username = session['username']
	user_id = session['user_id']
	submissions = get_all_submissions_for_project(user_id, project_id)

	context = {'username': username, 'user_id': user_id, 'num': project_id}
	context['submissions'] = submissions
	context['LOGOUT_URL'] = LOGOUT_URL
	context['best_score'] = 100
	context['best_id'] = 4

	return flask.render_template(SUBMIT_HTML, **context)
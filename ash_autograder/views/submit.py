from functools import wraps
import flask
from flask import session, redirect, url_for, request
import ash_autograder
from ash_autograder.views.globals import *
from ash_autograder.views.grader import *


@ash_autograder.app.route('/autograde/<project_num>/', methods=['GET', 'POST'])
def show_autograder(project_num):
	"""Display submissions/autograder route."""

	#if post request
	if not logged_in():
		return redirect(url_for('show_index'))

	if not project_visible_to_user(session['username'], project_num):
		return redirect(url_for('show_index'))

	making_submit = False;
	if session['username'] in USERNAME_SUBMIT:
		making_submit = True
	
	logname = session['username']
	submissions = get_submissions_for_project(logname, project_num)

	submits_exist = False

	if len(submissions) > 0:
		submits_exist = True

	context = {'logname' : logname, 'submissions' : submissions, 'project_num': project_num, 'submits_exist' : submits_exist, 'making_submit' : making_submit}
	return flask.render_template("submit.html", **context)

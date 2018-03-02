from functools import wraps
import flask
from flask import session, redirect, url_for, request
import ash_autograder
from ash_autograder.views.globals import logged_in, get_submissions_for_project


@ash_autograder.app.route('/autograde/<project_num>', methods=['GET'])
def show_autograder(project_num):
	"""Display submissions/autograder route."""

	if not logged_in():
		return redirect(url_for('show_index'))

	logname = session['username']
	submissions = get_submissions_for_project(logname, project_num)


	context = {'logname' : logname, 'submissions' : submissions, 'project_num': project_num}
	return flask.render_template("submit.html", **context)

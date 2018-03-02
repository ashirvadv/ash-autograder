from functools import wraps
import flask
from flask import session, redirect, url_for, request
import ash_autograder
from ash_autograder.views.globals import logged_in, get_submission


@ash_autograder.app.route('/submission/<submission_id>', methods=['GET'])
def show_submission(submission_id):
	"""Display submission route."""

	if not logged_in():
		return redirect(url_for('show_index'))

	#add some error checking for what if the submission doesnt exist?

	logname = session['username']
	submission = get_submission(submission_id)

	if submission is None:
		#redirect
		return redirect(url_for('show_autograder'))

	project_num = submission['projectid']


	context = {'logname' : logname, 'submission' : submission, 'project_num': project_num}
	return flask.render_template("submission.html", **context)

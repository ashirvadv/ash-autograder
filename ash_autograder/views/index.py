import flask
from flask import session, redirect, url_for, request
import ash_autograder
from ash_autograder.views.globals import get_projects, check_logged_in


@ash_autograder.app.route('/', methods=['GET'])
def show_index():
	"""Display / route."""

	projects = get_projects()

	logname = ''
	if 'username' not in session:
		logname = 'ash'
	else:
		logname = session['username']

	context = {'logname' : logname, 'projects' : projects}
	return flask.render_template("index.html", **context)

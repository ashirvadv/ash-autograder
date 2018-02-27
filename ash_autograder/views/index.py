from functools import wraps
import flask
from flask import session, redirect, url_for, request
import ash_autograder
from ash_autograder.views.globals import get_projects, logged_in

def login_required(func):
    """Require login."""
    @wraps(func)
    def wrap(*args, **kwargs):
        """Wrap."""
        if 'username' in session:
            return func(*args, **kwargs)
        return redirect(url_for('show_login'))
    return wrap

@ash_autograder.app.route('/', methods=['GET'])
def show_index():
	"""Display / route."""

	if not logged_in():
		return redirect(url_for('show_login'))

	projects = get_projects()

	logname = session['username']

	context = {'logname' : logname, 'projects' : projects}
	return flask.render_template("index.html", **context)

import flask
from flask import session, redirect, url_for, request
import ash_autograder
from ash_autograder.views.Authenticate import authenticate_user, remove_from_session

from ash_autograder.views.urls import LOGOUT_URL

@ash_autograder.app.route(LOGOUT_URL, methods=['GET', 'POST'])
def show_logout():
	'''Show logout page.'''

	authenticated = authenticate_user()

	if authenticated != None:
		return authenticated

	remove_from_session()

	return redirect(url_for('show_login'))
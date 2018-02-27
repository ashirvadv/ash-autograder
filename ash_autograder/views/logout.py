from flask import session, redirect, url_for
import ash_autograder
from ash_autograder.views.index import login_required
import ash_autograder.views.login


@ash_autograder.app.route('/accounts/logout/')
@login_required
def logout():
    """Logout/remove session."""
    session.pop('username', None)
    return redirect(url_for('show_login'))

import flask
import ash_autograder


@ash_autograder.app.route('/')
def show_index():
    """Display / route."""
    context = {}
    return flask.render_template("index.html", **context)

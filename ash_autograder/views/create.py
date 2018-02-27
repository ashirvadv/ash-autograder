import uuid
import hashlib
import os
import shutil
import tempfile
import flask
from flask import session, redirect, url_for, request
import ash_autograder
from ash_autograder.model import get_db
from ash_autograder.config import UPLOAD_FOLDER

def sha256sum(filename):
	"""Return sha256 hash of file content, similar to UNIX sha256sum."""
	content = open(filename, 'rb').read()
	sha256_obj = hashlib.sha256(content)
	return sha256_obj.hexdigest()

def hash_new_pass(password):
	"""Hash new pass."""
	algorithm = 'sha512'
	salt = uuid.uuid4().hex
	hashobj = hashlib.new(algorithm)
	passwordsalted = salt + password
	hashobj.update(passwordsalted.encode('utf-8'))
	password_hash = hashobj.hexdigest()
	passworddbstring = "$".join([algorithm, salt, password_hash])
	return passworddbstring

def upload_file(temp_file):
	"""Upload file."""
	dummy, temp_filename = tempfile.mkstemp()
	file = temp_file
	file.save(temp_filename)

	hash_txt = sha256sum(temp_filename)
	dummy, suffix = os.path.splitext(file.filename)
	hash_filename_basename = hash_txt + suffix
	hash_filename = hash_filename_basename

	shutil.move(temp_filename, UPLOAD_FOLDER + '/' + hash_filename)
	ash_autograder.app.logger.debug("Saved %s", hash_filename_basename)

	return hash_filename

def create_account(username, fullname, email, file, password):
	"""Create Account."""
	database = get_db()
	cursor = database.cursor()
	hash_password = hash_new_pass(password)
	hash_filename = upload_file(file)
	cursor = cursor.execute("INSERT INTO users (username, fullname, email, filename, password) VALUES (?, ?, ?, ?, ?)",
							(username, fullname, email, hash_filename,
							 hash_password))

	database.commit()

	session['username'] = username
	return redirect(url_for('show_index'))

@ash_autograder.app.route('/uploads/<filename>', methods=['GET', 'POST'])
def create_filename_create(filename):
	"""Create filename url login."""
	return flask.send_from_directory(ash_autograder.app.config['UPLOAD_FOLDER'],
									 filename, as_attachment=True)

@ash_autograder.app.route('/accounts/create/', methods=['GET', 'POST'])
def show_create():
	"""Create account."""
	if request.method == 'POST':
		return create_account(request.form['username'], 
								request.form['fullname'],
								request.form['email'],
								request.files['file'],
								request.form['password'])

	#if already logged, go to edit page

	return flask.render_template('create.html')
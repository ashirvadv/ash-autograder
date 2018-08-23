import ash_autograder
from flask.ext.bcrypt import Bcrypt

def hash_password(password):
	'''Use some encryption algorithm to hash the inputted password.'''
	bcrypt = Bcrypt(ash_autograder.app)
	result = bcrypt.generate_password_hash(password)
	return result.decode('utf-8')

def correct_password(correct, password):
	'''Check if the input password is correct.'''
	bcrypt = Bcrypt(ash_autograder.app)
	return bcrypt.check_password_hash(correct.encode('utf-8'), password)

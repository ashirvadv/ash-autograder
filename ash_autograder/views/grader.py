import os

def run_command(command):
	"""Return bash command."""
	return os.system(command)

def get_current_path():
	"""Return the current path."""
	return run_command('pwd')

def get_path_string():
	"""Return string of current path."""
	return os.getcwd()
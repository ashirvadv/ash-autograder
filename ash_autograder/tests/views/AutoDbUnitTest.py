from ash_autograder.views.AutoDb import *
from ash_autograder.views.SQLExceptions import *

from ash_autograder.views.globals import get_all_methods_from_class

class AutoDbUnitTests:
	'''SELECT STATEMENT TESTS'''

	@classmethod
	def test_select_no_table(self):
		'''Test that the NoInputError is raised when no table_name is provided.'''
		try:
			query = build_select_command(None, ['col1'], None)
		except MissingInputError:
			return
		except Exception:
			pass
		assert False

	@classmethod
	def test_select_no_columns(self):
		'''Test that the NoInputError is raised when no columns are provided.'''
		try:
			query = build_select_command('table', None, None)
		except MissingInputError:
			return
		except Exception:
			pass
		assert False

	@classmethod
	def test_select_single_column(self):
		'''Test that build_select_command works for a single column passed in.'''
		try:
			query = build_select_command('table', ['col'], None)
		except Exception:
			assert False
		assert query == 'SELECT col FROM table'

	@classmethod
	def test_select_single_column_with_condition(self):
		'''Test that build_select_command works for a single column passed in.'''
		try:
			query = build_select_command('table', ['col'], 'col = 5')
		except Exception:
			assert False
		assert query == 'SELECT col FROM table WHERE col = 5'

	@classmethod
	def test_select_mult_column(self):
		'''Test that build_select_command works for multiple columns passed in.'''
		try:
			query = build_select_command('table', ['col1', 'col2'], None)
		except Exception:
			assert False
		assert query == 'SELECT col1, col2 FROM table'

	@classmethod
	def test_select_mult_column_with_condition(self):
		'''Test that build_select_command works for multiple columns passed in.'''
		try:
			query = build_select_command('table', ['col1', 'col2'], 'col2 = 5')
		except Exception:
			assert False
		assert query == 'SELECT col1, col2 FROM table WHERE col2 = 5'	

	'''INSERT STATEMENT TESTS'''

	@classmethod
	def test_insert_no_table(self):
		'''Test that the NoInputError is raised when no table_name is provided.'''
		try:
			query = build_insert_command(None, ['col1'], ['data'])
		except MissingInputError:
			return
		except Exception:
			pass
		assert False

	@classmethod
	def test_insert_no_columns(self):
		'''Test that the NoInputError is raised when no columns are provided.'''
		try:
			query = build_insert_command('table', None, None)
			print(query)
		except MissingInputError:
			return
		except Exception:
			pass
		assert False

	@classmethod
	def test_insert_unequal_lists(self):
		'''Test that when provided a list of columns and a different size list of data, this fails.'''
		try:
			query = build_insert_command('table', ['col1'], ['d', 'a'])
		except UnequalListSizeError:
			return
		except Exception:
			pass
		assert False

	@classmethod
	def test_insert_single_column(self):
		'''Test that when provided a single column and data insert builds correct string.'''
		try:
			query = build_insert_command('table', ['col1'], ['a'])
			assert query == 'INSERT INTO table (col1) VALUES ("a")'
			return
		except Exception:
			assert False
		assert False

	@classmethod
	def test_insert_mult_columns(self):
		'''Test that insert builds string for multiple columns of data.'''
		try:
			query = build_insert_command('table', ['col1', 'col2', 'col3'], ['a', 'b', 'c'])
			assert query == 'INSERT INTO table (col1, col2, col3) VALUES ("a", "b", "c")'
			return
		except Exception:
			assert False
		assert False

	'''UPDATE STATEMENT TESTS'''

	@classmethod
	def test_update_no_table(self):
		'''Test for no table provided as input.'''
		try:
			query = build_update_command(None, ['col'], ['data'], 'WHERE col = 1')
		except MissingInputError:
			return
		except Exception:
			pass
		assert False

	@classmethod
	def test_update_no_columns(self):
		'''Test for no columns provided as input.'''
		try:
			query = build_update_command('table', None, ['data'], 'WHERE col = 1')
		except MissingInputError:
			return
		except Exception:
			pass
		assert False

	@classmethod
	def test_update_no_data(self):
		'''Test for no data provided as input.'''
		try:
			query = build_update_command('table', ['col'], None, 'WHERE col = 1')
		except MissingInputError:
			return
		except Exception:
			pass
		assert False

	@classmethod
	def test_update_unequal_list(self):
		'''Test for unequal list sizes.'''
		try:
			query = build_update_command('table', ['col'], ['a', 'b'], 'WHERE col = 1')
		except UnequalListSizeError:
			return
		except Exception:
			pass
		assert False

	@classmethod
	def test_update_single_column(self):
		'''Test for a single column provided.'''
		try:
			query = build_update_command('table', ['col'], ['a'], None)
			assert query == 'UPDATE table SET col = "a"'
			return
		except Exception:
			pass
		assert False

	@classmethod
	def test_update_single_column_with_condition(self):
		'''Test for a single column with condition provided.'''
		try:
			query = build_update_command('table', ['col'], ['a'], 'WHERE col = "b"')
			assert query == 'UPDATE table SET col = "a" WHERE col = "b"'
			return
		except Exception:
			pass
		assert False		

	@classmethod
	def test_update_mult_column(self):
		'''Test for multiple columns provided.'''
		try:
			query = build_update_command('table', ['col', 'col2'], ['a', 'b'], None)
			assert query == 'UPDATE table SET col = "a", col2 = "b"'
			return
		except Exception:
			pass
		assert False

	@classmethod
	def test_update_mult_column_with_condition(self):
		'''Test for multiple columns with condition provided.'''
		try:
			query = build_update_command('table', ['col', 'col2'], ['a', 'b'], 'WHERE col = "b"')
			assert query == 'UPDATE table SET col = "a", col2 = "b" WHERE col = "b"'
			return
		except Exception:
			pass
		assert False

def print_result(num_run, num_passed):
	'''Print out the result of the tests.'''
	print('{} tests ran!'.format(num_run))
	print('{} tests passed!'.format(num_passed))
	print('{} tests failed!'.format(num_run - num_passed))

def main():
	'''Run Tests.'''
	num_tests_run = 0
	num_tests_passed = 0

	test_class = 'AutoDbUnitTests.'
	tests = get_all_methods_from_class(AutoDbUnitTests)

	for test in tests:
		try:
			exec(test_class + test + '()')
			num_tests_passed += 1
		except AssertionError:
			print(str(test) + ' FAILED')
		num_tests_run += 1

	print_result(num_tests_run, num_tests_passed)

main()
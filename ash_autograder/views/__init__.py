'''
example:
from ash_autograder.views.index import show_index
'''

'''
DASHBOARD PAGES
'''
# /
from ash_autograder.views.dashboard import show_dashboard

'''
USER ACCOUNT PAGES
'''
# /accounts/create/
from ash_autograder.views.sign_up import show_sign_up
# /accounts/login/
from ash_autograder.views.login import show_login
# /accounts/logout/
from ash_autograder.views.logout import show_logout
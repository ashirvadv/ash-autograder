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


'''
PROJECT PAGES
'''

# /projects/
from ash_autograder.views.projects import show_projects

# /project/<project_id>/
from ash_autograder.views.project import show_project, download_file


'''
AUTOGRADER PAGES
'''
# /submit/<project_id>/
from ash_autograder.views.submit import show_submit

# /submission/<submit_id>/
# from ash_autograder.views.projects import show_projects


'''
ADMIN PAGES
'''

# /admin/projects/
from ash_autograder.views.admin_projects import show_admin_projects

# /admin/projects/create/
from ash_autograder.views.admin_create_project import show_admin_create_project
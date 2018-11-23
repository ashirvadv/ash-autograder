'''This page contains all the html pages that correspond to urls.'''

'''
DASHBOARD PAGES
'''
# /
DASHBOARD_URL = '/'
DASHBOARD_HTML = 'dashboard.html'

'''
USER ACCOUNT PAGES
'''
# /accounts/create/
SIGN_UP_URL = '/accounts/create/'
SIGN_UP_HTML = 'sign_up.html'

# /accounts/login/
LOGIN_URL = '/accounts/login/'
LOGIN_HTML = 'login.html'

# /accounts/logout/
LOGOUT_URL = '/accounts/logout/'


'''
PROJECT PAGES
'''

# /projects/
PROJECTS_URL = '/projects/'
PROJECTS_HTML = 'projects.html'

# /project/<project_id>/
PROJECT_URL = '/project/<project_id>/'
PROJECT_HTML = 'project.html'


'''
AUTOGRADER PAGES
'''
# /submit/<project_id>/
SUBMIT_URL = '/submit/<project_id>/'

# /submission/<submit_id>/
SUBMISSION_URL = '/submission/<submit_id>/'


'''
ADMIN PAGES
'''

# /admin/projects/
ADMIN_PROJECTS_URL = '/admin/projects/'
ADMIN_PROJECTS_HTML = 'admin_projects.html'

# /admin/projects/create/
ADMIN_PROJECTS_CREATE_URL = '/admin/projects/create/'
ADMIN_PROJECTS_CREATE_HTML = 'admin_create_project.html'
import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.project_slug}}'

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: The project slug (%s) is not a valid Python module name. Please do not use a - and use _ instead' % module_name)

    #Exit to cancel project
    sys.exit(1)
    
    
PROJECT_NAME_REGEX = r'^([A-Z0-9]|[A-Z0-9][A-Z0-9._-]*[A-Z0-9])$'

project_name = '{{ cookiecutter.project_name }}'

if not re.match(PROJECT_NAME_REGEX, project_name, re.IGNORECASE ):
    print(f'ERROR: The project name ({project_name}) is not a valid Python project name.') 

    #Exit to cancel project
    sys.exit(1)

import json
import os
import sys


# Ensure the selected project slug is usable
project_slug = '{{ cookiecutter.project.slug }}'
assert_msg = 'Project slug should be valid Python identifier!'


import re
identifier_re = re.compile(r"[a-zA-Z][a-zA-Z0-9_-]*$")
assert bool(identifier_re.match(project_slug)), assert_msg


valid_cms_key = ['y', 'n']
if "{{ cookiecutter.cms }}" not in valid_cms_key:
    print("Include CMS '{{ cookiecutter.cms }}' is not valid!")
    print("Valid include CMS keys are: %s" % ', '.join(valid_cms_key))
    sys.exit(1)


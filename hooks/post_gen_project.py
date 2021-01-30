#!/usr/bin/env python
import os
from glob import iglob
from pathlib import Path

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')

    if '{{ cookiecutter.create_banner}}' != 'y':
        search_str = Path(PROJECT_DIRECTORY).joinpath('**/common/screen.py')
        screen_files = [f for f in iglob(str(search_str), recursive=True)]
        [os.remove(f) for f in screen_files]

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')
    
    #if common folder is essentially empty then delete it
    search_str = Path(PROJECT_DIRECTORY).joinpath('**/common/*.py')
    common_files = [Path(f) for f in iglob(str(search_str), recursive=True)]
    if len(common_files) == 1:
        if common_files[0].name == '__init__.py':
            common_files[0].unlink()
            common_files[0].parent.rmdir()



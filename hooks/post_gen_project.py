#!/usr/bin/env python
import os
from glob import iglob
from pathlib import Path
from shutil import rmtree

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    if not Path(filepath).exists:
        return
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    #Erase github workflows directory if not wanted
    if '{{ cookiecutter.use_github_workflow }}' != 'y':
        #all yml files
        github_folder = Path(PROJECT_DIRECTORY, '.github', '**')
        [Path(f).unlink for f in iglob(str(github_folder.joinpath('*.yml')), recursive=True)]
        #remove doc directory
        rmtree(str(Path(PROJECT_DIRECTORY, '.github')))


    if '{{ cookiecutter.use_sphinx }}' != 'y':
        #all doc files
        doc_files_search = Path(PROJECT_DIRECTORY, 'docs', '**')
        [Path(f).unlink for f in iglob(str(doc_files_search.joinpath('*.*')), recursive=True)]
        #remove doc directory
        rmtree(str(Path(PROJECT_DIRECTORY, 'docs')))

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file(str(Path('docs').joinpath('author_link.rst')))

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

    #remove sample application files not chosen by user
    chosen_app_example = '{{ cookiecutter.cmd2_example }}'
    all_possible_examples = ['first_app', 'arg_decorators', 'environment', 'internal_plugin']

    search_str = Path(PROJECT_DIRECTORY).joinpath('**/*.py')
    python_files = [Path(f) for f in iglob(str(search_str), recursive=True)
                 if Path(f).stem in all_possible_examples]
                    
    #remove all files that weren't chosen
    [f.unlink() for f in python_files if f.stem != chosen_app_example]
   
    #rename chosen file to app.py
    [os.rename(str(f), str(f.parent.joinpath('app.py'))) for f in python_files if f.stem == chosen_app_example]

    #remove plugin directory if the cmd example is not internal_plugin
    if 'internal_plugin' not in chosen_app_example:
        plugin_dir_search = Path(PROJECT_DIRECTORY).joinpath('**/plugins')
        [rmtree(d) for d in iglob(str(plugin_dir_search), recursive=True)]
        base_plugin_search = Path(PROJECT_DIRECTORY).joinpath('**/base_plugin.py')
        [Path(d).unlink() for d in iglob(str(base_plugin_search), recursive=True)]

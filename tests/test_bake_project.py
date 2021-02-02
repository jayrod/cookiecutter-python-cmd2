import os
from contextlib import contextmanager
from cookiecutter.utils import rmtree
from pathlib import Path
from glob import iglob

@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert 'setup.py' in found_toplevel_files
        assert 'tests' in found_toplevel_files
        assert 'LICENSE' in found_toplevel_files


def test_bake_non_internal_plugin_example(cookies):
    with bake_in_temp_dir(
            cookies,
            extra_context={'cmd2_example': 'first_app'}
        ) as result:

        #there should be no plugin directory
        plugins_search = Path(result.project).joinpath('**/plugins')
        plugins = [f for f in iglob(str(plugins_search), recursive=True)]
        assert not plugins

        #there shouldn't be a base_plugin file
        search = Path(result.project).joinpath('**/base_plugin.py')
        base_plugin = [f for f in iglob(str(search), recursive=True)]
        assert not base_plugin

def test_bake_without_author_file(cookies):
    with bake_in_temp_dir(
        cookies,
        extra_context={'create_author_file': 'n'}
    ) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert 'AUTHORS.rst' not in found_toplevel_files
def test_bake_without_banner(cookies):
    with bake_in_temp_dir(
        cookies,
        extra_context={'create_banner': 'n'}
    ) as result:
        #screen file should not have been generated
        search_str = Path(result.project.dirname).joinpath('**/common/screen.py')
        files = [f for f in iglob(str(search_str), recursive=True)]
        assert not files

        #Intro banner code should not be in app file
        search_str = Path(result.project.dirname).joinpath('**/app.py')
        files = [Path(f) for f in iglob(str(search_str), recursive=True)]
        assert files
       
        #make sure banner code is not present
        app_file_content = files[0].read_text()
        assert 'self.intro' not in app_file_content
        assert 'import banner' not in app_file_content

import nox
from pathlib import Path


@nox.session(reuse_venv=True)
def test(session):
    session.install('cookiecutter')
    session.install('pytest')
    session.install('pytest-cookies')
    session.run('pytest', 'tests', 
            env={'PYTHONPATH': Path().cwd()})

import nox
from pathlib import Path


@nox.session(reuse_venv=True)
def lint(session):
    session.install('isort')
    session.install('black')
    session.run('isort', 'src')
    session.run('black', 'src')
    

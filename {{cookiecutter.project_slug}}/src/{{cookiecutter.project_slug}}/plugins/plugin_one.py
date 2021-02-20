from cmd2 import with_default_category, CommandSet, Statement
from {{cookiecutter.project_slug}}.common.base_plugin import BaseCommandSet

@with_default_category('Plugins')
class AutoLoadCommandSet(CommandSet, BaseCommandSet):

    def __init__(self):
        super().__init__()

    def do_hello(self, _: Statement):
        self._cmd.poutput('Hello')

    def do_world(self, _: Statement):
        self._cmd.poutput('World')

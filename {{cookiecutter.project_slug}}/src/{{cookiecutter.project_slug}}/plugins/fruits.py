from cmd2 import CommandSet, with_default_category, Statement

from {{ cookiecutter.project_slug }}.common.base_plugin import BaseCommandSet

@with_default_category('Fruits')
class LoadableFruits(CommandSet, BaseCommandSet):
    def __init__(self):
        super().__init__()

    def do_apple(self, _: Statement):
        self._cmd.poutput('Apple')

    def do_banana(self, _: Statement):
        self._cmd.poutput('Banana')

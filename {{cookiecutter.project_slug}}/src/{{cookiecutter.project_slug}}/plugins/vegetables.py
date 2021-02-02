from cmd2 import CommandSet, with_default_category, Statement

from {{ cookiecutter.project_slug }}.common.base_plugin import BaseCommandSet

@with_default_category('Vegetables')
class LoadableVegetables(CommandSet, BaseCommandSet):
    def __init__(self):
        super().__init__()

    def do_arugula(self, _: Statement):
        self._cmd.poutput('Arugula')

    def do_bokchoy(self, _: Statement):
        self._cmd.poutput('Bok Choy')


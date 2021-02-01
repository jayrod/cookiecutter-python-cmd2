# coding=utf-8
import cmd2
import cmd2_ext_test
import pytest

from {{ cookiecutter.project_slug }}.app import App

class ExampleTester(cmd2_ext_test.ExternalTestMixin, App):
    def __init__(self, *args, **kwargs):
        # gotta have this or neither the plugin or cmd2 will initialize
        super().__init__(*args, **kwargs)


class TestApplication:

    def setup_method(self, method):
        self.app = ExampleTester()

    def teardown_method(self, method):
        self.app.fixture_teardown()

    def test_something(self):

        self.app.fixture_setup()
        out = self.app.app_cmd("something")
        assert isinstance(out, cmd2.CommandResult)



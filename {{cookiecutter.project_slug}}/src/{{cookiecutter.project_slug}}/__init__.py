""" Entry point of cmd2 application """
from {{cookiecutter.project_slug}}.app import App


def main():
    c = App()
    c.cmdloop()


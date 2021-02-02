""" Entry point of cmd2 application """
from {{cookiecutter.project_slug}}.app import App

import pluginlib

def main():
    {% if cookiecutter.cmd2_example == 'internal_plugin' %}
    #load plugins
    loader = pluginlib.PluginLoader(modules=['{{ cookiecutter.project_slug }}.plugins'])
    plugins = loader.plugins

    my_sets = [o() for o in plugins.CommandSets.values()]

    c = App(command_sets=my_sets)
    {% else %}
    c = App()
    {% endif %}
    c.cmdloop()

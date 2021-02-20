""" Entry point of cmd2 application """
from {{cookiecutter.project_slug}}.app import App
from pluginlib import PluginLoader

def main():

    loader = PluginLoader(modules=['{{cookiecutter.project_slug}}.plugins'])
    plugins = loader.plugins

    if 'CommandSets' not in plugins.keys():
        my_sets = []
    else:
        my_sets = [o() for o in plugins.CommandSets.values()]

    c = App()
    c.cmdloop()

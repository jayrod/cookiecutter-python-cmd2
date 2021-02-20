""" Entry point of cmd2 application """
from {{cookiecutter.project_slug}}.app import App
from pluginlib import PluginLoader

def main():

    #Load plugins from internal module
    loader = PluginLoader(modules=['{{cookiecutter.project_slug}}.plugins'])
    #because autoload is set to True by default plugins are loaded
    loader.plugins

    c = App()
    c.cmdloop()

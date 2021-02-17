from cmd2 import Settable, Cmd

class DefaultSettings:

    @classmethod
    def add_default_settings(self, app: Cmd):

        # Make maxrepeats settable at runtime
        app.maxrepeats = 3
        app.add_settable(Settable('maxrepeats', int, 'max repetitions for speak command'))


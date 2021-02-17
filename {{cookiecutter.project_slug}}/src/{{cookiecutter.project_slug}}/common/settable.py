from cmd2 import Settable, Cmd

class DefaultSettings:

    @classmethod
    def add_default_settings(self, app: Cmd):

        app.some_setting = 'Change this default setting'

        app.add_settable(
                    Settable('some_setting',
                        str, 
                        'Setting description'
                        )
                )


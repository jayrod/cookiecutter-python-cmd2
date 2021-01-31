#!/usr/bin/env python
# coding=utf-8
"""
A sample application for cmd2 demonstrating customized environment parameters
"""
import cmd2

{% if cookiecutter.create_banner == 'y' -%}
from {{cookiecutter.project_slug}}.common.screen import banner
{% endif %}



class App(cmd2.Cmd):
    """ Example cmd2 application. """

    def __init__(self):
        super().__init__()
        self.degrees_c = 22
        self.sunny = False
        self.add_settable(cmd2.Settable('degrees_c',
                                        int,
                                        'Temperature in Celsius',
                                        onchange_cb=self._onchange_degrees_c
                                        ))
        self.add_settable(cmd2.Settable('sunny', bool, 'Is it sunny outside?'))

        {% if cookiecutter.create_banner == 'y' -%}
        #set banner
        self.intro = banner()
        {% endif %}


    def do_sunbathe(self, arg):
        """Attempt to sunbathe."""
        if self.degrees_c < 20:
            result = "It's {} C - are you a penguin?".format(self.degrees_c)
        elif not self.sunny:
            result = 'Too dim.'
        else:
            result = 'UV is bad for your skin.'
        self.poutput(result)

    def _onchange_degrees_c(self, param_name, old, new):
        # if it's over 40C, it's gotta be sunny, right?
        if new > 40:
            self.sunny = True


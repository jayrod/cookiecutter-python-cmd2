#!/usr/bin/env python
# coding=utf-8
"""
A simple application using cmd2 which demonstrates 8 key features:

    * Settings
    * Commands
    * Argument Parsing
    * Generating Output
    * Help
    * Shortcuts
    * Multiline Commands
    * History
"""

import argparse
import cmd2
{% if cookiecutter.create_banner == 'y' -%}
from {{cookiecutter.project_slug}}.common.screen import banner
{% endif -%}
{% if cookiecutter.default_settings == 'y' -%}
from {{cookiecutter.project_slug}}.common.settable import DefaultSettings
{% endif -%}
from {{cookiecutter.project_slug}}.app_cmd_args import ParserFactory
from cmd2 import Settable

class App(cmd2.Cmd):
    """A simple cmd2 application."""

    def __init__(self):
        shortcuts = cmd2.DEFAULT_SHORTCUTS
        shortcuts.update({'&': 'speak'})
        super().__init__(multiline_commands=['orate'], shortcuts=shortcuts)

        {% if cookiecutter.create_banner == 'y' -%}
        #set banner
        self.intro = banner()
        {% endif -%}
        {% if cookiecutter.default_settings == 'y' -%}
        #add default settings
        DefaultSettings.add_default_settings(self)
        {% endif %}

        self.maxrepeats
        self.add_settable(Settable('maxrepeats', int, 'Max repetitions for speak command'
            ))

    @cmd2.with_argparser(ParserFactory.parser('speak_parser'))
    def do_speak(self, args):
        """Repeats what you tell me to."""
        words = []
        for word in args.words:
            if args.piglatin:
                word = '%s%say' % (word[1:], word[0])
            if args.shout:
                word = word.upper()
            words.append(word)
        repetitions = args.repeat or 1
        for _ in range(min(repetitions, self.maxrepeats)):
            # .poutput handles newlines, and accommodates output redirection too
            self.poutput(' '.join(words))

        #always set the last result 
        self.last_result = ' '.join(words)

    # orate is a synonym for speak which takes multiline input
    do_orate = do_speak



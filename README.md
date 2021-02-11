
Cookiecutter CMD2 Basic Project 
-------------------------------

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for a Python CMD2 application.

* GitHub repo: https://github.com/jayrod/cookiecutter-python-cmd2/
* Documentation: COMING SOON
* Free software: BSD license

Features of generated Application
--------

* Functional testing examples using [cmd2-ext-test](https://github.com/python-cmd2/cmd2-ext-test) vi pytest
* Nox lint via isort and black
* bump2version : Pre-configured version bumping with a single command



Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/jayrod/cookiecutter-python-cmd2.git

Options
-------

| Field        | Default                  | Description                                                                            |
|--------------|--------------------------|----------------------------------------------------------------------------------------|
| full_name    | Github User              | Used to describe the auther of this application.                                       |
| email        | voxebeg454@example.com   | How to get in touch with the author.                                                   |
| project_name | PythonBoilerplateCMD2    | This is the application name used during installation and in the README docutmentation |
| project_slug | {sanitized project_name} | Name of the python package                                                             |
| project_short_description| "Command Line Tool" | Short project description|
| command_name | cmd2 | command name used for invocation after installation|
| version | 0.1.0   | Initial software version |
| use_pytest |  yes   | Adds sample pytests |
| create_author_file |  yes   | Adds given full_name to an Author file|
| create_banner | yes   | Creates a placeholder banner |
| open_source_license | MIT license| Lets you choose a license structure|
| cmd2_example |  first_app | Allows for choice of several startup cmd2 examples|

[![asciicast](https://asciinema.org/a/388246.svg)](https://asciinema.org/a/388246)


Not Exactly What You Want?
--------------------------

Don't worry, you have options:

Fork This / Create Your Own
----------

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

* It's up to you whether or not to rename your fork/own version. Do whatever
  you think sounds good.

Or Submit a Pull Request
----------

I also accept pull requests on this, if they're small, atomic, and if they
make my own packaging experience better.

* [Nox](https://nox.thea.codes/en/stable/)
* [Sphinx](http://sphinx-doc.org/)
* [bump2version](https://github.com/c4urself/bump2version)
* [PyPi](https://pypi.python.org/pypi)

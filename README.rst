======================
Cookiecutter CMD2 Basic Project 
======================

Cookiecutter_ template for a Python package.

* GitHub repo: https://github.com/jayrod/cookiecutter-python-cmd2/
* Documentation: COMING SOON
* Free software: BSD license

Features
--------

* Testing setup with ``unittest`` and ``python setup.py test`` or ``pytest``
* Nox_ testing: Setup to easily test for Python 3.5, 3.6, 3.7, 3.8
* bump2version_: Pre-configured version bumping with a single command

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/jayrod/cookiecutter-python-cmd2.git

Then:

* Create a repo and put it there.
* Install the dev requirements into a virtualenv. (``pip install -r requirements_dev.txt``)
* Add a ``requirements.txt`` file that specifies the packages you will need for
  your project and their versions. For more info see the `pip docs for requirements files`_.


[![asciicast](https://asciinema.org/a/14.png)](https://asciinema.org/a/14)

Not Exactly What You Want?
--------------------------

Don't worry, you have options:

Fork This / Create Your Own
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

* It's up to you whether or not to rename your fork/own version. Do whatever
  you think sounds good.

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they
make my own packaging experience better.


.. _Nox: https://nox.thea.codes/en/stable/
.. _Sphinx: http://sphinx-doc.org/
.. _bump2version: https://github.com/c4urself/bump2version
.. _PyPi: https://pypi.python.org/pypi

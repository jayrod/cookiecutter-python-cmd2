.. {{cookiecutter.project_name}} documentation master file, created by
   sphinx-quickstart on Wed Feb 10 23:30:03 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to {{cookiecutter.project_name}}'s documentation!
=========================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   readme_link
   {% if cookiecutter.create_author_file == 'y' -%}
   author_link
   {% endif %}

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

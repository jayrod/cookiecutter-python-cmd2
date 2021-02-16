.PHONY: clean-pyc clean-build docs clean

help:
	@echo "clean        - remove all build, test, coverage and Python artifacts"
	@echo "clean-build  - remove build artifacts"
	@echo "clean-pyc    - remove Python file artifacts"
	{% if cookiecutter.use_pytest == 'y' -%}
	@echo "test         - run tests quickly with the default Python"
	{% endif -%}
	{% if cookiecutter.use_nox == 'y' -%}
	@echo "test-all     - run tests on every Python version with nox"
	{% endif -%}
	@echo "dist         - package"
	@echo "install      - install the package to the active Python's site-packages"


clean: clean-build clean-pyc clean-test

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
{% if cookiecutter.use_nox == 'y' -%}
	rm -rf .nox/
{% endif %}
{% if cookiecutter.use_pytest == 'y' -%}
test:
	pytest
{% endif %}

{% if cookiecutter.use_nox == 'y' -%}
test-all:
	nox -s test
{% endif %}

dist: clean
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean
	python setup.py install

